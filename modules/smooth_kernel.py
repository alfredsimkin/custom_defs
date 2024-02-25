
def smooth(a, b, first_label, second_label, lims=False):
	'''
	A function from Nick Stepankiw to generate smooth scatter plots
	'''
	import matplotlib as mpl
	mpl.use('Agg') #comment this in if using a nongraphical interface, comment out to enable graphical interface
	import matplotlib.pyplot as plt
	import scipy
	import scipy.stats as stats
	import numpy as np
	x = np.array(a) # a is your x-coordinates
	y = np.array(b) # b is your y-coordinates
	if lims!=False:
		xmin, xmax=lims[0]
		ymin, ymax=lims[1]
#		plt.xlim(lims[0])
#		plt.ylim(lims[1])
	else:
		xmin = x.min()
		xmax = x.max()
		ymin = y.min()
		ymax = y.max()
	#normally distributed data
#	a = scipy.randn(5000)
#	b = 2*scipy.randn(5000)

	# begin plot
	#data = hexbin(x,y,mincnt=1, bins='log', gridsize = 200) # this was an attempt to find the approximate number of occurances in a bin

	#generate smoothed kernel
	steps = 200j #steps is a complex number that determines the number of gradations of the mgrid. bigger means more gradations which takes longer. 100j is probably fine
#	steps=5
	X, Y = np.mgrid[xmin:xmax:steps, ymin:ymax:steps]
	positions = np.vstack([X.ravel(), Y.ravel()])
	values = np.vstack([x, y])
	kernel = stats.gaussian_kde(values) #actual smoothing function
	Z = np.reshape(kernel(positions).T, X.shape)

	#plot this smoothed kernel
	fig = plt.figure()
	ax = fig.add_subplot(111)
	cax = ax.imshow(np.rot90(Z), cmap=plt.cm.gist_earth_r ,extent=[xmin, xmax, ymin, ymax], aspect = 'auto')

	#cbar = fig.colorbar(cax, ticks=[min(min(x),min(y)), 0.5*( min(min(x),min(y)) + max(max(x),max(y)) ) , max(max(x),max(y))], orientation='vertical')
	cbar = fig.colorbar(cax, orientation='vertical')
	#plt.colorbar(img, cax = plt_bar)

	#useful stuff
#	else:
#		plt.xlim([xmin, xmax])
#		plt.ylim([ymin, ymax])
		#ax.set_ylim([ymin, ymax])
	plt.title(first_label+'_vs_'+second_label)
	plt.xlabel(first_label)
	plt.ylabel(second_label)
	plt.tight_layout()
	plt.savefig(first_label+'_vs_'+second_label+'.png', bbox_inches='tight')
