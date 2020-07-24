import os, sys, re

userPath = "/Applications/Tunnelblick.app/Contents/user.txt"
files = [f for f in os.listdir(sys.path[0]) if ".ovpn" in f]
for f in files:
    print(f)
    #read input file
    fin = open(sys.path[0]+os.path.sep+f, "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    toReplace = re.search('auth-user-pass(.*)\n', data).group(1)
    print("toReplace : "+toReplace)
    data = data.replace("auth-user-pass"+toReplace, "auth-user-pass "+userPath)
    data = data.replace("comp-lzo", "")
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(sys.path[0]+os.path.sep+f, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()