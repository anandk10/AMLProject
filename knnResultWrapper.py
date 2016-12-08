class knnResultWrapper():
	def __init__(self, modelResultList):
		self.modelResultList = modelResultList
	def get(self):
		return self.modelResultList