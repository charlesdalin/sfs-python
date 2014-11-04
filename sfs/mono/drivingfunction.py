"""Compute driving functions for various systems."""

import numpy as np
from numpy.core.umath_tests import inner1d  # element-wise inner product


def _wfs_ps(k, x0, n0, xs):
    """Point source by two- or three-dimensional WFS.

    ::

                     (x0-xs) n0
      D(x0,k) = j k ------------- e^(-j k |x0-xs|)
                    |x0-xs|^(3/2)

    """
    x0 = np.asarray(x0)
    n0 = np.asarray(n0)
    xs = np.squeeze(np.asarray(xs))
    ds = x0 - xs
    r = np.linalg.norm(ds, axis=1)
    return 1j * k * inner1d(ds, n0) / r ** (3 / 2) * np.exp(-1j * k * r)


wfs_2d_ps = _wfs_ps


def wfs_25d_ps(k, x0, n0, xs, xref=[0, 0, 0]):
    """Point source by 2.5-dimensional WFS.

    ::

                  ____________   (x0-xs) n0
      D(x0,k) = \|j k |xref-x0| ------------- e^(-j k |x0-xs|)
                                |x0-xs|^(3/2)

    """
    x0 = np.asarray(x0)
    n0 = np.asarray(n0)
    xs = np.squeeze(np.asarray(xs))
    xref = np.squeeze(np.asarray(xref))
    ds = x0 - xs
    r = np.linalg.norm(ds, axis=1)
    return np.sqrt(1j * k * np.linalg.norm(xref - x0)) * inner1d(ds, n0) / \
        r ** (3 / 2) * np.exp(-1j * k * r)


wfs_3d_ps = _wfs_ps


def _wfs_pw(k, x0, n0, n=[0, 1, 0]):
    """Plane wave by two- or three-dimensional WFS.

    Eq.(17) from [Spors et al, 2008]::

      D(x0,k) =  j k n n0  e^(-j k n x0)

    """
    x0 = np.asarray(x0)
    n0 = np.asarray(n0)
    n = np.squeeze(np.asarray(n))
    return 1j * k * np.inner(n, n0) * np.exp(-1j * k * np.inner(n, x0))


wfs_2d_pw = _wfs_pw


def wfs_25d_pw(k, x0, n0, n=[0, 1, 0], xref=[0, 0, 0]):
    """Plane wave by 2.5-dimensional WFS.

    ::

                       ____________
      D_2.5D(x0,w) = \|j k |xref-x0| n n0 e^(-j k n x0)

    """
    x0 = np.asarray(x0)
    n0 = np.asarray(n0)
    n = np.squeeze(np.asarray(n))
    xref = np.squeeze(np.asarray(xref))
    return np.sqrt(1j * k * np.linalg.norm(xref - x0)) * np.inner(n, n0) * \
        np.exp(-1j * k * np.inner(n, x0))


wfs_3d_pw = _wfs_pw


def delay_3d_pw(k, x0, n0, n=[0, 1, 0]):
    """Plane wave by simple delay of secondary sources."""
    x0 = np.asarray(x0)
    n = np.squeeze(np.asarray(n))
    return np.exp(-1j * k * np.inner(n, x0))


def source_selection_pw(n0, n):
    """Secondary source selection for a plane wave.

    Eq.(13) from [Spors et al, 2008]

    """
    n0 = np.asarray(n0)
    n = np.squeeze(np.asarray(n))
    return np.inner(n, n0) >= 0


def source_selection_ps(n0, x0, xs):
    """Secondary source selection for a point source.

    Eq.(15) from [Spors et al, 2008]

    """
    n0 = np.asarray(n0)
    x0 = np.asarray(x0)
    xs = np.squeeze(np.asarray(xs))
    ds = x0 - xs
    return inner1d(ds, n0) >= 0
