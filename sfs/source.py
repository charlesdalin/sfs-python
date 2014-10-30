"""Compute the sound field generated by a sound source"""

import numpy as np
from scipy import special


def point(k, x0, x, y, z):
    """Point source"""
    #              1  e^(-j k |x-x0|)
    # G(x-xs,w) = --- ---------------
    #             4pi      |x-x0|
    xx, yy, zz = np.meshgrid(x - x0[0], y - x0[1], z - x0[2], sparse=True)
    r = np.sqrt((xx) ** 2 + (yy) ** 2 + (zz) ** 2)
    return np.squeeze(np.exp(-1j * k * r) / r)


def line(k, x0, x, y, z):
    """Line source parallel to the z-axis"""
    #              j   (2)
    # G(x-xs,w) =  -  H0  ( k |x-x0| )
    #         
    xx, yy, zz = np.meshgrid(x - x0[0], y - x0[1], z, sparse=True)
    r = np.sqrt((xx) ** 2 + (yy) ** 2)
    return np.squeeze(special.hankel2(0, k * r))


def plane(k, n0, x, y, z):
    """Plane wave"""
    # G(x,w) = e^(-i w/c n x)
    xx, yy, zz = np.meshgrid(x, y, z, sparse=True)
    n0 = np.asarray(n0)
    return np.squeeze(np.exp(-1j * k * ( n0[0] * xx + n0[1] * yy + n0[2] * zz))) 
