# Day 1: The Tyranny of the Rocket Equation

## Part 1

This was just a simple maths equation. Divide by 3, round down, subtract 2.
Trivial to implement:

```python
def calculate_fuel_1(mass):
    return int(mass / 3) - 2
```

## Part 2

The part was more interesting. As the fuel is returned from part 1 
that fuel is mass which must also be sent up requiring more fuel. 
Then that fuel also must be sent up with more fuel with more mass etc.
until the fuel required is either 0 or less that 0.

Immediately this problem seemed to lend itself to recursion, so that's how
I implemented it:

```python
def calculate_fuel_2(mass):
    mass = int(mass / 3) - 2
    return 0 if mass < 1 else mass + calculate_fuel_2(mass)
```

Making this a bit more readable:

```python
def calculate_fuel_2(mass):
    mass = int(mass / 3) - 2
    if mass < 1:
        return 0 
    else:
        return mass + calculate_fuel_2(mass)
```

Essentially, while the mass still needs fuel, run the function
on the mass again. This recursively gets the required fuel and
fulfills the requirements in a very small amount of code. To
shorten the code a wee bit I replaced the long form conditional statement
with a conditional expression, essentially a python ternary operator.
