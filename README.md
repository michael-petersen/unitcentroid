# unitcentroid

### A python package for computing the centroid from a collection of points on the surface of a unit sphere.

-------

Install by running `python setup.py install` in the unitcentroid directory once unpacked.

-------

#### The theory.

Some example data ships with the package, drawn from simulations presented in Donaldson et al. (2022).

In an experiment that is sensitive to the direction of particles, we are given a set of observations that triggered a detector. These observations may be selected in any fashion; typically one assumes that only particles above some energy threshold (equivalently, $v_{\rm min}$) will trigger a detector.

Given a sample of $n$ observations distributed with angles $(\phi,\theta)$ on the sky, we compute the set of angular separations between each individual observation $i$ and all other particles, $\Xi_i = \{\xi_1,\dots,\xi_j,\dots,\xi_n\}$ for $j \in[1,n],j\ne i$, where $\xi_j$ is the angular separation between the $j^{\rm th}$ observation and the $i^{\rm th}$ observation. For each set $\Xi_j$, we compute the $p^{\rm th}$ percentile value, which we denote $\Xi_j|_{p}$. In our case, we choose $p=50$, which is the median. Smaller values of $p$ with emphasise contributions from higher-density regions, lower values of $p$ will emphasise lower-density regions. The observation with the minimum $\Xi_j|_{p}$ is defined as the centroid observation.

One advantage of this procedure is that it is well-defined for relatively small numbers of observations. In fact, given the relatively expensive nature of this computation, the procedure is best performed on relatively small numbers of observations. However, small numbers of observations may be subject to Poisson noise, necessitating an uncertainty estimate.

To estimate the uncertainty, we partition the $n$ observations into $\sqrt{n}$ subgroups of $\sqrt{n}$ observations and repeat the angular separation procedure for each subgroup. Then, with $\sqrt{n}$ centroid observations distributed as $\{(\phi,\theta)\}_{\sqrt{n}}$, we construct an uncertainty ellipse on the sky by measuring the $2\times2$ covariance matrix $C$. We define two principal uncertainty axes $\sigma_{\phi}=2.44\sqrt{C_{00}}$ and $\sigma_{\theta}=2.44\sqrt{C_{11}}$. We include a scaling of 2.44 to estimate the 95\% confidence interval, assuming a $\chi^2$ distribution. The rotation of the uncertainty axes is given by $\zeta=\arctan\left(\frac{2C_{01}}{(C_{00}+C_{11}}\right)$, which we use to rotate and plot the uncertainties.  The correlation coefficient is then $c_{\phi\theta}=C_{01}/(\sigma_{\phi}\sigma_{\theta})$. 

In practice, we find that our uncertainty estimates are converged for $n>100$ observations, but the uncertainty ellipsoid shape and orientation is dependent on the structure of the underlying distribution of observations. This suggests that further refinement of the algorithm may allow for improved characterisation of the on-sky distributions.

-------

#### Extensions.

The technique above can be improved in several ways.
1. Computational clean-up. We are currently approaching the median computation by brute force, which will be difficult for large numbers of particles.
2. Can we extend this analysis to use observational errors? In the case where the direction of particles has some uncertainty ellipse in sky coordinates, one can Monte Carlo resample the error ellipses between points (at high computational cost...).
2. What about censored measurements that are only sensitive to part of the sky?
3. We have not attempted any energy-weighting, but one could in principle measure the energy-weighted centroid if one believed that multiple populations were present. For example, in the case of the MW and LMC, given that the LMC particles dominate the highest velocities, an energy-weighted centroid would give preference to LMC particles.



### License
-------

This project is Copyright (c) Michael Petersen and licensed under the terms of the two-clause BSD license. See the ``licenses`` folder for more information.
