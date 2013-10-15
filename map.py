class Map(object):
	"""docstring for Map"""
	def __init__(self, nomFichier): 
		super(Map, self).__init__()
		
		self.ligne = 0
		self.collone = 0
		self.nomFichier = nomFichier

	def getMyArrayMap(self):

		f = open(self.nomFichier, 'r')
		for line in f:
			self.ligne = self.ligne+1
			for x in xrange(0,len(line)):
				self.collone = len(line)
		f.close()

		# On recupere dans le fichier Level le niveau puis on construit un tableau a deux dimension
		self.Matrix = [[0 for x in xrange(self.collone)] for x in xrange(self.ligne)]


		h = 0
		f = open(self.nomFichier, 'r')
		for line in f:
			for x in xrange(0,len(line)):
				if line[x] != '\n':
					self.Matrix[h][x] = line[x]
			h = h+1
		f.close()
		
		return self.Matrix
