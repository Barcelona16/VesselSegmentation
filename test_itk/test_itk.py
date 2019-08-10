import itk
import sys



if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " <inputImage> <outputImage>")
    sys.exit(1)

inputImage = sys.argv[1]
outputImage = sys.argv[2]
PixelType = itk.UC
Dimension = 3

ImageType = itk.Image[PixelType, Dimension]

ReaderType = itk.TubeSpatialObject[3]
Output=itk.Image[PixelType,Dimension]
reader = ReaderType.New()
reader.GetProperty().SetName(inputImage)
output=sys.stdout
outputfile=open("b.txt","a")
sys.stdout=outputfile
reader.PrintSelf()
#itk.SpatialObjectToImageFilter(reader,Output)
image=reader.GetOutput()
print(image)
# RGBPixelType = itk.RGBPixel[PixelType]
# RGBImageType = itk.Image[RGBPixelType, Dimension]

# RGBFilterType = itk.ScalarToRGBColormapImageFilter[ImageType, RGBImageType]
# rgbfilter = RGBFilterType.New()
# rgbfilter.SetInput(reader.GetOutput())
# rgbfilter.SetColormap(RGBFilterType.Hot)

# WriterType = itk.ImageFileWriter[ImageType]
# writer = WriterType.New()
# writer.SetFileName(outputImage)
# writer.SetInput(reader.GetOutput())

# writer.Update()
