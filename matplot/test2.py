import matplotlib.pyplot as mat
import numpy

ypoints = numpy.array([1, 2, 1, 3, 0, 1, 2])
ypoints2 = numpy.array([0,1,0,2,0])

mat.title("i am a title",fontdict={"family":"serif","color":"#00FF00","size":30})
mat.ylabel("i am a Y label")
mat.xlabel("i am a X label")

mat.grid(axis="y", linestyle="--")

mat.subplot(2,1,1)
mat.plot(ypoints, "o:r")

mat.subplot(2,1,2)
mat.plot(ypoints2, c="#00ff00", linewidth=5, alpha=0.5)

mat.show()
