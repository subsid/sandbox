import matplotlib as mpl
import numpy as np
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

fmeasures = list(map(lambda x: x * 100, [
        0.6579,
        0.6494,
        0.6410,
        0.6329,
        0.6250,
        0.6173,
        0.6098,
        0.6024,
        0.5952 ]))

negativeExamples =  [
2000,
4000,
6000,
8000,
10000,
12000,
14000,
16000,
18000]

accuracies =  list(map(lambda x: x * 100, [ 0.8267,
    0.8920,
    0.9200,
    0.9356,
    0.9455,
    0.9523,
    0.9573,
    0.9612,
    0.9642 ]))

plt.title('Effect of negative examples on F-measure and Accuracy')
p1 = plt.plot(negativeExamples, fmeasures, label = 'F-Measure')
p2 = plt.plot(negativeExamples, accuracies, label = 'Accuracy')
plt.legend(['F-Measure', 'Accuracy'])
plt.axis([0, 20000, 50, 100])
plt.ylabel('Percentage %')
plt.xlabel('Number of non-circle shapes')
plt.show()
