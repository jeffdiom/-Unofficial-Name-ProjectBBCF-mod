#! /usr/bin/python3

import os, json, sys
from collections import OrderedDict

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: bbcf_script_rebuilder.py infile.json outfile.json")
    else:
        commands = json.loads(open(sys.argv[1]).read())

        ordered_commands = OrderedDict()

        for command in OrderedDict(sorted(commands.items())):

            ord_command = OrderedDict()

            for k in sorted(commands[command].keys()):
                ord_command[k] = commands[command][k]

            ordered_commands[command] = ord_command

        with open(sys.argv[2], "w") as f_out:
            f_out.write(json.dumps(ordered_commands, indent=4))
