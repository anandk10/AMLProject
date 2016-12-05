import csv
def readData(filepath, best_predictors, data=[]):
	with open(filepath,'r') as f:
		datalist = list(csv.reader(f))
		
		column_len = len(datalist[0])
		for i in range(len(datalist)):
			#print(i)
			if i!=0:
				relevantDataList = []
				# the read data may be read in string format;
				# thus converting it into float type
				#print(datalist[i])
				# print("Col len ",column_len)
				for j in range(column_len-1):
					# print("Best pred ",best_predictors)
					# input()
					# print("j-val " ,j)
					if not best_predictors or j in best_predictors:
						# print(j)
						# input()
						# print("Selected ",datalist[i][j])
						relevantDataList.append(round(float(datalist[i][j]),4))
						# datalist[i][j] = round(float(datalist[i][j]),4)
				# print("Class: ",datalist[i][column_len-1])
				relevantDataList.append(int(float(datalist[i][column_len-1])))
				# if relevantDataList[-1] != 0:
					# print("List: ",relevantDataList)
					# input()
				# input("Press any key")
				# print("List: ",relevantDataList)
				#datalist[i][column_len-1] = int(float(datalist[i][column_len-1]))
				# now append this converted row into the data[]
				# data.append(datalist[i])
				data.append(relevantDataList)