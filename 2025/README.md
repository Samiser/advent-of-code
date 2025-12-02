# Advent of Code 2025

going back to python this year!

logic in the aoc_2025 module, tests and my inputs are kept separate

example usage:

```
$ nix run . -- -h
usage: aoc [-h] [-i INPUTS] day

positional arguments:
  day

options:
  -h, --help           show this help message and exit
  -i, --inputs INPUTS  path to the input files directory (default: './input')

$ nix run . -- 1
1011
5937
```

or you could build and run the binary directly:

```
$ nix build
$ ./result/bin/aoc 1
1011
5937
```
