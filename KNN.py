import numpy as np
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


testvector = ima2vector('digits/testDigits/0_1.txt')
print(testvector[0,0:31])





