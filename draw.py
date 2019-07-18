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
    r=[]
    npoints=0
    lenofx=0
    radicus=0
    ax = plt.axes(projection='3d')
    for line in alllines:
        line = re.split("[ ]",line)
        if(line[0]=="NPoints"):
            npoints=int(line[2])+1
            #ax.scatter(x,y,z,c='r',linewidths=r,marker='.') 
            plt.plot(x,y,z,linewidth=radicus*2)
            #plt.savefig("./vesselImg/examples"+str(lenofx)+".png")
            lenofx=lenofx+1
            print(lenofx)
            x=[]
            y=[]
            z=[]
            # r=[]
        elif(npoints!=0):
            npoints=npoints-1
            if(line[0]!="Points"):
                x.append(float(line[0]))
                y.append(float(line[1]))
                z.append(float(line[2]))
                r.append(float(line[3]))
                radicus=float(line[3])
    cValue = ['r','y','g','b','r','y','g','b','r'] 
    #ax.scatter(x,y,z,c='r',linewidths=r,marker='.') 
    #plt.plot(x,y,z,markersize=r)
    print(max(r))
    print(min(r))
    print(len(r))   
    plt.show()
    #plt.savefig("examples.png")
drawTre("./VesselData/Normal-002/AuxillaryData/VascularNetwork.tre")