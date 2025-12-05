import argparse
import cProfile
from pathlib import Path
from dataclasses import dataclass
from time import perf_counter
from pkgutil import iter_modules

from . import days
from . import inputs


@dataclass
class Args:
    day: int | None
    profile: bool
    inputs: Path


def run_day(
    day: int, input_dir: Path, profile: bool, parser: argparse.ArgumentParser
) -> float:
    try:
        module = days.load(day)
        data = inputs.load(day, input_dir)
    except ValueError as e:
        parser.error(str(e))

    print(f"\033[1mday {day}:\033[0m")

    if profile:
        profiler = cProfile.Profile()
        start = perf_counter()
        result = profiler.runcall(module.solve, data)
        time = perf_counter() - start
        print(result)
        profiler.print_stats()
    else:
        start = perf_counter()
        result = module.solve(data)
        time = perf_counter() - start
        print(result)
        print(f"\033[2mtime: {time * 1000:.2f} ms\033[0m")

    return time


def main() -> None:
    parser = argparse.ArgumentParser()
    _ = parser.add_argument(
        "-d", "--day", type=int, help="run a specific day (runs all days by default)"
    )
    _ = parser.add_argument(
        "-i",
        "--inputs",
        type=Path,
        default=Path("inputs"),
        help="path to the input files directory (default: './input')",
    )
    _ = parser.add_argument(
        "-p",
        "--profile",
        action="store_true",
        help="print cProfile results instead of time taken",
    )

    args = parser.parse_args(namespace=Args)

    if args.day == None:
        total_time = sum(
            run_day(day + 1, args.inputs, args.profile, parser)
            for day in range(len(list(iter_modules(days.__path__))))
        )
        if not args.profile:
            print(f"\ntotal time: {total_time * 1000:.2f} ms")
    else:
        _time = run_day(args.day, args.inputs, args.profile, parser)
