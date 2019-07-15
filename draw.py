import re
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
def drawTre(address):
    f = open(address, "r")
    alllines=f.readlines()
    f.close()
    x=[]    
    y=[]
    z=[]
    npoints=0
    ax = plt.axes(projection='3d')
    for line in alllines:
        line = re.split("[ ]",line)
        if(line[0]=="NPoints"):
            npoints=float(line[2])+1
            plt.plot(x,y,z)
            x=[]
            y=[]
            z=[]
        elif(npoints!=0):
            npoints=npoints-1
            if(line[0]!="Points"):
                x.append(float(line[0]))
                y.append(float(line[1]))
                z.append(float(line[2]))
                #print(type(line[0]))
    plt.plot(x,y,z)
    plt.show()

drawTre("./VesselData/Normal-002/AuxillaryData/VascularNetwork.tre")