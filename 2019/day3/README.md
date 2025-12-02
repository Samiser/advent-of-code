# Day 3: Crossed Wires

Whew this problem is a lot more complicated than the last two...

First, we should build a function that returns a generator for the 
sequence of coordinates of the wire. This will make comparing the
wire paths later a lot easier.

We'll start by building a dictionary of instructions:

```python
step = {'U':(0,1),
        'D':(0,-1),
        'L':(-1,0),
        'R':(1,0)}
```

Then initialise x and y: 

```python
x = y = 0
```

Now we can loop through the instructions and use the dictionary to
change the x and y values and yield the resulting sequence of coordinates:

```python
for seg in path:
    dx,dy = step[seg[0]]
    length = int(seg[1:])

    for n in range(length):
        x += dx
        y += dy
        yield x, y
```

Next, for part two, we'll make a function that creates a dictionary of 
coordinates and wire lengths travelled to reach that coordinate:

```python
for path_length, coord in enumerate(self.trace(path), 1):
    if coord not in coords:
        coords[coord] = path_length
```

This uses the generator we built earlier to calculate the distance
travelled of each coordinate using enumerate. Then it stores that
distance in a dictionary of coords.

Finally, now that each wire has a generator for the coords they can
be used like sets to find intersecting points:

```python
intersections = wire1.coords.keys() & wire2.coords.keys()
```

Now we have all we need to solve each problem. First, the intersecting
point with the minimum Manhattan distance. In this case, all that has
to be done is iterate over x and y of each intersecton's coordinates
and find the minimum sum of the absolute value of each x and y:

```python
min(abs(x)+abs(y) for x,y in intersections)
```

Second, finding the intersection with the smallest combined steps on each wire.
Again it's iterating over each intersection but now we're using the dictionary
created earlier to sum the lengths of each intersection for each wire and
find the minimum:
```python
min(wire1.coords[coord] + wire2.coords[coord] for coord in intersections)
```
