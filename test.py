import os
import numpy
import SimpleITK
import matplotlib.pyplot as plt
 
def sitk_show(img, title=None, margin=0.0, dpi=20):
    nda = SimpleITK.GetArrayFromImage(img)
    #print(nda.size)
    #spacing = img.GetSpacing()
    #print(spacing)
    figsize = (1 + margin) * nda.shape[0] / dpi, (1 + margin) * nda.shape[1] / dpi
    #print(figsize)
    #extent = (0, nda.shape[1]*spacing[1], nda.shape[0]*spacing[0], 0)
    extent = (0, nda.shape[1], nda.shape[0], 0)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_axes([margin, margin, 1 - 2 * margin, 1 - 2 * margin])
 
    plt.set_cmap("gray")
    ax.imshow(nda, extent=extent, interpolation=None)
 
    if title:
        plt.title(title)
 
    plt.show()
dataNum="002" # data num
# Paths to the .mhd files
filenameT1 = "./VesselData/Normal-"+dataNum+"/DTI/Normal"+dataNum+"-DTI.mha"   #弥散张量图像 
filenameT2 = "./VesselData/Normal-"+dataNum+"/T1-Flash/Normal"+dataNum+"-T1-Flash.mha"
filenameT3 = "./VesselData/Normal-"+dataNum+"/MRA/Normal"+dataNum+"-MRA.mha"
filenameT4 = "./VesselData/Normal-"+dataNum+"/T2/Normal"+dataNum+"-T2.mha"
filenameT5 = "./VesselData/Normal-"+dataNum+"/AuxillaryData/SkullStripped-T1-Flash.mha"
 
# Slice index to visualize with 'sitk_show'
idxSlice = 95
 
# int label to assign to the segmented gray matter
labelGrayMatter = 2
labelWhiteMatter = 1
 
imgT1Original = SimpleITK.ReadImage(filenameT2)
imgT2Original = SimpleITK.ReadImage(filenameT5)

#---------------平滑处理
#The CurvatureFlowImageFilter class “implements a curvature driven image denoising algorithm”.
#  The math behind this filter are based on a finite-differences algorithm and are quite convoluted.
#  Should you feel like it, you can read more about the algorithm in the class’ docs.
#-------------------------------------------------------------------------

imgSmooth = SimpleITK.CurvatureFlow(image1=imgT1Original,
                                    timeStep=0.125,
                                    numberOfIterations=5) 

#lstSeeds = [(48,149)]
lstSeeds = [(58,178),(85,138),(92,175),(85,141),(111,158)] #种子点
sitk_show(imgSmooth[:,:,idxSlice])
imgWhiteMatter = SimpleITK.ConnectedThreshold(image1=imgT1Original[:,:,idxSlice], 
                                              seedList=lstSeeds, 
                                              lower=0,  # 亮度区间
                                              upper=50,
                                              replaceValue=1)
#sitk_show(SimpleITK.Tile(imgT1Original[:, :, idxSlice],   imgT2Original[:, :, idxSlice],                          (2, 1, 0)))
sitk_show(imgWhiteMatter)
sitk_show(imgT1Original[:,:,idxSlice])

