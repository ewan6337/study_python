import os

fname = "/home/user/Desktop/git/study_python/practice/input.txt"

if os.path.exists(fname):
    fi = open(fname, "r", encoding="utf-8")
    for data in fi:
        print(data)
    fi.close()
else:
    print("%s does not exist" % fname)
