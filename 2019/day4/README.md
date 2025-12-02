# Day 4: Secure Container

For this challenge, each rule should be considered seperately.

- It is a six-digit number - The input provided will always follow this rule
- The value is within the range given in your puzzle input - No need to go outwith puzzle input

These two rules don't really need much paying attention to, but
the next two will require more thought:

- Two adjacent digits are the same (like 22 in 122345).
- Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

So, as this challenge involves iterating over a large amount of numbers
and returning which ones are valid, once again I decided to use a generator.

```python
def valid(start, end):
    for number in range(start, end):
        prev = []
        double = False
        ordered = True
```

In order to do the comparative operators on each character of the number, it was
converted into a string and this string was iterated over in a loop.

```python
for n in str(number):
    if len(prev) > 0:
```

In this loop, first it is tested whether the number is bigger than the previous number.
If it is less, the sequence is out of order and the ordered flag is set to false.

```python
if n < prev[-1]:
    ordered = False
```

Then a check is made to see whether the number was already in the sequence. If it was
then a double it present and the first rule has been fulfilled, so the flag is set to True.

```python
elif prev.count(n) > 0:
    double = True
```

Now that the rules have been checked, the results can be yielded. For part two, since
it is known that the number is ordered then to make sure it's not a triple or more
the number of occurences must be two.

```python
if ordered: 
    yield double, 2 in Counter(prev).values()
```

Now it's just a matter of counting which results passed the rules using the generator:
```python
for rule1, rule2 in valid(153517, 630395):
    if rule1:
        total1 += 1 
    if rule1 and rule2:
        total2 += 1 
````

total1 is the solution to part 1 and total2 is the solution to part 2
