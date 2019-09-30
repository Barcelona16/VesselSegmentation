import re
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import csv
def writecsv(filename,x,y,z):
    f = open('test.csv','a+',encoding='utf-8',newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow([x,y,z])
    f.close()
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
            #print(lenofx)
            x=[] #346
            y=[] #386
            z=[] #118
            # r=[]
        elif(npoints!=0):
            npoints=npoints-1
            if(line[0]!="Points"):
                x.append(float(line[0]))
                y.append(float(line[1]))
                z.append(float(line[2]))
                writecsv("test.csv",float(line[0]),float(line[1]),float(line[2]))
                r.append(float(line[3]))
                radicus=float(line[3])
    cValue = ['r','y','g','b','r','y','g','b','r'] 
    #ax.scatter(x,y,z,c='r',linewidths=r,marker='.') 
    #plt.plot(x,y,z,markersize=r)
    # print(max(r))
    # print(min(r))
    # print(max(x))
    # print(max(y))
    # print(max(z))
    # print(len(r))   
    print(x)
    plt.show()
    #plt.savefig("examples.png")
drawTre("VascularNetwork.tre")