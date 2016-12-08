import knn
from knnResultWrapper import knnResultWrapper
import pickle
from knnResult import knnResult
from resultWriter import resultWriter
from confusionMatrix import ResultsMetric

def testKnn(datasetPath, trainingFileName, testingFileName, best_predictors):
	distMetricDict={}
	distMetricDict[1] = "euclidean"
	distMetricDict[2] = "manhattan"
	distMetricDict[3] = "completelink"

	kLimit = 4

	# kLimit is the # of training records
	kList = [i for i in range(1,kLimit)]
	# print("Accuracy at k= 1 is %f"%(accuracyAtK))

	knnResults = []
	for distMetric in range(1,4):
		print("Dist metric used ",distMetric)
		accuracyTrend=[]
		for i in range(1,kLimit):
			resultMetric = knn.knn(datasetPath, trainingFileName, testingFileName, i, best_predictors, distMetric)
			if i==1:
				datasetPath=None
			accuracyTrend.append(resultMetric.accuracy)
			print("Accuracy at k= %d is %f ."%(i,resultMetric.accuracy))
		knnResultInst = knnResult(kList, accuracyTrend, distMetricDict[distMetric], len(best_predictors))
		#knnResultInst.add([kList, accuracyTrend])
		knnResults.append(knnResultInst)
	results = knnResultWrapper(knnResults)
	with open("resultRedWine"+str(len(best_predictors)),"wb") as f:
		pickle.dump(results, f, -1)	
	knnResultWriter = resultWriter("knn")
	# # for k in knnResultWrapper:
	# # 	print k.extract()
	knnResultWriter.plotCurve(knnResults)