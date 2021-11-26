"""
basic stuff about the surface of spheres

"""
import numpy as np



def sky_hist_2d(x,y,xbins,ybins,weights=None,sky=True):
    """easy 2d histogram for the surface of a sphere (aka the sky)
    
    if sky=True, the returned map is
    normalised by the area of each pixel to correct for geometric effects
    """
    
    
    X,Y = np.meshgrid(xbins,ybins)
    
    if weights is None:
        weights = np.ones(x.size)
           
    dx = np.abs(xbins[1]-xbins[0])
    dy = np.abs(ybins[1]-ybins[0])
    img = np.zeros([xbins.size,ybins.size])
    Nxindx = (np.round((x - np.nanmin(xbins))/(dx))).astype('int')
    Nyindx = (np.round((y - np.nanmin(ybins))/(dy))).astype('int')

    # loop through bins
    for xval in range(0,xbins.size):
        for yval in range(0,ybins.size):
            w = np.where((Nxindx==xval) & (Nyindx==yval))[0]
            if len(w) > 0:
                img[xval,yval] += np.nansum(weights[w])
                
    if sky:
        return X,Y,img.T/np.cos(Y*np.pi/180.)/(dx*dy)
    else:
        return X,Y,img.T/(dx*dy)


def haversine(lon1, lat1, lon2, lat2,deg=True):
    """
    Calculate the great circle distance between two points 
    on a sphere (specified in decimal degrees or radians)
    """
    # convert decimal degrees to radians 
    if deg:
        lon1, lat1, lon2, lat2 = (np.pi/180.)*lon1, (np.pi/180.)*lat1, (np.pi/180.)*lon2, (np.pi/180.)*lat2

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2. * np.arcsin(np.sqrt(a)) 
    if deg:
        return (180./np.pi)*c
    else:
        return c
    

