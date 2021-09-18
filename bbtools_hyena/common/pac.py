import os, struct, glob, zlib, subprocess, sys

def extract_pac(filename, outpath):

    # constants (purely here for readability)
    BASE_PAC_HEADER_SIZE = 32
    BASE_FILE_HEADER_SIZE = 16

    basename = os.path.split(filename)[1]
    fh = open(filename, "rb")

    fh.seek(4)

    #extract header data
    DATA_START, TOTAL_SIZE, FILE_COUNT = struct.unpack("<3I", fh.read(12))
    UNK01, STRING_SIZE, UNK03, UNK04 = struct.unpack("<4I", fh.read(16))

    # Size of an entry is the determined by the offset to the first 
    # file data minus the header size; the file is formatted like so :
    # header|file_header_1|...|file_header_n|file_data_1|...|file_data_n
    ENTRY_SIZE = int((DATA_START - BASE_PAC_HEADER_SIZE) / FILE_COUNT)

    for i in range(0, FILE_COUNT):
        fh.seek(BASE_PAC_HEADER_SIZE + i * (ENTRY_SIZE))

        FILE_NAME = fh.read(STRING_SIZE).decode("latin1").strip('\0')

        FILE_ID, FILE_OFFSET, FILE_SIZE, UNK = struct.unpack(
            "<4I", fh.read(BASE_FILE_HEADER_SIZE))

        fh.seek(DATA_START + FILE_OFFSET)

        outFilename = os.path.join(outpath, FILE_NAME)

        out = open(outFilename, "wb")
        out.write(fh.read(FILE_SIZE))
        out.close()


def repack(in_dir, out_file):

    # constants (purely here for readability)
    BASE_PAC_HEADER_SIZE = 32
    BASE_FILE_HEADER_SIZE = 16
    FILE_NAME_LENGTH = 32
    FILE_HEADER_SIZE = BASE_FILE_HEADER_SIZE + FILE_NAME_LENGTH
    FILE_OFFSET = 4

    # open the output file handle with write permissions
    fh_out = open(out_file, "wb")

    # Get the list of input files
    file_list = []

    for root, directories, files in os.walk(in_dir):
        for file in files:
            if (    file.endswith(".jonbin") 
                or  file.endswith(".bin") 
                or  file.endswith(".hip")):

                file_list.append(os.path.join(in_dir, file))

    # Initialize the header variables
    data_start = BASE_PAC_HEADER_SIZE
    total_size = BASE_PAC_HEADER_SIZE
    file_count = len(file_list)
    string_size = FILE_NAME_LENGTH

    # Each new file increases the total size by its own size (duh)
    # and adds a new 32 byte part to the .pac's header
    for file in file_list:

        total_size += os.path.getsize(file) + FILE_HEADER_SIZE + FILE_OFFSET
        data_start += FILE_HEADER_SIZE

    # Write the archive header
    fh_out.write(
        struct.pack("<4s7i",
            bytes("FPAC", encoding="latin1"),
            data_start,
            total_size,
            file_count,
            1, # Unknown
            string_size,
            0, # Unknown
            0  # Unknown
        )
    )

    current_file_id = 0
    current_file_offset = 0

    # Write each file's header
    for file in file_list:

        # Get the path-independent file name
        basename = os.path.split(file)[1]

        # Open the bin file for reading
        fh_bin = open(file, "rb")
        bin_size = os.path.getsize(file)

        # Write the file's header
        fh_out.write(
            struct.pack('<' + str(FILE_NAME_LENGTH) + 's4i',
                bytes(basename, encoding="latin1"),
                current_file_id,
                current_file_offset,
                bin_size,
                0
            )
        )

        current_file_offset += bin_size

    # Write each file's contents
    for file in file_list:

        fh_bin = open(file, "rb")

        bin_size = os.path.getsize(file)
        fh_out.write(fh_bin.read(bin_size))
        fh_bin.close()

    fh_out.close()

if __name__ == "__main__":
    if ((len(sys.argv) < 4) or (len(sys.argv) > 5)) or ((sys.argv[1] != "unpack") and
                                (sys.argv[1] != "pack")):
        print("Usage: {sys.argv[0]} unpack <pac_directory> <output_dir>")
        print("       {sys.argv[0]} pack <input_dir> <output_path>")
    else:

        in_path = sys.argv[2]
        out_path = sys.argv[3]
        file_filter = None

        if len(sys.argv) == 5:
            file_filter = sys.argv[4]

        if (sys.argv[1] == "unpack"):

            for in_file in glob.glob(os.path.join(in_path, "*.pac")):

                if (file_filter is None) or (file_filter in in_file):
                    extract_pac(in_file, out_path)

        else :
            if (file_filter is None) or (file_filter in in_path):
                repack(in_path, out_path)

        print("")
        print("DONE")
        print("")