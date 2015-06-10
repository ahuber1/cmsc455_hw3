# the left half of the equation for circle 1
def circle1(x, y):
	return ((x - 2.0) ** 2.0) + ((y - 2.0) ** 2.0)

# the left half of the equation for circle 2
def circle2(x, y):
	return (x ** 2.0) + ((y - 2.0) ** 2.0)

# the left half of the equation for circle 3
def circle3(x, y):
	return (x ** 2.0) + (y ** 2.0)

# determines whether a point delineated by x and y
# are in circle 1
def insideCircle1(x, y):
	return circle1(x, y) <= 1.0 ** 2.0

# determines whether a point delineated by x and y
# are in circle 2
def insideCircle2(x, y):
	return circle2(x, y) <= 2.0 ** 2.0

# determines whether a point delineated by x and y
# are in circle 3
def insideCircle3(x, y):
	return circle3(x, y) <= 3.0 ** 2.0

# Tests to see whether a point delineated by x and y
# is outside circle 1 and inside circle 2 and 3
def test(x, y):
	return insideCircle1(x, y) == False and insideCircle2(x, y) and insideCircle3(x, y)

# Counts the number of points that are in the area of interest.
# 'gridSeparation' is the amount of separation between the points
def count(gridSeparation):
	lowest_x = -4.0
	highest_x = 4.0
	lowest_y = lowest_x
	highest_y = highest_x
	counter = 0
	numIter = ((highest_x - lowest_x) / gridSeparation) ** 2
	iterCount = 0
	x = lowest_x

	while x <= highest_x:
		y = lowest_y
		while y <= highest_y:
			counter += 1.0 if test(x, y) else 0.0
			y += gridSeparation
			iterCount += 1
			if iterCount % 10000 == 0:
				progress = (iterCount / numIter) * 100
				print 'Progress (grid_size={0}) --> {1:.2f}%\r'.format(gridSeparation, progress),
		x += gridSeparation
	print ' ' * 50 + '\r',
	return counter

# Calculates the approximate area using many points and determining
# whether or not they are in the area of interest.
# 'gridSeparation' is the amount of separation between the points
def area(gridSeparation):
	return 1.0 * gridSeparation * gridSeparation * count(gridSeparation)

blockSizes = [0.1, 0.01, 0.001, 0.0001]

print 'Block Size   Calculated Area'
print '----------   ---------------'

for size in blockSizes:
	a = area(size)

	sizeStr = '{0:.04f}'.format(size)
	areaStr = '{0:.03f}'.format(a)

	sizeStr = sizeStr.rjust(10, ' ')
	areaStr = areaStr.rjust(15, ' ')

	print '%s   %s' % (sizeStr, areaStr)