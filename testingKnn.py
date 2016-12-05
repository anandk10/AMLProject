import knn
def testKnn(datasetPath, trainingFileName, testingFileName, best_predictors):
	kLimit = 2
	# first run it for k=1
	kLimit,accuracyAtK = knn.knn(datasetPath, trainingFileName, testingFileName, 1, best_predictors)
	accuracyTrend=[]
	accuracyTrend.append(accuracyAtK)
	# kLimit is the # of training records
	print("Accuracy at k= 1 is %f"%(accuracyAtK))
	for i in range(2,kLimit):
		size,accuracyAtK = knn.knn(None, trainingFileName, testingFileName, i, best_predictors)
		accuracyTrend.append(accuracyAtK)
		print("Accuracy at k= %d is %f"%(i,accuracyAtK))
	kList = [i for i in range(kLimit)]
	return kList, accuracyTrend