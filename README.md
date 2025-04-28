# Vector2D - Library for working with 2D vectors
The Vector2D library provides an easy way to work with two-dimensional (2D) vectors in Python. It supports all the basic vector operations and has an intuitive interface.

## Main features

- Creating vectors with given coordinates
- Calculating the length (modulus) of a vector
- Scalar product of vectors
- Adding and subtracting vectors
- Multiplying a vector by a scalar
### Examples of use

Creating a vector
``` python
from vector2d import Vector2D
```

Main operations
``` python
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
```

 Додавання
 ``` python
sum_v = v1 + v2  
```

Віднімання
``` python
diff_v = v1 - v2  
```
 Множення на скаляр
 ``` python
scaled_v = v1 * 3  
```

 Довжина вектора
 ``` python
length = v1.magnitude()  
```

 Скалярний добуток
 ``` python
dot = v1.dot_product(v2)  
```
### Methods documentation
```python 
Vector2D(x, y)
```

Creates a new vector with x and y coordinates.

**Parameters:**

- x (int/float) - coordinate on the abscissa axis
- y (int/float) - coordinate on the ordinate axis

**Exceptions**
- TypeError - if the coordinates are not numbers

### Operators
|Operator| Action                   |Example|
|--------|-------                   |-------|
|+       |Adding vectors            |`v1+v2`|
|-       |Subtracting vectors       |`v1-v2`|
|*       |Multiplication by a scalar|`v1*3` |

**Methods**
`magnitude()`

Calculates the length of a vector.

**Returns:**

`float` - the length of the vector

`dot_product(other)`

Calculates a scalar product with another vector.

**Parameters:**

`other` (Vector2D) - another vector

**Returns:**

`float` - the value of the scalar product

**Exceptions:**

`TypeError` - if the parameter is not Vector2D
### Error handling

|Method Possible    | error   | Description                          |
|---------------    | -----   |------------                          |
|`__init__ `        |TypeError| Non-numeric coordinates              |
|`__add__, __sub__` |TypeError|Operations with nonvectors            |
|`__mul__ `         |TypeError|Multiplication by a non-numeric scalar|
|`dot_product`      |TypeError|Scalar product with a nonvector       |

## Author
Machok Oleksandr ,11IPZ ,student UDU Dragomanova
![gif](https://media1.tenor.com/m/3KA0kR_r8W4AAAAd/fun-memes.gif)
