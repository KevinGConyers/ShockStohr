#!/usr/bin/python
import sys
import argparse
import os
import pyperclip


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
    config = loadConfig()
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
            addPassword(filepath, args.username, args.password, args.note)
            print("added the password for %s to the database" % (args.username))
    if args.mode == 'clip':
        extractPassword(filepath, args.username)


def extractPassword(filepath, username):
    if not os.path.exists(filepath):
        print("No file exists by that name, check your config file\n")
        exit()
    usernamelist = []
    passwordlist = []
    notelist = []
    with open(filepath, "r") as inputfile:
        for line in inputfile:
            if username in line:
                user, passw, note = line.split(',')
                usernamelist.append(user)
                passwordlist.append(passw)
                notelist.append(note)
    if len(usernamelist) > 1:
        print("Please choose an account with the correct note:\n")
        for x in range(0, len(usernamelist)):
                        print("%i) %s\t\t\t%s\n" % (x+1, usernamelist[x], notelist[x]))
        selected = int(input("Which account number:\n"))
        pyperclip.copy(passwordlist[selected-1]) #avoiding an off-by-one error
    else:
        pyperclip.copy(passwordlist[0])





def addPassword(filepath, username, password, note):
    if not os.path.isfile(filepath):
        print("No file exists by that name, creating at " + filepath)
        createFile(filepath)
    with open(filepath, "a") as outputfile:
        outputfile.write(username + ", " + password + ", " + note + "\n" )


def createFile(filepath):
    with open(filepath, "w+") as outputfile:
        outputfile.write("test, test, this is a default encryption test and should be ignored \n")

def loadConfig():
    configdict = {} 
    if os.path.exists("~/.ShockStohr/config"):
        with open("~/.ShockStohr/config", "r") as configfile:
            for line in configfile:
                attribute, value = line.replace(" ", "").split(":")
                configdict[attribute] = value
    else:
        with open("/usr/local/etc/ShockStohr/default_config", "r") as configfile:
            for line in configfile:
                attribute, value = line.replace(" ", "").replace("\t", "").strip("\n").split(":")
                configdict[attribute] = value
    return configdict
main()
