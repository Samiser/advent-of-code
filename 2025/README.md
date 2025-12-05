# Advent of Code 2025

going back to python this year!

logic in the aoc_2025 module, tests and my inputs are kept separate

example usage:

```
$ nix run . -- -h
usage: aoc [-h] [-d DAY] [-i INPUTS] [-p]

options:
  -h, --help           show this help message and exit
  -d, --day DAY        run a specific day (runs all days by default)
  -i, --inputs INPUTS  path to the input files directory (default: './input')
  -p, --profile        print cProfile results instead of time taken

$ nix run . -- -d 1
day 1:
1011
5937
time: 0.97 ms
```

or you could build and run the binary directly:

```
$ nix build
$ ./result/bin/aoc -d 1 -p
day 1:
1011
5937
         4155 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     4147    0.000    0.000    0.000    0.000 day01.py:1(count_zero_passes)
        1    0.000    0.000    0.002    0.002 day01.py:34(solve)
        3    0.000    0.000    0.000    0.000 day01.py:35(<genexpr>)
        1    0.001    0.001    0.002    0.002 day01.py:9(day1)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'splitlines' of 'str' objects}
```
