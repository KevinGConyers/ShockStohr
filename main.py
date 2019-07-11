#!/usr/bin/python
import sys
import argparse
def handleArgs():
# Allowed arguments are
# -f --file [filename] points to the file containing the encrypted data, if not provided a default file is produced in /home/$user/.ShockStohr/defaultstorage
# -c --clip if this flag is given the password is put on the clipboard using xclip
# -C --comm [command] if this flag is given, the command is ran with the provided password [EXPERIMENTAL]
    parser = argparse.ArgumentParser(description='Command line password manager')
    parser.add_argument('-f', '--filename', nargs='?', dest='filename', help='provide a filename, if not provided, a default is used')
    parser.add_argument('-m', '--mode', dest='mode', help='sets the mode.', required='true')
    args = vars(parser.parse_args(sys.argv[1:]))
    if args["filename"] is 'None':
        args["filename"] = 'default'
    return args

def main():
    args = handleArgs()
    [print(args[i]) for i in args]


main()
