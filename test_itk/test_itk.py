import itk
import sys



if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " <inputImage> <outputImage>")
    sys.exit(1)

inputImage = sys.argv[1]
outputImage = sys.argv[2]
PixelType = itk.UC
Dimension = 3

#ImageType = itk.Image[PixelType, Dimension]

ReaderType = itk.SpatialObjectReader[3]
#Output=itk.Image[PixelType,Dimension]
reader = ReaderType.New()
reader.SetFileName(inputImage)
reader.Update()
group = reader.GetGroup()
print(group.GetNumberOfChildren())
# reader.GetProperty().SetName(inputImage)
# output=sys.stdout
# outputfile=open("b.txt","a")
# sys.stdout=outputfile
#reader.PrintSelf()
#print(itk.SpatialObjectToImageFilter.GetTypes(reader))
#image=reader.GetOutput()
tube = group.GetObjectById(2)
print(tube)


# writer.Update()
