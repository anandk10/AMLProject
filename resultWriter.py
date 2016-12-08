import os
import matplotlib.pyplot as plt
import random
class resultWriter:

	def __init__(self, algo):
		self.path=os.path.dirname(os.path.realpath(__file__))+"/"+algo

	def plotCurve(self, modelResultList):
		distMetricDict={}
		distMetricDict[1] = "euclidean"
		distMetricDict[2] = "manhattan"
		distMetricDict[3] = "complete-link"
		# modelResultList - 4 parts: xplotList, yplotList, information (used to save file by that name)
		# 					information is obtained from distanceMetric and best predicate count
		i=0
		fileName=""
		color=['red','blue','green','black']
		for modelResult in modelResultList:
			xplotlist, yplotlist, info = modelResult.extract()
			
			fileName+=info+"-"
			print "Xplot: ",xplotlist
			print "YPlot: ",yplotlist
			c = color[i]
			print(c)
			plt.plot(xplotlist, yplotlist, color=c, linewidth=1.5**2, linestyle="--",label=info.split("-")[0])
			i+=1
		plt.legend(loc="upper right")
		plt.savefig(self.path+"-"+fileName+".png")
		'''
		The extract() gives the information to be put up on the graph.
		Using this information plot the curves.
		'''
	def __str__(self):
		return ""+self.path