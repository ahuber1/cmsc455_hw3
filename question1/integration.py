import math
import numpy as np
import numpy.polynomial.legendre as leg
from gaulegf import gaulegf

def getCoordinates(minimum, maximum, numVals, function):
	step = (maximum - minimum + 0.0) / numVals
	xvals = []
	yvals = []
	x = minimum + 0.0

	while x <= maximum:
		xvals.append(x)
		yvals.append(function(x))
		x = x + step
	return (np.array(xvals), np.array(yvals))

def calculateError(actualArea, observedArea):
	return observedArea - actualArea

def printLine(integrationMethod, numPoints, computedValue, error):
	integrationMethodStr = integrationMethod
	numPointsStr = str(numPoints)
	computedValueStr = '{:.5}'.format(computedValue)
	errorStr = '{:.5}'.format(error)

	integrationMethodStr = integrationMethodStr.rjust(14, ' ')
	numPointsStr = numPointsStr.rjust(14, ' ')
	computedValueStr = computedValueStr.rjust(14, ' ')
	errorStr = errorStr.rjust(14, ' ')
	print '%s   %s   %s   %s' % (integrationMethodStr, numPointsStr, computedValueStr, errorStr)

def gaussLegendre(a, b, n, function):
	x, w = gaulegf(a, b, n)
	area = 0.0
	for i in range(1, n + 1):
		area = area + w[i] * function(x[i])

	return area

actualArea = 1.0 - math.cos(1.0)

x_8, y_8 = getCoordinates(0, 1, 8, math.sin)
x_16, y_16 = getCoordinates(0, 1, 16, math.sin)
x_32, y_32 = getCoordinates(0, 1, 32, math.sin)
x_64, y_64 = getCoordinates(0, 1, 64, math.sin)
x_128, y_128 = getCoordinates(0, 1, 128, math.sin)

trap_16 = np.trapz(y_16, x=x_16)
trap_32 = np.trapz(y_32, x=x_32)
trap_64 = np.trapz(y_64, x=x_64)
trap_128 = np.trapz(y_128, x=x_128)

gauss_8 = gaussLegendre(0, 1, 8, math.sin)
gauss_16 = gaussLegendre(0, 1, 16, math.sin)

print 'Exact Solution: %.2f' % actualArea
print ''
print 'Integr. Method   Num. of Points   Computed Value            Error'
print '--------------   --------------   --------------   --------------'
printLine('Trapezoidal', 16, trap_16, calculateError(actualArea, trap_16))
printLine('Trapezoidal', 32, trap_32, calculateError(actualArea, trap_32))
printLine('Trapezoidal', 64, trap_64, calculateError(actualArea, trap_64))
printLine('Trapezoidal', 128, trap_128, calculateError(actualArea, trap_128))
printLine('Gauss-Legendre', 8, gauss_8, calculateError(actualArea, gauss_8))
printLine('Gauss-Legendre', 16, gauss_16, calculateError(actualArea, gauss_16))