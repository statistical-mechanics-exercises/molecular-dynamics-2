# Calculating the forces

If we were writing a Monte Carlo code we would only need to calculate the potential as the moves are random .  We are writing an MD code, however, so we need to calculate the forces acting on each of the atoms so we can calculate the trajectory.

Writing a program to calculate the forces on the atoms is thus your task in this next exercise.  You must write a function called `potential` that takes as input an Nx2 matrix that contains the atomic positions.  Your function should then return two quantities:

1. A scalar value for the potential.
2. An Nx2 matrix of forces that are acting on the atoms.

Remember the force is equal to the negative derivative of the potential:

![](https://render.githubusercontent.com/render/math?math=V(\mathbf{x})=\sum_{i=2}^N\sum_{j=1}^{i-1}4\left[\left(\frac{1}{r_{ij}}\right)^{12}-\left(\frac{1}{r_{ij}}\right)^6\right])

 with respect to the atomic positions.  Good luck!
