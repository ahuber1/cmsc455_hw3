import time

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
	x = lowest_x
	startTime = int(round(time.time() * 1000))
	while x <= highest_x:
		y = lowest_y
		while y <= highest_y:
			counter += 1.0 if test(x, y) else 0.0
			y += gridSeparation
			if int(round(time.time() * 1000)) - startTime >= 10000:
				x = highest_x
				counter ==  0
		x += gridSeparation
	print ' ' * 50 + '\r',
	return counter

# Calculates the approximate area using many points and determining
# whether or not they are in the area of interest.
# 'gridSeparation' is the amount of separation between the points
def area(gridSeparation):
	return 1.0 * gridSeparation * gridSeparation * count(gridSeparation)

blockSizes = [0.1, 0.01, 0.001, 0.0001]

print ''
print 'NOTE: There is a timeout of 10 seconds. If the area is not calculated'
print '      within 10 seconds, the computation is skipped.'
print '' 
print 'Block Size   Calculated Area'
print '----------   ---------------'

for size in blockSizes:
	a = area(size)

	sizeStr = ''
	areaStr = ''

	sizeStr = '{0}'.format(size)
	sizeStr = sizeStr.rjust(10, ' ')

	if a > 0:
		areaStr = '{0:.03f}'.format(a).rjust(15, ' ')
	else:
		areaStr = 'Timeout'.rjust(15, ' ')

	print '%s   %s' % (sizeStr, areaStr)

print ''