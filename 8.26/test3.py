#-*-coding:utf-8-*-
import os
import shutil

new_path='F:\\test2'

for derName,subfolders,filenames in os.walk('F:\\test1'):
    for i in range(len(filenames)):
        if filenames[i].endswith('.txt'):
            file_path=derName+'\\'+filenames[i]
            shutil.copy(file_path,new_path)