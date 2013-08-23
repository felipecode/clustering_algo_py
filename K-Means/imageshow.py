from PIL import Image

# Show data as image, specific for 16x16 !

def showClusters(clusters):

    for idx,i in enumerate(clusters): 

        str1 = ''.join(str(e) + ' ' for e in i)
        im= Image.new('1',(16,16))
        im.putdata(map(int,str1.split()))
        im.save('teste' +str(idx) + '.bmp','BMP')



