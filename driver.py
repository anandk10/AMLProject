import knn
import sys

def usage():
	print("Wrong usage.")

(datasetPath, trainingFileName, testingFileName, algo) = (sys.argv[1:5])

if algo=="knn":
	k = int(sys.argv[5])
	best_predictors=[]
	for i in range(5,len(sys.argv)):
		best_predictors.append(int(sys.argv[i]))
	print("The best predictors chosen : ",best_predictors)
	print("datasetPath",datasetPath)
	print("trainFile:",trainingFileName)
	print("testingFile:",testingFileName)

	print("k set to ",k)
	knn.knn(datasetPath, trainingFileName, testingFileName, k, best_predictors)

elif algo=="lr":
	usage()
else:
	usage()
	sys.exit(1)






# (datasetPath, trainingFileName, testingFileName,k) = (sys.argv[1:5])

'''
If the user inputs no best predictors then, all the columns would be chosen for
running the algorithm

'''

