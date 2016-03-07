#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'

import os
import os.path

infnameFont = os.getcwd() + "/in/"
outfnameFont = os.getcwd() + "/out/"

filelist = []

for parent, dirnames, filenames in os.walk(infnameFont):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for dirname in dirnames:  # 输出文件夹信息
        print("parent is:" + parent)
        print("dirname is" + dirname)

    for filename in filenames:  # 输出文件信息
        print("parent is:" + parent)
        print("filename is:" + filename)
        filelist.append(filename)
        print("the full name of the file is:" + os.path.join(parent, filename))

print(filelist)
fileNameList = []
for file in filelist:
    if (file != '.DS_Store'):
        fileNameList.append(file.split('.')[0])

print(fileNameList)

cclist = ['CC_SYNTHESIZE(', 'CC_SYNTHESIZE_RETAIN(']

for namefile in fileNameList:
    infile = open(infnameFont + namefile + '.h', "r")
    outfile = open(outfnameFont + namefile + '.pkg', "w")
    print(namefile)
    begin = False
    for line in infile.readlines():
        if line.find('class ' + namefile) != -1:
            begin = True
            print('Begin')
        if begin:
            if line.find(cclist[0]) != -1 or line.find(cclist[1]) != -1:
                str = line[:line.find('//')]
                if str.find(cclist[0]) != -1:
                    str = str[line.find(cclist[0])+len(cclist[0]):line.find(');')]
                else:
                    str = str[line.find(cclist[1])+len(cclist[1]):line.find(');')]
                strlist = str.split(',')
                stringlist = []
                for s in strlist:
                    stringlist.append(s.strip())
                print(stringlist)
                if stringlist[0] != '':
                    line1 = stringlist[0] + ' ' + stringlist[1] + ';'
                    line2 = 'void ' + 'set' + stringlist[2] + '(' + line1 + ');'
                    line3 = stringlist[0] + ' ' + 'get' + stringlist[2] + '();'
                    outfile.writelines('    ' + line1 + '\n')
                    outfile.writelines('    ' + line2 + '\n')
                    outfile.writelines('    ' + line3 + '\n')
                    outfile.writelines('\n')
                pass
            elif line.find('private') != -1:
                pass
            elif line.find('#endif') != -1:
                pass
            else:
                outfile.writelines(line)
    infile.close()
    outfile.close()

