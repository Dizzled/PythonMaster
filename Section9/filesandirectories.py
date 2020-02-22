import os

# Walk through directories in current directory an example of recursive functions operating on a recursive system
def listDirectories(s):

    def dirList(d):
        nonlocal tabStop # Inorder to declare a variable in a nested function this is the only way ie look for variable in closing scopes
        files = os.listdir(d)
        for f in files:
            currentDir = os.path.join(d, f)
            if os.path.isdir(currentDir):
                print("\t " * tabStop + "Directory " + f )
                tabStop += 1
                dirList(currentDir)
                tabStop -= 1
            else:
                print("\t" * tabStop + f)

    tabStop = 0
    if(os.path.exists(s)):
        print("Directories listing of " + s)
        dir_lists(s)
    else:
        print(s + " Does not exist")


# listing = os.walk('.')
#
# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print(d)
#     for file in files:
#         print(file)
listDirectories('.')