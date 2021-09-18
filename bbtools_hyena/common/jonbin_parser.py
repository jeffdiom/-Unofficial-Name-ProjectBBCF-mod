import os, struct, glob, zlib, subprocess, sys, json, re
from collections import OrderedDict
import struct

def parse(f):
    data = OrderedDict()
    data["Header"] = OrderedDict()
    data["Header"]["Images"] = []

    # Jonbin files start with JONB
    f.read(4)

    # Extract file header
    imageCount, = struct.unpack("<H", f.read(2))
    data["Header"]["ImageCount"] = imageCount

    for i in range(imageCount):
        data["Header"]["Images"].append(f.read(32).decode("latin1").strip('\0'))

    data["Header"].update(zip([
                                "Header_Unknown1",
                                "Header_Unknown2",
                                "chunkCount", 
                                "Header_Unknown3", 
                                "hurtboxCount", 
                                "hitboxCount"
                                ], struct.unpack("<b5h", f.read(11))))

    data["Header"]["UnknownBoxCounts"]  = struct.unpack("<27h", f.read(54))
    data["Header"]["Header_Unknown4"]   = struct.unpack("<28B", f.read(28))

    data["Chunks"] = []

    # Extract chunk data
    for i in range(data["Header"]["chunkCount"]):

        data["Chunks"].append(OrderedDict(zip(
        [   "SrcX", "SrcY", "SrcWidth", "SrcHeight", 
            "X", "Y", "Width", "Height"
        ],  struct.unpack("<8f", f.read(8 * 4)))))
        
        data["Chunks"][i]["Unknown"]   = struct.unpack("<8I", f.read(8 * 4))
        data["Chunks"][i]["Layer"]     = struct.unpack("<I", f.read(4))
        data["Chunks"][i]["Unknown2"]  = struct.unpack("<3I", f.read(3 * 4))

    data["Hurtboxes"] = []
    data["Hitboxes"] = []
    data["UnknownBoxes"] = []

    # Extract hitboxes/hurtboxes data
    for i in range(data["Header"]["hurtboxCount"]):
        data["Hurtboxes"].append(OrderedDict(zip(["ID", "X", "Y", "Width", "Height"], 
                                 struct.unpack("<I4f", f.read(20)))))

    for i in range(data["Header"]["hitboxCount"]):
        data["Hitboxes"].append(OrderedDict(zip(["ID", "X", "Y", "Width", "Height"], 
                                 struct.unpack("<I4f", f.read(20)))))
    
    # Get one box for each unknown box type (add the count index as type for
    # debugging/reverse engineering purposes)
    for boxCountIndex in range(len(data["Header"]["UnknownBoxCounts"])):
        for boxIndex in range(data["Header"]["UnknownBoxCounts"][boxCountIndex]):
            data["UnknownBoxes"].append(OrderedDict(zip(["ID", "X", "Y", "Width", "Height"], 
                                                    struct.unpack("<I4f", f.read(20)))))
            data["UnknownBoxes"][-1]["Index"] = boxIndex
            data["UnknownBoxes"][-1]["BoxType"] = boxCountIndex
    
    # print(data["UnknownBoxes"])
    return data

def pack(f, data):

    f.write("JONB".encode("latin1"))
    
    f.write(struct.pack("<H", data["Header"]["ImageCount"]))

    for i in range(data["Header"]["ImageCount"]):
        f.write(struct.pack("<32s", str(data["Header"]["Images"][i].ljust(32, "\x00")).encode("latin1")))

    f.write(struct.pack("<b5h",
                        data["Header"]["Header_Unknown1"], 
                        data["Header"]["Header_Unknown2"], 
                        data["Header"]["chunkCount"], 
                        data["Header"]["Header_Unknown3"], 
                        data["Header"]["hurtboxCount"], 
                        data["Header"]["hitboxCount"], 
                        ))

    f.write(struct.pack("<27h", *data["Header"]["UnknownBoxCounts"]))
    f.write(struct.pack("<28B", *data["Header"]["Header_Unknown4"]))

    # Extract hitbox data
    for i in range(data["Header"]["chunkCount"]):
        f.write(
            struct.pack("<8f",    
                        data["Chunks"][i]["SrcX"],      data["Chunks"][i]["SrcY"], 
                        data["Chunks"][i]["SrcWidth"],  data["Chunks"][i]["SrcHeight"], 
                        data["Chunks"][i]["X"],         data["Chunks"][i]["Y"], 
                        data["Chunks"][i]["Width"],     data["Chunks"][i]["Height"]))
        f.write(struct.pack("<8I", *data["Chunks"][i]["Unknown"]))
        f.write(struct.pack("<I", *data["Chunks"][i]["Layer"]))
        f.write(struct.pack("<3I", *data["Chunks"][i]["Unknown2"]))

    for i in range(data["Header"]["hurtboxCount"]):
        f.write(
            struct.pack("<I4f", 
                        data["Hurtboxes"][i]["ID"], 
                        data["Hurtboxes"][i]["X"],      data["Hurtboxes"][i]["Y"], 
                        data["Hurtboxes"][i]["Width"],  data["Hurtboxes"][i]["Height"]))

    for i in range(data["Header"]["hitboxCount"]):
        f.write(
            struct.pack("<I4f", 
                        data["Hitboxes"][i]["ID"], 
                        data["Hitboxes"][i]["X"],       data["Hitboxes"][i]["Y"], 
                        data["Hitboxes"][i]["Width"],   data["Hitboxes"][i]["Height"]))

    for box in data["UnknownBoxes"]:
        f.write(struct.pack("<I4f", box["ID"], box["X"], box["Y"], box["Width"], box["Height"]))


def jonbin_parse(in_file, out_path):

    if not in_file.endswith(".jonbin"):
        print(f"This doesn't look like a json file : {os.path.split(in_file)[1]}")
        return

    fh_in = open(in_file, "rb")

    # Get the decompiled collision data
    result = parse(fh_in)

    # Dump it to a JSON file
    basename = os.path.split(in_file)[1]
    out_file = os.path.join(out_path, basename.replace(".jonbin", ".json"))

    fh_out = open(out_file, "w")

    file_data = json.dumps(result, indent=4)

    # Put the contents of all the arrays on the same line
    regex = r'(\[[ \d,]*)\n +((\d+,?)|\])'

    while (re.search(regex, file_data)):
        file_data = re.sub(regex, r'\1 \2', file_data)

    # Write the data to a json file
    fh_out.write(file_data)
    fh_out.close()

    fh_in.close()


def jonbin_pack(in_file, out_path):

    if not in_file.endswith(".json"):
        print(f"This doesn't look like a json file : {os.path.split(in_file)[1]}")
        return

    col_data = json.loads(open(in_file).read())

    basename = os.path.split(in_file)[1]
    out_file = os.path.join(out_path, basename.replace(".json", ".jonbin"))

    fh_out = open(out_file, "wb")

    pack(fh_out, col_data)

    fh_out.close()

if __name__ == "__main__":
    if ((len(sys.argv) < 4) or (len(sys.argv) > 5)) or ((sys.argv[1] != "unpack") and
                                (sys.argv[1] != "pack")):
        print("Usage: {sys.argv[0]} unpack <char_directory> <output_dir>")
        print("       {sys.argv[0]} pack <input_dir> <char_directory>")
    else:

        in_path = sys.argv[2]
        out_path = sys.argv[3]
        file_filter = None

        if len(sys.argv) == 5:
            file_filter = sys.argv[4]

        if (sys.argv[1] == "unpack"):

            for in_file in glob.glob(os.path.join(in_path, "*.jonbin")):

                if (file_filter is None) or (file_filter in in_file):
                    jonbin_parse(in_file, out_path)
        else :

            for in_file in glob.glob(os.path.join(in_path, "*.json")):

                if (file_filter is None) or (file_filter in in_file):
                    jonbin_pack(in_file, out_path)

        print("")
        print("DONE")
        print("")