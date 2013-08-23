# simple kmeans implementation with linear nearest neighbors finding.
# a better implemenation would use a fortune algorithm or any other nearest neighbors


import random
import math


def euDistance(p1,p2): # maybe use a more tradicional optmized method ?
                       # function to calculate the euclidian distance
    dist = 0 
    for i in range(len(p1)):

        dist += (p1[i]-p2[i])*(p1[i]-p2[i])

    return math.sqrt(dist)




def findNearestNeighbors(clusters,points):# Function to find the for each cluster the set "c" of its nearest neighbors
    
    #initialize the sets
    c = [None]*len(points)

    for i in range(len(points)): # A loop to iterate over points on the space
        nearest = euDistance(points[i],clusters[0]) # initialize the nearest with the first cluster
        c[i] = 0  
        for j in range(1,len(clusters)):            
            distance = euDistance(points[i],clusters[j]) # calculate the distance to the cluster center
            if  distance < nearest:
                nearest = distance
                c[i] = j
        
    return c  
  
def sumVectors(v1,v2):  # "pythonic" way to sum vectors, zip merge both arrays  and we iterate over them
    
    return [x + y for x, y in zip(v1,v2)]
        

def divideArray(v1,scalar): # Also there is probably a more pythonic way. Dividing a vector with an scalar

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

def initRandom(k,dim,vrang):  # Initialize the points at random with the represented space.

    clusters = []
    for i in range(k):
        center = []
        for j in range(dim):
            center.append(random.randint(vrang[0],vrang[1]))
        
        clusters.append(center)
    
    return clusters                


      
def moveClustersCenters(c,pontos,clusters): # function to move the clusters center to the center of the its associated points

    newClusters = [[0]*len(pontos[0]) for _ in range(len(clusters))]  # initialize the new clusters centers " Pythonic way "

    conts =[0]*len(clusters)


    for i in range(len(pontos)): # sum each set that is related to each cluster center
        newClusters[c[i]] = sumVectors(newClusters[c[i]],pontos[i]) 
        conts[c[i]] +=1

    quantoMoveu = 0 # calculate how much each cluster has moved to its new center
    for i in range(len(clusters)):
        newClusters[i] = divideArray(newClusters[i],conts[i])  
        quantoMoveu +=  euDistance( newClusters[i] , clusters[i])
	

    return quantoMoveu/len(clusters),newClusters  # return the new clusters and how much they moved
        

def kmeans(data,k,erro):  # Pass a the data vectors and the desired k numbers of clusters

    #points = describeData()
    # data is a matriz with D dimensions and M neuros of data
    clusters = initForgy(k,data) # initialize the clusters using the forgy method.   
    #clusters = initRandom(9,256,(0,1))   UNCOMENT THIS TO INITIALIZE WITH THE RANDOM METHOD

   
    quantoMoveu = erro +1 # initialize how much it moved
    while quantoMoveu > erro:  # while the cluster has not moved enought 
        c=findNearestNeighbors(clusters,data)  # find neighboors
        quantoMoveu,newClusters=moveClustersCenters(c,data,clusters) # move cluster
       
        clusters = newClusters



    return clusters

def classify(clusters,data): # used to tell which cluster is the closest , basically by testing the distances

    closest = euDistance(clusters[0],data)
    closestid = 0
    for i in range(1,len(clusters)):
        dist = euDistance(clusters[i],data)
        if dist < closest:
            closest = dist
            closestid = i 

    return closestid
        
    
