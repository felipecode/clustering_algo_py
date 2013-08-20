# simple kmeans implementation with linear nearest neighbors finding.
# a better implemenation would use a fortune algorithm.


import random
import math
from readData import *
from imageshow import *

def euDistance(p1,p2): # maybe use a more tradicional optmized method ?

    dist = 0 
    for i in range(len(p1)):

        dist += (p1[i]-p2[i])*(p1[i]-p2[i])

    return math.sqrt(dist)




def findNearestNeighbors(clusters,points):

    
    #inicializa c
    c = [None]*len(points)

    for i in range(len(points)):
        nearest = 1000000   # inicializa nearest com um valor alto . NOT SAFE!
        for j in range(len(clusters)):
            
            distance = euDistance(points[i],clusters[j]) # calcula a distancia do ponto ao cluster center
            if  distance < nearest:
                nearest = distance
                c[i] = j
        
    return c  
  
def sumVectors(v1,v2):  # "pythonic" way, zip merge both arrays  and we iterate over them
    
    return [x + y for x, y in zip(v1,v2)]
        

def divideArray(v1,scalar): # Also there is probably a more pythonic way

    v2 = []
    for i in range(len(v1)):
        if v1[i] != 0:
            v2.append(v1[i]/scalar)
        else:
            v2.append(v1[i])

    return v2

def initForgy(k,data):
            
    return random.sample(data,k)# initialize clusters with a certain amount of dimensions using the Forgy Method
    # forgy initializes by taking data samples at random.
    # this is done by the python function that take 

def initRandom(k,dim,vrang):  # contains the range of values encontered

    clusters = []
    for i in range(k):
        center = []
        for j in range(dim):
            center.append(random.randint(vrang[0],vrang[1]))
        
        clusters.append(center)
    
    return clusters                


      
def moveClustersCenters(c,pontos,clusters):

    newClusters = [[0]*len(pontos[0]) for _ in range(len(clusters))] 
    #print "Clusters Entrada"
    #print clusters
    conts =[0]*len(clusters)
    #novos cluster centers
    #print " MOving clusters " 
    #print newClusters
    #print conts

    for i in range(len(pontos)):
        newClusters[c[i]] = sumVectors(newClusters[c[i]],pontos[i]) 
        # soma os pontos pertencentes a media
        conts[c[i]] +=1
    
    print " Numero em cada center "
    print conts
    quantoMoveu = 0 # calculamos o quanto moveu tirando a media do quanto moveu cada cluster
    for i in range(len(clusters)):
        newClusters[i] = divideArray(newClusters[i],conts[i])  
        quantoMoveu +=  euDistance( newClusters[i] , clusters[i])
	
    
    #divide e finaliza a media
    #print quantoMoveu
    #print "Novos clusters agora"
    #print newClusters  

    return quantoMoveu/len(clusters),newClusters
        

def kmeans(data,k,erro):
    # passa uma string de onde esta os dados e um k dizendo quantos clusters

    #points = describeData()
    # Pontos e uma matriz MxD , onde D e o numero de dimensos e M eh a quantidade dedados
    clusters = initForgy(k,data) # initialize the clusters using the forgy method.   
    #clusters = initRandom(9,256,(0,1))

    #print " Clusters Inicializados "
    #print clusters
    #showClusters(clusters)   
    print 'N Clusters ',len(clusters)
    quantoMoveu = erro +1 # initialize how much it moved
    while quantoMoveu > erro: 
        c=findNearestNeighbors(clusters,data)
        quantoMoveu,newClusters=moveClustersCenters(c,data,clusters)
        print newClusters ==clusters
        clusters = newClusters
        print quantoMoveu


    return clusters

def classify(clusters,data): # used to tell which cluster is the closest

    #print len(data)
    closest = euDistance(clusters[0],data)
    closestid = 0
    for i in range(1,len(clusters)):
        dist = euDistance(clusters[i],data)
        if dist < closest:
            closest = dist
            closestid = i 

    return closestid
        
    


#euDistance([1,1],[1,1])


#read data inclui todos os dados .txt


data3G1 = readData('../Databases/SimpleOCR/DB3/G1',False)
data3G2 = readData('../Databases/SimpleOCR/DB3/G2',False)
data2G1 = readData('../Databases/SimpleOCR/DB2/G1',False)
data2G2 = readData('../Databases/SimpleOCR/DB2/G2',False)
data1G12 = readData('../Databases/SimpleOCR/DB1',True)

print len(data1G12[0])

data = data3G1 + data3G2
#data = [[1,2],[3,4],[1,1]]

clusters=kmeans(data,9,0.001)

for idx,i in enumerate(data2G1):
    print "Numero",idx
    print "classificado ", classify(clusters,i)

for idx,i in enumerate(data2G2):
    print "Numero",idx
    print "classificado ",classify(clusters,i)

for idx,i in enumerate(data1G12):
    print "Numero ",idx
    print  "classificado ",classify(clusters,i)





showClusters(clusters)




	




