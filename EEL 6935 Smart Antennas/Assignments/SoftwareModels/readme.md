# Modeling of a Linear Antenna Array

physical array properties
structure of properties
    - M : number of elements
    - d : spacing between elements
    - processor : function that processes the incoming signals and produces an output.




arvsig = ArrivingSignal(m,fc,theta)

antarr = AntennaArray(M,d)

antarr.zeroBeamFormer(thetas,e)

processor.run(arvsig,antarr)

processor.plot.ArrayBeamPattern('db','norm')
