# unitcentroid

### A python package for computing the centroid from a collection of points on the surface of a unit sphere.

-------

Install by running `python setup.py install` in the unitcentroid directory once unpacked.

-------

#### The theory.

Some example data ships with the package, drawn from simulations presented in Donaldson et al. (2022).

In an experiment that is sensitive to the direction of particles, we are given a set of observations that triggered a detector. These observations may be selected in any fashion; typically one assumes that only particles above some energy threshold (equivalently,
<img src="https://render.githubusercontent.com/render/math?math=v_%7B%5Crm%7Bmin%7D%7D">) will trigger a detector.

Given a sample of
<img src="https://render.githubusercontent.com/render/math?math=n"> observations distributed with angles
<img src="https://render.githubusercontent.com/render/math?math=(%5Cphi%2C%5Ctheta)">
on the sky, we compute the set of angular separations between each individual observation
<img src="https://render.githubusercontent.com/render/math?math=i"> and all other particles,
<img src="https://render.githubusercontent.com/render/math?math=%5CXi_i%20%3D%20%5C%7B%5Cxi_1%2C%5Cdots%2C%5Cxi_j%2C%5Cdots%2C%5Cxi_n%5C%7D">
for
<img src="https://render.githubusercontent.com/render/math?math=j%20%5Cin%5B1%2Cn%5D%2Cj%5Cne%20i">, where
<img src="https://render.githubusercontent.com/render/math?math=%5Cxi_j">
is the angular separation between the
<img src="https://render.githubusercontent.com/render/math?math=j%5E%7B%5Crm%7Bth%7D%7D">
observation and the
<img src="https://render.githubusercontent.com/render/math?math=i%5E%7B%5Crm%7Bth%7D%7D">
observation. For each set
<img src="https://render.githubusercontent.com/render/math?math=%5CXi_j">, we compute the
<img src="https://render.githubusercontent.com/render/math?math=p%5E%7B%5Crm%7Bth%7D%7D">
percentile value, which we denote
<img src="https://render.githubusercontent.com/render/math?math=%5CXi_j%7C_%7Bp%7D">. In our case, we choose <img src="https://render.githubusercontent.com/render/math?math=p%3D50">, which is the median. Smaller values of
<img src="https://render.githubusercontent.com/render/math?math=p">
with emphasise contributions from higher-density regions, lower values of
<img src="https://render.githubusercontent.com/render/math?math=p"> will emphasise lower-density regions. The observation with the minimum
<img src="https://render.githubusercontent.com/render/math?math=%5CXi_j%7C_%7Bp%7D">
is defined as the centroid observation.

One advantage of this procedure is that it is well-defined for relatively small numbers of observations. In fact, given the relatively expensive nature of this computation, the procedure is best performed on relatively small numbers of observations. However, small numbers of observations may be subject to Poisson noise, necessitating an uncertainty estimate.

To estimate the uncertainty, we partition the
<img src="https://render.githubusercontent.com/render/math?math=n">
observations into
<img src="https://render.githubusercontent.com/render/math?math=%5Csqrt%7Bn%7D"> subgroups of
<img src="https://render.githubusercontent.com/render/math?math=%5Csqrt%7Bn%7D"> observations and repeat the angular separation procedure for each subgroup. Then, with
<img src="https://render.githubusercontent.com/render/math?math=%5Csqrt%7Bn%7D"> centroid observations distributed as
<img src="https://render.githubusercontent.com/render/math?math=%5C%7B(%5Cphi%2C%5Ctheta)%5C%7D_%7B%5Csqrt%7Bn%7D%7D">, we construct an uncertainty ellipse on the sky by measuring the
<img src="https://render.githubusercontent.com/render/math?math=2%5Ctimes2">
 covariance matrix
<img src="https://render.githubusercontent.com/render/math?math=C">. We define two principal uncertainty axes <img src="https://render.githubusercontent.com/render/math?math=%5Csigma_%7B%5Cphi%7D%3D2.44%5Csqrt%7BC_%7B00%7D%7D">
and
<img src="https://render.githubusercontent.com/render/math?math=%5Csigma_%7B%5Ctheta%7D%3D2.44%5Csqrt%7BC_%7B11%7D%7D">. We include a scaling of 2.44 to estimate the 95% confidence interval, assuming a
<img src="https://render.githubusercontent.com/render/math?math=%5Cchi%5E2"> distribution. The rotation of the uncertainty axes is given by
<img src="https://render.githubusercontent.com/render/math?math=%5Czeta%3D%5Carctan%5Cleft(%5Cfrac%7B2C_%7B01%7D%7D%7B(C_%7B00%7D%2BC_%7B11%7D%7D%5Cright)">, which we use to rotate and plot the uncertainties.  The correlation coefficient is then
<img src="https://render.githubusercontent.com/render/math?math=c_%7B%5Cphi%5Ctheta%7D%3DC_%7B01%7D%2F(%5Csigma_%7B%5Cphi%7D%5Csigma_%7B%5Ctheta%7D)">. 

In practice, we find that our uncertainty estimates are converged for <img src="https://render.githubusercontent.com/render/math?math=n%3E100"> observations, but the uncertainty ellipsoid shape and orientation is dependent on the structure of the underlying distribution of observations. This suggests that further refinement of the algorithm may allow for improved characterisation of the on-sky distributions.


#### Extensions.

The technique above can be improved in several ways.
1. Computational clean-up. We are currently approaching the median computation by brute force, which will be difficult for large numbers of particles.
2. Can we extend this analysis to use observational errors? In the case where the direction of particles has some uncertainty ellipse in sky coordinates, one can Monte Carlo resample the error ellipses between points (at high computational cost...).
2. What about censored measurements that are only sensitive to part of the sky?
3. We have not attempted any energy-weighting, but one could in principle measure the energy-weighted centroid if one believed that multiple populations were present. For example, in the case of the MW and LMC, given that the LMC particles dominate the highest velocities, an energy-weighted centroid would give preference to LMC particles.



### License
-------

This project is Copyright (c) Michael Petersen and licensed under the terms of the two-clause BSD license. See the ``licenses`` folder for more information.
