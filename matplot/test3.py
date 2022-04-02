from matplotlib.pyplot import *

subplot(4, 1, 1)
bar([1, 2, 3, 4, 5, 6], [1, 2, 4, 2, 3, 1])
margins(0.1)

subplot(4, 1, 2)
barh([1,2,3], [2, 1, 3])
margins(0.1)

subplot(4, 1, 3)
bar([0, 1, 2, 3], [1, 3, 2, 1], color="#0000FF", width=0.5)
plot([1, 3, 2, 1], "o:b")
margins(0.1)

subplot(4, 1, 4)
plot([1, 1, 2, 1, 3, 4, 5, 1, 3, 2])
margins(0.1)
show()
