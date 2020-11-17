import numpy as np

def potential(x) :
  energy = 0
  forces = np.zeros([7,2])
  # Your code goes here
  
  return energy, forces
  

# This command reads in the positions that are contained in the file called positions.txt
pos = np.loadtxt( "positions.txt" )
# This calculates and prints the energy of the configuration in the input file.  If the 
# code has been implemented correct this energy should be equal to -11.4809
eng, forces = potential( pos )
print( "The energy of the configuration is", eng )
for i in range(7) : print( "Force on atom", i, "is", forces[i] )
