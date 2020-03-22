import os
import re
from PIL import Image
import cv2

# filePath = 'D:\\APS360\\imdb_crop\\00\\'

filePath = 'D:\\APS360\\Dataset'
# filePath = 'D:\\APS360\\test'

totalindex = 0
a = 0
b = 0
c = 0
d = 0

for folder in range(0,100):
    n = 0
    newfolder = str(folder).zfill(2)
    print(newfolder)
    nowpath = filePath + '\\' + newfolder
    print(nowpath)
    fileList=os.listdir(nowpath)
    for i in fileList:

        oldname = nowpath + os.sep + fileList[n]
        string = fileList[n]

        data = re.findall(r"\d+\.?\d*", string)
        print(data)
        # float(data[5])
        year = int(float(data[5]) - float(data[2]))
        print(year)

        # 设置新文件名
        # if(year <= 14) and (year > 0) and (a < 10000):
        if(year <= 14) and (year > 0):
            newname = 'D:\\APS360\\updated\\Children0-14' + os.sep + str(year) + 'age' + str(totalindex + 1) + '.jpg'
            # newname = 'D:\\APS360\\updated\\Children0-14' + os.sep + str(year) + 'age' + str(a + 1) + '.jpg'
            a = a + 1
        # if(year > 14) and (year <= 24) and (b < 10000):
        if(year > 14) and (year <= 24):
            newname = 'D:\\APS360\\updated\\Youth15-24' + os.sep + str(year) + 'age' + str(totalindex + 1) + '.jpg'
            # newname = 'D:\\APS360\\updated\\Youth15-24' + os.sep + str(year) + 'age' + str(b + 1) + '.jpg'
            b = b + 1
        # if(year > 24) and (year <= 64) and (c < 10000):
        if(year > 24) and (year <= 64):
            newname = 'D:\\APS360\\updated\\Adults25-64' + os.sep + str(year) + 'age' + str(totalindex + 1) + '.jpg'
            # newname = 'D:\\APS360\\updated\\Adults25-64' + os.sep + str(year) + 'age' + str(c + 1) + '.jpg'
            c = c + 1
        # if(year >= 65) and (year <= 122) and (d < 10000):
        if(year >= 65) and (year <= 122):
            newname = 'D:\\APS360\\updated\\Seniors65+' + os.sep + str(year) + 'age' + str(totalindex + 1) + '.jpg'
            # newname = 'D:\\APS360\\updated\\Seniors65+' + os.sep + str(year) + 'age' + str(d + 1) + '.jpg'
            d = d + 1

        im = Image.open(oldname)

        (x,y) = im.size #read image size
        print(x)
        print(y)
        if (x >= y-10) and (x <= y+10):
            x_s = 128
            y_s = 128
            out = im.resize((x_s,y_s),Image.ANTIALIAS)
            out.save(newname)

            # img = Image.open(newname).convert('LA')
            # final = filePath + os.sep + str(year) + 'age' + str(n + 1) + '.jpg'
            # img.save(final)

            image = cv2.imread(newname, cv2.IMREAD_GRAYSCALE)
            cv2.imwrite(newname, image)

            # os.rename(oldname, newname)
            # print(oldname, '======>', newname)

            n += 1
            totalindex += 1
        else:
            # print(i)
            # i = i + 1
            n = n + 1
            totalindex += 1
            # continue
    # newfolder = newfolder + 1