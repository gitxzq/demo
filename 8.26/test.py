#-*-coding:utf-8-*-

import os
path='F:\\test\\'
m=20
n=30
for i in range(m):
    foldername = path + str(i)
    isExists=os.path.exists(foldername)
    mkpath = foldername + '\\'

    if not isExists:
        os.makedirs(foldername)
        for j in range(n):
            filename = mkpath + str(j) + '.txt'
            isfileExists = os.path.exists(filename)
            if not isfileExists:
                f = open(mkpath + str(j) + '.txt', 'w')
                f.write('this is' + ' ' + str(j) + ' text')

                f.close()
                print('创建%s目录成功,进入目录，创建%s号文件成功' % (i, j))
            else:
                print('创建%s目录成功,进入目录,发现%s号文件已经存在 ' % (i, j))
                continue
            j = j + 1

    else:
        for k in range(n):
            filename = mkpath + str(k) + '.txt'
            isfileExists = os.path.exists(filename)
            if not isfileExists:
                f = open(mkpath + str(k) + '.txt', 'w')
                f.write('this is' +' ' + str(k) + ' text')

                f.close()
                print('%s目录已经存在,进入目录，创建%s号文件成功' %(i,k) )
            else:
                print('%s目录已经存在,进入目录,发现%s号文件已经存在 '%(i,k))
                continue
            k = k + 1
        continue





