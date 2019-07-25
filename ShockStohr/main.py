#!/usr/bin/python
import argparse
import ShockStohr
import sys
import os


def handleArgs():
# Allowed arguments are
# -f --file [filename] points to the file containing the encrypted data, if not provided a default file is produced in /home/$user/.ShockStohr/defaultstorage
# -m --mode [mode] chose the moder to operate in. The possible modes are clip, add, and comm. Clip retrieves a password and puts in on your clipboard, add adds 
#   a password to the data file and comm runs a command with the username and password [Not yet implemented]
# -c if in command mode, this supplies the command to run
# -u [username] the user name to either retrieve the password for, or to store the password under
# -p [password] the password to store
# -n [Note] a note to help indentify the password
    parser = argparse.ArgumentParser(description='Command line password manager')
    #parser.add_argument('-f', '--filename',  dest='filename', action='store', default='default.shock', help='provide a filename, if not provided, a default is used, located in ~/.ShockStohr/default.shock')
    parser.add_argument('-m', '--mode', dest='mode', action='store', help='Sets the mode. Acceptable modes are clip and add', required='true')
    parser.add_argument('-u', dest='username', action='store', required='true')
    parser.add_argument('-p', dest='password', nargs='?', action='store', default='fail')
    parser.add_argument('-n', dest='note', nargs='?', action='store', default='fail')
    parser.add_argument('-k', dest='key', action='store', default='')
    args = parser.parse_args(sys.argv[1:])
    return args

def main():
    config = ShockStohr.loadConfig()
    args = handleArgs()
    home = os.path.expanduser("~")
    filepath = home + "/.ShockStohr/" + config["file"] + ".shock"

    if args.mode == 'add':
        if args.note  == 'fail':

            print('Please provide a note')
            exit()
        elif args.password == 'fail':
            print('Please provdice a password')
            exit()
        else:
            ShockStohr.addPassword(filepath, args.username, args.password, args.note)
            print("added the password for %s to the database" % (args.username))
    if args.mode == 'clip':
        ShockStohr.extractPassword(filepath, args.username)


main()
