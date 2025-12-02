# Day 2: 1202 Program Alarm

## Part 1

This challenge is essentially just implementing a parser for instructions.
At this point, the program only contains instructions with four values (apart from exit).
To keep it simple, this solution just splices 4 values and parses whatever the first one is
to get the instruction.

```python
for a, b, c, d in (code[i:i + 4] for i in range(0, len(code) - 3, 4)):
		if a == 99:
				break
		elif a == 1:
				code[d] = code[b] + code[c]
		elif a == 2:
				code[d] = code[b] * code[c]
```

Honestly this solution is pretty bad and since it's hinted that this will be used
again I'll probably have to rework it at some point but oh well.

## Part 2

Using part one, brute force some inputs to provide a set output.
Not that difficult, just loop through all possible inputs until
the correct set is found:

```python
for noun in range(99):
		for verb in range(99):
				code[1] = noun
				code[2] = verb
				if run(code.copy()) == 19690720:
						print("Noun is ", noun)
						print("Verb is ", verb)
						break

```

