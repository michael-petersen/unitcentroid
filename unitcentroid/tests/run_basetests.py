"""
this file tests the basic distributions

"""
import numpy as np
import pkg_resources

# bring in the package itself
import unitcentroid

# identify the testing files
d1 = pkg_resources.resource_filename('unitcentroid','data/LMC.evolved.galactocentric.solar.system1_3eb.dat')

# read in the models, which are 6d positions of dark matter particles in the solar neighbourhood
model1 = np.genfromtxt(d1,delimiter=';',skip_header=1)

# now bring in the default measurement
from unitcentroid import unitcentroid

velp = np.arctan2(-model1[:,4],-model1[:,3])
velt = np.arctan(-model1[:,5]/np.sqrt(model1[:,3]**2 + model1[:,4]**2))
tvel = np.sqrt(model1[:,3]**2 + model1[:,4]**2 + model1[:,5]**2.)


rotation_angle = 0.
    
nmax = 5
for i,vthresh in enumerate(np.linspace(400,800,nmax+1)):
    x,y,ex,ey,xyc = unitcentroid.find_median_particle(velp,velt,tvel,vthreshold=vthresh,tolerance=50.,error=True)
    print(vthresh,x,y,ex,ey)
    print((180./np.pi)*rotation_angle)
    plt.scatter(x,y,s=100,marker='X',facecolor='none',edgecolor=cm.viridis(i/nmax,1.))
    #plt.plot([x-ex,x+ex],[y,y],color=cm.viridis(i/nmax,1.),lw=1.)
    make_error_bars(ax,x,y,ex,ey,xyc,color='black')
 


