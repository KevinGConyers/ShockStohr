import sys
import os
import pyperclip

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

