import os
def change_name(location):
    directory = os.listdir(location)
    os.chdir(location)
    newlist = []
    for filename in directory:
        if filename.endswith(".mp3"):
            newlist.append(filename)
            os.rename(filename, filename[:-4])
        if filename.endswith(" - Copy"):
            newlist.append(filename)
            os.rename(filename, filename[:-6])
    print newlist
#C:\Users\Public\Music\Sample Music
dir = raw_input("Enter the directory you want to search \n")
change_name(dir)
