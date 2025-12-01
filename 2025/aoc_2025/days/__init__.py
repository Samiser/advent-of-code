import importlib
from typing import Protocol, runtime_checkable


@runtime_checkable
class Day(Protocol):
    def part1(self, data: str) -> str: ...
    def part2(self, data: str) -> str: ...


def load(day: int) -> Day:
    name = f"{__name__}.day{day:02d}"
    try:
        module = importlib.import_module(name)
        if isinstance(module, Day):
            return module
        else:
            raise
    except ModuleNotFoundError as e:
        if e.name == name:
            raise ValueError(f"No module for day {day:02d}") from None
        raise
