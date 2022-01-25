""" 
Name: Kenny Tran 025496300
Date: 3/3/21
Lab 4
"""
class Vector:
        def __init__(self, l):
                self.v = l
                self.size = len(l)

        def get_ith_element(self, i):
                return self.v[i]

        def __add__(self, other):
                if self.size != other.size:
                        return None
                sum = []
                for i in range(self.size):
                        sum.append(self.get_ith_element(i) + other.get_ith_element(i))
                return Vector(sum)

        def __sub__(self, other):
                if self.size != other.size:
                        return None
                sub = []
                for i in range(self.size):
                        sub.append(self.get_ith_element(i) - other.get_ith_element(i))
                return Vector(sub)

        def __mul__(self, other):
                if self.size != other.size:
                        return None
                mult = []
                dot = 0
                for i in range(self.size):
                        mult.append(self.get_ith_element(i) * other.get_ith_element(i))
                for x in range(len(mult)):
                        dot = dot + mult[x]
                return dot

        def __str__(self):
                return str(self.v)
