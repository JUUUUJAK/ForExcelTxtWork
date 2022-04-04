import pandas as pd
import os
from openpyxl import load_workbook, workbook
import time


def append_files_in_dir(root_dir, prefix):
    myfiles = list()
    files = os.listdir(root_dir)
    for file in files :
        path = os.path.join(root_dir, file)
        if ".txt" in (prefix + path):
            myfiles.append((prefix+path))
        if os.path.isdir(path):
            append_files_in_dir(path, prefix)
    print("현재 작업 위치 - " + root_dir)

    if len(myfiles) == 0 :
        return
    outfile_name = root_dir + ".csv"
    outfile = open(outfile_name, "w")
    validation(outfile,myfiles)
    outfile.close()


def validation(out_file,myfiles):
    dupcount = 0
    counter = 0
    for filename in myfiles:
        if ".txt" not in filename:
           continue
        try:

            file = open(filename)
            df = pd.read_csv(file,sep=" ",header=None, names=['Class', 'Vec1', 'Vec2', 'Vec3', 'Vec4']).round(4)

            filename2 = filename.replace("검수", "원본")
            file2 = open(filename2)
            df2 = pd.read_csv(file2, sep=" ",header=None, names=['Class', 'Vec1', 'Vec2', 'Vec3', 'Vec4']).round(4)

            df_row = pd.concat([df, df2], ignore_index=True)

            col = list(df.columns)
            df_grp = df_row.groupby(col)
            df_di = df_grp.groups
            idx = [x[0] for x in df_di.values() if len(x) == 1]


            if df_row.loc[idx, :].empty:
                print('현재 작업 - ' + filename + ', 수정되지 않았습니다.')
            else:
                dupcount = dupcount + 1
                print('현재 작업 - ' + filename + ', 카운터 1 추가 - ' + str(dupcount))
                out_file.write(filename)
                out_file.write('\n')
            counter = counter + 1


        except FileNotFoundError:
            print(filename+' - 없는 파일입니다.')
            out_file.write(filename+' - 없는 파일')
            out_file.write('\n')

    out_file.write('\n작업량 = ' + str(counter))
    out_file.write('\n수정량 = ' + str(dupcount))


if __name__ == '__main__':
    root_dir = os.getcwd()
    files = os.listdir(root_dir)
    append_files_in_dir(root_dir,"")
    print('작업이 완료되었습니다.')
    os.system('pause')




