import argparse
import numpy as np
import matplotlib.pyplot as plt

def ArgumentSetup():

  # plotting option
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-p', '--plot', 
    action='store',
    choices=[
      'temperature', 
      'heat_content', 
      'heat_flux',
    ],
    type=str,
    required=False,
    help='plot one of following: %(choices)'
  )

  return parser.parse_args()

def PlanetModel(nSteps):
    
  # define parameters
  timeStep = 100
  waterDepth = 4000  # meters
  solarConstant = 1350  # W/m^2
  albedo = 0.3
  epsilon = 1
  sigma = 5.67E-8  # W/m^2 K^4
  heatCapacity = waterDepth * 4200000  # J/K m^2
  
  # initialise variables
  time = [0]
  temperature = [0]
  heatContent = [(heatCapacity * temperature[0])]
  heatIn = solarConstant * ((1 - albedo) / 4)
  heatOut = [0]
  
  # create model
  for step in np.arange(0, nSteps):
    print(temperature[-1], heatOut[-1])
    _heatOut = epsilon * sigma * temperature[-1]**4
    _heatContent = heatContent[-1] + ((heatIn - _heatOut) * timeStep * 31536000)
    _temperature = _heatContent / heatCapacity
    _time = time[-1] + timeStep    
    time.append(_time)
    temperature.append(_temperature)
    heatContent.append(_heatContent)
    heatOut.append(_heatOut)
    
  return time, temperature, heatContent, heatOut
  
if __name__ == '__main__':

  args = ArgumentSetup()
  if args.plot == 'temperature':
    nSteps = int(input(''))
    outputs = PlanetModel(nSteps)
    plt.plot(outputs[0], outputs[1])
    plt.xlabel('Time (years)')
    plt.ylabel('Temperature (K)')
    plt.show()
  elif args.plot == 'heat_content':
    nSteps = int(input(''))
    outputs = PlanetModel(nSteps)
    plt.plot(outputs[0], outputs[2])
    plt.xlabel('Time (years)')
    plt.ylabel('Heat content (J/m^2)')
    plt.show()
  elif args.plot == 'heat_flux':
    nSteps = int(input(''))
    outputs = PlanetModel(nSteps)
    plt.plot(outputs[0], outputs[3])
    plt.xlabel('Time (years)')
    plt.ylabel('Heat flux (W/m^2)')
    plt.show()
  elif args.plot == None:
    nSteps = int(input(''))
    outputs = PlanetModel(nSteps)
  
