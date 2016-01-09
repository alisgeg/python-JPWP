import urllib2
import os
import imagereader
import sys

def compare(givenImageName):
	print "reading %s..." % (givenImageName)
	givenImage = imagereader.read(givenImageName)
	from scipy.misc import imresize
	import numpy as np
	print "%sx%sx%s" % (len(givenImage), len(givenImage[0]), len(givenImage[0][0]))
	f = open('countryNames.txt', 'r')
	listOfCountries = []
	listOfDiff = []

	for el in os.listdir("./flags"):

		tmpFileName = el
		listOfCountries.append(el)
		currentImage = imagereader.read('./flags/' + tmpFileName)
		# currentImage = open('./flags/' + tmpFileName, 'r')
		# currentImage = mpimg.imread(currentImage)

		x = currentImage.shape[0]
		y = currentImage.shape[1]
		
		givenImage = imresize(givenImage, (x, y), interp='bilinear')

		givenImageInt32 = np.empty(currentImage.shape, dtype=np.int32)
		np.copyto(givenImageInt32, givenImage, casting='unsafe')

		currentImageInt32 = np.empty(currentImage.shape, dtype=np.int32)
		np.copyto(currentImageInt32, currentImage, casting='unsafe')

		diff = calculateColorDiff(givenImageInt32, currentImageInt32)

		listOfDiff.append(diff)

	maxDiff = float(max(listOfDiff))
	minDiff = float(min(listOfDiff))

	for i in range(len(listOfDiff)):
		listOfDiff[i] = (float(listOfDiff[i])-minDiff)/(maxDiff-minDiff)

	index = listOfDiff.index(min(listOfDiff))
	

	print listOfCountries[index]
	# listOfCountries[index] = listOfCountries[index][:listOfCountries[index].index(".")-1]
	return listOfCountries[index]


def calculateColorDiff(image1, image2):
	import numpy as np
	diff1 = sum(sum(np.sqrt(abs(image1[:,:,0]-image2[:,:,0]))))
	diff2 = sum(sum(np.sqrt(abs(image1[:,:,1]-image2[:,:,1]))))
	diff3 = sum(sum(np.sqrt(abs(image1[:,:,2]-image2[:,:,2]))))
	diff = diff1 + diff2 + diff3
	return diff

if __name__ == '__main__':
	compare('test.png')