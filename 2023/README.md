# Advent of Code 2023
doing it in rust this year

can build with nix or cargo
```
nix build
cargo build
```

using entr for real time compilation and running like so
```
ls -d src/*  | entr nix run . -- one input/day1.txt
```
