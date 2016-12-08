class knnResult:
	def __init__(self, klist, accuracyTrend, distanceMetric, bestPredictorsCount):
		self.klist = klist
		self.accuracyTrend = accuracyTrend
		self.distanceMetric = distanceMetric
		self.bestPredictorsCount = bestPredictorsCount
		self.info = self.distanceMetric+"-"+str(bestPredictorsCount)

	def add(self, klistAccuracy):
		# klist, accuracyTrend
		self.klist = klistAccuracy[0]
		self.accuracyTrend = klistAccuracy[1]

	def extract(self):
		return self.klist, self.accuracyTrend, self.info