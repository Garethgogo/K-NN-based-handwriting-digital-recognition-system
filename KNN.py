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
    # get the size
    dataSetSize = dataSet.shape[0]
    # Matrix operation, calculating the difference between the test data and the corresponding data item for each sample data
    diffMat = np.tile(inx,(dataSetSize,1)) - dataSet
    # compute the sum of the square
    sqdiffMat = diffMat**2
    sqDistance = sqdiffMat.sum(axis=1)
    # get the distance vector
    distances = sqDistance**0.5
    # sorted by distance
    sortedDis = distances.argsort()
    classcount = {}
    for i in range(k):
        # get the label
        thelabel = labels[sortedDis]
        # strore the times every label appear
        classcount[thelabel] = classcount.get(thelabel,0)+1
        # sorted by frequency of occurence
    sortedClassCount = sorted(classcount.items(), key=operator.itemgetter(1), reverse=True)
    # return the label of highest frequency
    return sortedClassCount[0][0]









