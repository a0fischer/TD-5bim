import math, pickle

class Sphere(object):
    """
    Sphere with associated geometrical properties.

    ...

    Attributes
    ----------
    radius : float
        Radius of the sphere.

    Methods
    -------
    __str__()
        String representation of a sphere.
    surface()
        Compute the surface of a sphere.
    volume()
        Compute the volume of a sphere.
    diameter()
        Compute the diameter of a sphere.
    dump(filename)
        Dump the sphere in an output file.
    """

    def __init__(self, radius):
        """Initialisation of a sphere with a given `radius`.
        
        Parameters
        ----------
        radius : float
            Radius of the sphere.
            
        Returns
        -------
        None
        """
        self.radius = radius
        pass

    def __str__(self):
        """String representation of a sphere.
        
        Parameters
        ----------
        None
            
        Returns
        -------
        str
            Description like "Sphere(`radius`)".
        """
        return '%s(%s)' % (self.__class__.__name__, self.radius)

    def surface(self):
        """Surface computation of a sphere.
        
        Parameters
        ----------
        None
            
        Returns
        -------
        float
            Surface of the sphere.
            
        Notes
        -----
        The surface of a sphere is computed using this equation:

        .. math:: 4 * \pi * `radius`^2
        """
        return 4.0 * 3.1416 * self.radius ** 2
        pass

    def volume(self):
        """Volume computation of a sphere.
        
        Parameters
        ----------
        None
            
        Returns
        -------
        float
            Volume of the sphere.
        
        Notes
        -----
        The volume of a sphere is computed using this equation:

        .. math:: \frac{4}{3} * \pi * `radius`^3
        """
        return 4/3 * 3.1416 * self.radius ** 3
        pass

    def diameter(self):
        """Diameter computation of a sphere.
        
        Parameters
        ----------
        None
            
        Returns
        -------
        float
            Diameter of the sphere.
        
        Notes
        -----
        The surface of a sphere is computed using this equation:

        .. math:: 2 * `radius`
        """
        return self.radius ** 2
        pass

    def dump(self, filename):
        """Dumping a sphere in a file with a given `filename`.
        
        Parameters
        ----------
        filename : str
            Filename where the sphere will be dumped.
            
        Returns
        -------
        None
        """
        with open(filename, "w") as f:
            pickle.dump(self, f)
        pass

def loadSphere(filename):
    """ Loading a sphere from a given file.
        
        Parameters
        ----------
        filename : str
            Filename where a sphere is dumped.
            
        Returns
        -------
        Sphere object
            Object of the class Sphere, composed by a radius.
        """
    with open(filename, "r") as f:
        sphere = pickle.load(f)
        return sphere
    pass
