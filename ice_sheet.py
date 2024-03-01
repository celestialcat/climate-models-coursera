import numpy as np
import matplotlib.pyplot as plt

def IceSheet(
	n_year,                  # years
	n_x=10,                  # number of grid points
	x_width=1E6,             # metres
	t_step=100,              # years
	flow_param=1E4,          # metres/year
	snow_fall=0.5            # metres/year
):
	
	# =======================================
	# set plotting features and define arrays
	# =======================================
	
	# initialise elevation and flow arrays
	elev = np.zeros(n_x+2)
	flow = np.zeros(n_x+1)
	
	# define elevation plotting properties
	fig, ax = plt.subplots()
	ax.plot(elev)
	plt.show(block=False)
	
	# =============================
	# time loop for ice-sheet model
	# =============================
	
	# calculate elevation and flow over years
	dx = x_width/n_x
	results = {}
	for year in np.arange(0, int(n_year/t_step)):
		for x in np.arange(0, n_x+1):
			flow[x] = (elev[x]-elev[x+1])/dx * flow_param * (elev[x]+elev[x+1])/2/dx
		for x in np.arange(1, n_x+1):
			elev[x] = elev[x] + (snow_fall+flow[x-1]-flow[x]) * t_step
			results[f'{year}'] = elev[5]
			print(year, elev[5])
			ax.clear()
			ax.plot(elev)
			plt.show(block=False)
			plt.pause(0.001)
			fig.canvas.draw()
	
	return results

if __name__ = '__main__':

	#years = float(input(''))
	model = IceSheet(20000)
