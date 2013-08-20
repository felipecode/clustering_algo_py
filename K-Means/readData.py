import dircache
import re

def readData(path,pop): # recebe o arquivo onde estao os dados, funcao deve ser reimplementada para cada tipo de dado



    files=dircache.listdir(path)  # lista os arquivos existentes no diretorio
    #print files
    points = []
    for i in files:    # iterate over the files

        if i[-3:] =='txt':
            f=open(path+ '/' +i, 'r')  # open file for reading
            # readdata
            a = f.read()
            m = re.compile('[\W]+')
            splited = m.split(a)
            
            if pop:
                splited.pop(0)

            splited.pop(len(splited)-1)
            splited = [int(i) for i in splited] #convert the elements to int
            if pop:            
                for j in range(9):
	                points.append(splited[j*256:(j+1)*256])
            else:
                points.append(splited)
               
            f.close()
                 
    

  
    
    # here we assume 256 dimensions and 10 data points, that is the case for the group 1
    #print points
    return points
