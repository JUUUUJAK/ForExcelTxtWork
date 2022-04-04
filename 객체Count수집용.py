
import os
import pandas as pd

myfiles = list()
outfile_name = "FullCount.csv"

def append_files_in_dir(root_dir, prefix):
    files = os.listdir(root_dir)
    for file in files:
        path = os.path.join(root_dir, file)
        if ".txt" in (prefix+path):
            myfiles.append((prefix+path))
        if os.path.isdir(path):
            append_files_in_dir(path,prefix)
    print("현재 작업 위치 - " + root_dir)
    if len(myfiles) == 0:
        return

def print_files_in_dir(out_file):
    for filename in myfiles:
        if ".txt" not in filename:
            continue
        file = open(filename)
        for line in file:
            out_file.write(line)
        out_file.write("\n")
        file.close()


if __name__ == "__main__":
    root_dir = "./"
    outfile = open(outfile_name, "w")
    append_files_in_dir(root_dir, "")
    print_files_in_dir(outfile)
    outfile.close()
    df = pd.read_csv(outfile_name, sep=" ", names=["class", "N1", "N2", "N3", "N4"])
    df['class'].value_counts(sort=False).to_csv("ClassCount.csv")

print("작업이 완료되었습니다.")
os.system('pause')
