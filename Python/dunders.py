#!/usr/bin/python3
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.xyz = (self.x**2 + self.y**2 + self.z**2)**(1/2)
    
    def __repr__(self,*args):
        """
        String Representation of object
        """
        return f"{self.__class__.__name__}({vars(self)})"

    def __eq__(self, other):
        """
        Defines how to vectors would be equal.
        """
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __gt__(self, other):
        """
        Greater than comparrison
        """
        return self.xyz > other.xyz
    
    def __lt__(self, other):
        """
        Less than comparrison
        """
        return self.xyz < other.xyz
    
    def __len__(self):
        """
        Acts as .shape()
        """
        return 3

    def __add__(self, other):
        """
        Adding 2 vectors
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        """
        Scalar Product
        """
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def __sub__(self, other):
        """
        Subtracting 2 vectors
        """
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
    
    def __div__(self, other):
        raise NotImplementedError("No such thing as vector division.")

    def angle(self, other):
        """
        The angle between the two vectors
        """
        from math import acos,pi
        return acos(self*other/(self.xyz*other.xyz))*(180/pi)

    def cross(self, other):
        """
        Cross product between 2 vecrors
        """
        i = self.y*other.z - self.z*other.y
        j = self.z*other.x - self.x*other.z
        k =  self.x*other.y - self.y*other.x
        return Vector(i, j, k)


v1 = Vector(x=1,y=1,z=1)
v2 = Vector(x=2, y=-2,  z=6)
v3 = Vector(x=2, y=-2, z=6)

print(max(v1,v2), min(v1,v2), len(v1), sep="\n")
print(f"Is {v2} == {v3}?",v2==v3,sep="\n")
print(f"{v1} + {v2}?",v1+v2,sep="\n")
print(f"Dot product of {v1} * {v2} = {v1 * v2}")
print(f"Cross product of {v1} x {v2} = {v1.cross(v2)}")
print(f"Angle between {v1} x {v2} = {v1.angle(v2)}")