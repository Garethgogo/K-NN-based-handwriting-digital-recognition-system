import numpy as np
import operator
def ima2vector(filename):
    # create the vector
    vct = np.zeros((1,1024))
    # read the data from the file
    fr = open(filename)
    for i in range(32):
        # read every line
        lineStr = fr.readline()
        for j in range(32):
            # store the frist 32 data into the vct
            vct[0,32*i+j] = int(lineStr[j])
    return vct

def classify(inx,dataSet,iabels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inx,(dataSetSize,1)) - dataSet
    sqdiffMat = diffMat**2
    sqDistance = sqdiffMat.sum(axis=1)
    distances = sqDistance**0.5
    sortedDis = distances.argsort()
    classcount = {}
    for i in range(k):
        thelabel = labels[sortedDis]
        classcount[thelabel] = classcount.get(thelabel,0)+1
    sortedClassCount = sorted(classcount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]









