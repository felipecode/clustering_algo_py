from PIL import Image




def showClusters(clusters):

    for idx,i in enumerate(clusters): # i eh um dos clusters

        str1 = ''.join(str(e) + ' ' for e in i) # convertendo para string
        #print len(str1)

        #print rstr1
        im= Image.new('1',(16,16))
        im.putdata(map(int,str1.split()))
        im.save('teste' +str(idx) + '.bmp','BMP')



