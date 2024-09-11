import os
import shutil

def cleanfolder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        print("Directory does not exist.")

def cleanfile(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("File does not exist.")

if __name__ == "__main__":
    cleanfolder("./output/")
    cleanfile("convertAlignments.message.log")
    cleanfile("convertPronDict.message.log")
    cleanfile("inter_pron_dict.txt")
    cleanfile("wordTranscriptions.pkl")