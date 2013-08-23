
from readData import *
from imageshow import *
from kmeans import *

# MAIN PART
# read data from the multi databases

data3G1 = readData('../Databases/SimpleOCR/DB3/G1',False)
data3G2 = readData('../Databases/SimpleOCR/DB3/G2',False)
data2G1 = readData('../Databases/SimpleOCR/DB2/G1',False)
data2G2 = readData('../Databases/SimpleOCR/DB2/G2',False)
data1G12 = readData('../Databases/SimpleOCR/DB1',True)

print len(data1G12[0])

data = data3G1 + data3G2
#data = [[1,2],[3,4],[1,1]]

clusters=kmeans(data,10,0.001)

for idx,i in enumerate(data2G1):
    print "Numero",idx
    print "classificado ", classify(clusters,i)

for idx,i in enumerate(data2G2):
    print "Numero",idx
    print "classificado ",classify(clusters,i)

for idx,i in enumerate(data1G12):
    print "Numero ",idx
    print  "classificado ",classify(clusters,i)



showClusters(clusters)  # this functions is specific for the 256 dimensional case, printiing it to a image file.



