import numpy as np
import operator
import sys
import os

def createDataSet(foldername):
	fileList = os.listdir(foldername)
	returnMat = []
	classLabelVector = []
	for filename in fileList:
		classLabelVector.append(filename.split('_')[0])
		filepath = foldername + '/' + filename
		fp = open(filepath)
		for line in fp:
			line = fp.readlines()
			line = [l[:-1] for l in line]
			line = ''.join(line)
			line = [float(l) for l in line]
			returnMat.append(line)
	returnMat = np.array(returnMat)
	return returnMat, classLabelVector

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

def calcErrorRate(trainingDataSet, trainingDataLabel, testDataSet, testDataLabel, k):
	errorCnt = 0
	for i in range(len(testDataSet)):
		result = classify0(testDataSet[i], trainingDataSet, trainingDataLabel, k)
		if result != testDataLabel[i]:
			errorCnt += 1
	print(int(errorCnt/len(testDataSet)*100))

command = sys.argv
trainingDataFolder = command[1]
testDataFolder = command[2]
trainingDataSet, trainingDataLabel = createDataSet(trainingDataFolder)
testDataSet, testDataLabel = createDataSet(testDataFolder)
for k in range(1, 21):
	calcErrorRate(trainingDataSet, trainingDataLabel, testDataSet, testDataLabel, k)
