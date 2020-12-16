import numpy as np

def potential(x) :
  energy = 0
  forces = np.zeros([7,2])
  # Your code goes here
  for i in range(1,7) :
      for j in range(i) :
          d = x[i,:]-x[j,:]
          r2 = sum(d*d)
          r6 = r2*r2*r2 
          r12 = r6*r6 
          energy = energy + 4/r12 - 4/r6
          pref = 4*( 6/(r6*r2) - 12/(r12*r2) )
          forces[i,:] =  forces[i,:] - pref*d
          forces[j,:] =  forces[j,:] + pref*d
  return energy, forces
  

# This command reads in the positions that are contained in the file called positions.txt
pos = np.loadtxt( "positions.txt" )
# This calculates and prints the energy of the configuration in the input file.  If the 
# code has been implemented correct this energy should be equal to -11.4809
eng, forces = potential( pos )
print( "The energy of the configuration is", eng )
for i in range(7) : print( "Force on atom", i, "is", forces[i] )
