import os, sys, re

userPath = "/Users/taykara/user.txt"
files = [f for f in os.listdir(sys.path[0]) if ".ovpn" in f]
for f in files:
    print(f)
    #read input file
    fin = open(sys.path[0]+os.path.sep+f, "rt")
    #read file contents to string
    data = fin.read()
    #Add \n in the end of the string if there is not
    if "\n" not in data[-1] :
        data.join("\n")
    #find option auth-user-pass and replace its value if there is one
    toReplace = re.search('auth-user-pass(.*)\n', data).group(1)
    print("toReplace : "+toReplace)
    data = data.replace("auth-user-pass"+toReplace, "auth-user-pass "+userPath)
    #remove comp-lzo preceded or followed by \n to remove the line
    data = data.replace("\ncomp-lzo", "")
    data = data.replace("comp-lzo\n", "")
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(sys.path[0]+os.path.sep+f, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()