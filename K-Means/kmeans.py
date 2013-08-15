import random

def euDistance(p1,p2)

    dist = 0 
    for i in range(len(p1)):

        dist += (p1[i]-p2[i])*(p1[i]-p2[i])

    return sqrt(dist)

def describeData(path) # recebe o arquivo onde estao os dados, funcao deve ser reimplementada para cada tipo de dado

    points = []

    f=open('/Dataset/data.txt', 'r')  # open file for reading
    # readdata
    
    
    return points


def findNearestNeighbors(clusters,points)

    
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
  
def sumVectors(v1,v2):
    
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i] + v2[i])

    return v3
        

def divideArray(v1,scalar):

    v2 = []
    for i in range(len(v1)):
        v2.append(v1[i]/scalar)

    return v2

      
def moveClusterCenters(c,pontos,clusters):

    newClusters = [0*len(clusters[1])]*len(clusters)
    conts =[0]*len(clusters)
    #novos cluster centers

    for i in range(len(pontos)):
        newClusters[c[i]] = sumVectors(newClusters[c[i]],pontos[i]) 
        # soma os pontos pertencentes a media
        conts[c[i]] +=1
    
    quantoMoveu = 0 # calculamos o quanto moveu tirando a media do quanto moveu cada cluster
    for i in range(len(clusters)):
        newClusters[i] = divideArray(newClusters[i],conts[i])
        quantoMoveu += abs(newClusters[i] - clusters[i])
        #divide e finaliza a media
    
    clusters = newClusters
    return quantoMoveu/len(clusters)
        

def clusteriza(data,k,erro)
    # passa uma string de onde esta os dados e um k dizendo quantos clusters

    points = describeData()
    # Pontos e uma matriz MxD , onde D e o numero de dimensos e M eh a quantidade dedados
    clusters = initializeClusters()
    # clusters sao inicializados
    while quantoMoveu > erro:

	    c=findNearestNeighbors(clusters,points)
	    quantoMoveu=moveClustersCenters(c,pontos,clusters)


    return clusters



    





	




