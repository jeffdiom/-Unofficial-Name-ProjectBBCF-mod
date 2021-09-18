#! /usr/bin/python3

import os
import sys
import struct
import glob
import zlib
import subprocess
import json
import inspect
from pac import *
from jonbin_parser import *
from new_bbcf_bbtag_script_parser import *
from bbcf_bbtag_script_rebuilder import *

characters = json.loads(open("static_db/bbcf/characters.json").read())

# Character scripts, palettes, images (in that order
# because images need palettes to be extracted),
# special effects and collision data
archive_types = {
    "scr" : 
    { 
        "name": "scripts",
        "pack_func" : rebuild_bbscript,
        "unpack_func" : parse_bbscript
    }, 
    
    "pal" : 
    { 
        "name": "palettes",
        "pack_func" : None,
        "unpack_func" : None 
    }, 
    
    "img" : 
    { 
        "name": "sprites",
        "pack_func" : None,
        "unpack_func" : None 
    }, 
    
    "vri" : 
    { 
        "name": "effects",
        "pack_func" : None,
        "unpack_func" : None 
    }, 
    
    "col" : 
    { 
        "name": "collisions",
        "pack_func" : jonbin_pack,
        "unpack_func" : jonbin_parse
    } 
}

def arc_contains_filters(string, filters):
    if isinstance(filters, list):
        #if the filters contain an archive type filter
        arc_filters = ([item for item in filters 
                        if item in archive_types
                        or (item in [archive_types[arc]["name"] for arc in archive_types])])

        if len(arc_filters) > 0:
            
            #return the number of archive types matched by the filter
            return len([item for item in arc_filters 
                        if (item in string) 
                        or (    (item in archive_types) 
                            and (archive_types[item]["name"] in string)
                            )
                        ])
        # return 1 if we're not filtering the archive types
        else:
            return 1
    else:
        return filters in string

def char_contains_filters(string, filters):
    if isinstance(filters, list):

        #if the filters contain a character filter
        char_filters = ([item for item in filters 
                        if item in characters.keys()
                        or item in characters.values()])

        if len(char_filters) > 0:

            #return the number of characters matched by the filter
            return len([item for item in char_filters 
                        if (item in string) 
                        or (    (item in characters)
                            and (characters[item] in string)
                            )
                        ])
        # return 1 if we're not filtering characters
        else:
            return 1
    else:
        return filters in string


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path) 

def decompile_arc_contents(char_dirs_in_path, char_dirs_out_path, decompile_function):
    
    # Process each character directory
    for root, directories, files in os.walk(char_dirs_in_path):

        for char_dir in directories:

            # Filter out unwanted characters/script types
            if not char_contains_filters(char_dir, file_filter):
                continue

            out_path = os.path.join(char_dirs_out_path, char_dir)
            mkdir(out_path) 

            print(f"  decompile {char_dir}")

            for unpacked_file in glob.glob(f"{root}{char_dir}/*"):
                try:
                    decompile_function(unpacked_file, out_path)
                except :

                    if(sys.exc_info()[0] is KeyboardInterrupt):
                        sys.exit("Interrupted by user")
                    
                    print("    Failed.")
                    traceback.print_exc()

def recompile_arc_contents(char_dirs_in_path, char_dirs_out_path, recompile_function):

    # Process each character directory
    for root, directories, files in os.walk(char_dirs_in_path):

        for char_dir in directories:

            out_path = os.path.join(char_dirs_out_path, char_dir)

            # Filter out unwanted characters/script types
            if not char_contains_filters(out_path, file_filter):
                continue

            mkdir(out_path) 

            print(f"  recompile {char_dir}")

            for unpacked_file in glob.glob(f"{root}{char_dir}/*"):
                try:
                    recompile_function(unpacked_file, out_path)
                except:

                    if(sys.exc_info()[0] is KeyboardInterrupt):
                        sys.exit("Interrupted by user")
                    
                    print("    Failed.")
                    traceback.print_exc()

def bbcf_repack(in_path, out_path, file_filter):

    # Define and create input and output paths
    decompiled = os.path.join(in_path, "decompiled/")
    recompiled = os.path.join(in_path, "recompiled/")

    if not os.path.exists(decompiled):
        print(f"Error, no decompiled directory in {in_path}")
        exit(1)

    mkdir(out_path) 
    mkdir(recompiled) 

    # Make a recompiled folder for each archive type
    for arc in archive_types:
        mkdir(recompiled + archive_types[arc]["name"])

    print(" ")
    print("============================")
    print("    RECOMPILING BINARIES    ")
    print("============================")
    print(" ")

    for arc in archive_types:

        decompile_path = decompiled + archive_types[arc]["name"]
        recompile_path = recompiled + archive_types[arc]["name"]

        if  (   
                arc_contains_filters(decompile_path, file_filter)
            and (archive_types[arc]["unpack_func"] is not None) 
            ):

            print("Recompiling " + archive_types[arc]["name"])
            recompile_arc_contents( f"{decompile_path}/",
                                    f"{recompile_path}/",
                                    archive_types[arc]["pack_func"])

    print(" ")
    print("============================")
    print("     REBUILDING ARCHIVES    ")
    print("============================")
    print(" ")

    # Rebuild each archive directory into a .pac
    for arc in archive_types:

        if not arc_contains_filters(arc, file_filter):
            continue

        for root, directories, files in os.walk(recompiled + archive_types[arc]["name"] + "/"):

            for char_dir in directories:

                if not char_contains_filters(char_dir, file_filter):
                    continue

                # get the character digram from the character folder name
                char_digram = list(characters.keys())[list(characters.values()).index(char_dir)]
                out_file = "char_" + char_digram + "_" + arc + ".pac"

                archive_in_path  = os.path.join(root, f"{char_dir}/")
                archive_out_path = os.path.join(out_path, out_file)

                print (f"Building {archive_out_path}")
                repack(archive_in_path, archive_out_path)

def bbcf_unpack(in_path, out_path, file_filter):

    # Create output paths
    extracted = os.path.join(out_path, "extracted/")
    decompiled = os.path.join(out_path, "decompiled/")

    mkdir(out_path) 
    mkdir(extracted) 
    mkdir(decompiled)

    # Make an extracted and decompiled folder for each archive type
    for arc in archive_types:
        mkdir(extracted + archive_types[arc]["name"])
        mkdir(decompiled + archive_types[arc]["name"])

    # Process each character archive
    for filename in glob.glob(os.path.join(in_path, 'char_*.pac')):

        file_type = ""

        # print(arc_contains_filters(filename, file_filter), char_contains_filters(filename, file_filter), filename, file_filter)
        if (not char_contains_filters(filename, file_filter)
            or not arc_contains_filters(filename, file_filter)):
            continue

        if "boss" in filename:
            continue

        # Get file type
        for arc in archive_types:
            if arc in filename:
                file_type = archive_types[arc]["name"]

        # get char name in the filename
        char_name = [characters[char] for char in characters if "_" + char + "_" in filename]

        if len(char_name) > 0:
            char_name = char_name[0]
        else:
            continue

        out_path = os.path.join(extracted + file_type, f"{char_name}/")
        mkdir(out_path)

        basename = os.path.split(filename)[1]

        # Extract the .bin files from the .pac
        print(f"Extracting {basename} to {out_path}")

        try:
            extract_pac(filename, out_path)
        except:

            if(sys.exc_info()[0] is KeyboardInterrupt):
                sys.exit("Interrupted by user")
            
            print("    Failed.")
            traceback.print_exc()

    for arc in archive_types:

        extract_path = extracted + archive_types[arc]["name"]
        decompile_path = decompiled + archive_types[arc]["name"]

        if  (   
                (archive_types[arc]["unpack_func"] is not None) 
            and arc_contains_filters(extract_path, file_filter)
            ):

            print("Decompile " + archive_types[arc]["name"])
            decompile_arc_contents( f"{extract_path}/",
                                    f"{decompile_path}/",
                                    archive_types[arc]["unpack_func"])

if __name__ == "__main__":
    if (len(sys.argv) < 4) or ((sys.argv[1] != "unpack") and (sys.argv[1] != "pack")):
        print("Usage:bbcf_packer.py unpack <char_directory> <output_dir>")
        print("      bbcf_packer.py pack <input_dir> <char_directory>")
    else:

        in_path = sys.argv[2]
        out_path = sys.argv[3]
        file_filter = []

        for i in range(4, len(sys.argv)):
            file_filter.append(sys.argv[i])

        if (sys.argv[1] == "unpack"):
            bbcf_unpack(in_path, out_path, file_filter)
        else :
            bbcf_repack(in_path, out_path, file_filter)

        print("")
        print("DONE")