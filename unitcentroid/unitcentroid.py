"""
this file tests the basic distributions

"""
import numpy as np

from . import spheres

def find_median_particle(velp,velt,tvel,vthreshold=600,tolerance=50.,error=False):
    """
    find the particle from a distribution that has the smallest median separation to all other particles:
    i.e. the central particle
    
    
    
    """
    
    # subselect particles that are above the velocity threshold
    use    = tvel>vthreshold
    vphi   = velp[use]
    vtheta = velt[use]
    
    #print(vphi.size)
    
    # set up the array of separations, filled with maximum separations
    meandist = np.zeros(vphi.size) + np.pi
    
    for p in range(0,vphi.size):

        # compute the separations to all particles
        separations = spheres.haversine(vphi[p],vtheta[p],vphi,vtheta,deg=False)
        
        # compute the desired separation value (in fractions of the total number of particles)
        meandist[p] = np.nanpercentile(separations,tolerance)
        
    # one option is to randomly drop some fraction of the particles and see how much the centroid changes
    # a monte-carlo style error estimation
    if error:
        # how many samples?
        prefac = 1
        bootstrapsqrt = prefac*int(np.sqrt(meandist.size))
        centre1,centre2 = np.zeros(bootstrapsqrt),np.zeros(bootstrapsqrt)
        for n in range(0,bootstrapsqrt):
            nselect = np.random.randint(0,meandist.size,bootstrapsqrt)
            #print(meandist[nselect])
            w = np.nanargmin(meandist[nselect])
            centre1[n],centre2[n] = vphi[nselect[w]],vtheta[nselect[w]]            

    # this is the radius of the circle that encompasses the desired fraction of particles
    #print(180.*np.nanmin(meandist)/np.pi)
    # this could be used as a measure of the uncertainty? (or some fraction of this)
    
    # which particle is the centroid particle?
    w = np.nanargmin(meandist)
    
    # print the centroid
    #print(velp[w],velt[w])
    cov = (prefac)*np.cov([centre1,centre2])
    #print(cov)
    xerr,yerr = np.sqrt(cov[0][0]),np.sqrt(cov[1][1])
    corr = cov[0][1]/(xerr*yerr)
    #print('correlation:',corr)
    
    # to get a 95% confidence ellipse, multiply xerr and yerr by 2.4477 (chi^2 distribution prefactor)
    
    
    # return the centroid
    if error:
        return vphi[w],vtheta[w],xerr,yerr,corr
    else:
        return vphi[w],vtheta[w]

def make_error_bars(ax,x,y,ex,ey,xyc,color='black'):
    rotation_angle = 0.5*np.arctan(2*xyc*ex*ey/(ex**2 + ey**2))
    # first the 'x' error bars
    x1,x2,y1,y2 = -ex,ex,0,0
    x1p,y1p = np.dot([x1,y1],[[np.cos(rotation_angle),-np.sin(rotation_angle)],\
                              [np.sin(rotation_angle), np.cos(rotation_angle)]])
    x2p,y2p = np.dot([x2,y2],[[np.cos(rotation_angle),-np.sin(rotation_angle)],\
                              [np.sin(rotation_angle), np.cos(rotation_angle)]])    
    ax.plot([x+x1p,x+x2p],[y+y1p,y+y2p],color=color,lw=1.)
    
    # now the 'y' error bars
    x1,x2,y1,y2 = 0,0,-ey,ey
    #rotation_angle *= 0.5 # spherical convention
    x1p,y1p = np.dot([x1,y1],[[np.cos(rotation_angle),-np.sin(rotation_angle)],\
                              [np.sin(rotation_angle), np.cos(rotation_angle)]])
    x2p,y2p = np.dot([x2,y2],[[np.cos(rotation_angle),-np.sin(rotation_angle)],\
                              [np.sin(rotation_angle), np.cos(rotation_angle)]])    
    ax.plot([x+x1p,x+x2p],[y+y1p,y+y2p],color=color,lw=1.)




