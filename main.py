import math


class Vector2D:
    """
    This class implements a 2D vector with common vector operations.
    """

    def __init__(self, x: float, y: float):
        """
        Initializing a vector in 2D space with the specified coordinates.

        :param x: Numeric coordinate on the abscissa axis (integer or real number)
        :param y: Numeric coordinate on the ordinate axis (integer or real number)
        :raises TypeError: If any of the coordinates is not a numeric value

        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates x and y must be numbers.")
        self._x = float(x)
        self._y = float(y)


    def x(self):
        """
        Returns the abscissa axis of the vector.

        """
        return self._x


    def y(self):
        """
        Returns the ordinate axis of the vector.

        """
        return self._y

    def __str__(self):
        """
        Returns the string representation of the vector.

        :return: A string in the format 'Vector2D(x, y)'.

        """
        return f"Vector2D({self._x}, {self._y})"

    def __add__(self, other):
        """
       Adds a vector to another vector.

        :param other: Another instance of Vector2D to add.
        :return: A new instance of Vector2D as the result of the sum.
        :raises TypeError: If the other object is not a Vector2D instance.

        """
        if not isinstance(other, Vector2D):
            raise TypeError("Addition is only possible between instances of Vector2D.")
        return Vector2D(self._x + other.x, self._y + other.y)

    def __sub__(self, other):
        """
        Subtracts one vector from another.

        :param other: Another instance of Vector2D to subtract from.
        :return: A new instance of Vector2D as the result of the subtraction.
        :raises TypeError: If the other object is not a Vector2D instance.

        """
        if not isinstance(other, Vector2D):
            raise TypeError("Subtraction is only possible between instances of Vector2D.")
        return Vector2D(self._x - other.x, self._y - other.y)

    def __mul__(self, scalar):
        """
        Multiplies a vector by a scalar.

        :param scalar: The number to multiply by.
        :return: A new instance of Vector2D with scaled coordinates.
        :raises TypeError: If the scalar is not a number.

        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Multiplication is only possible with a numeric value.")
        return Vector2D(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar):
        """
        Implements reverse multiplication (scalar * vector)

        """
        return self.__mul__(scalar)

    def magnitude(self):
        """
        Calculates the magnitude (length) of the vector.

        :return: The magnitude of the vector as a float.

        """
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def dot_product(self, other):
        """
        Calculates the dot product of two vectors.

        :param other: Another instance of Vector2D.
        :return: The dot product as a float.
        :raises TypeError: If the other object is not a Vector2D instance.

        """
        if not isinstance(other, Vector2D):
            raise TypeError("A second instance of Vector2D is required for computation.")
        return self._x * other.x + self._y * other.y


if __name__ == "__main__":
    try:
        v1 = Vector2D(5, 6)
        v2 = Vector2D(3.4, 4)
        v3 = Vector2D(0, 7)

        print("v1:", v1)
        print("v2:", v2)
        print("Magnitude v1:", round(v1.magnitude(), 2))
        print("Dot product v1 and v2:", v1.dot_product(v2))

        print("v1 + v2:", v1 + v2)
        print("v1 - v2:", v1 - v2)
        print("v1 * 3:", v1 * 5)
        print("2 * v2:", 3 * v2)

    except Exception as e:
        print("Error:", e)