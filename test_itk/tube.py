import itk
import sys
TubeType = itk.TubeSpatialObject[3]
#TubePointer = TubeType.Pointer
TubePointType = TubeType.TubePointType
PointType = TubeType.PointType
CovariantVectorType = TubePointType.CovariantVectorType
#TubePointer tube = TubeType::New()
tube = TubeType.New()
