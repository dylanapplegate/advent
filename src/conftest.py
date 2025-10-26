from pathlib import Path
from typing import Iterator
import pytest


def get_solution_paths(root_dir: str) -> Iterator[Path]:
    for p in Path(root_dir).rglob("**/python/solution.py"):
        if "node_modules" not in str(p) and ".venv" not in str(p):
            yield p


def pytest_generate_tests(metafunc: "pytest.Metafunc") -> None:
    if "solution_path" in metafunc.fixturenames:
        solution_paths = list(get_solution_paths("src"))
        metafunc.parametrize(
            "solution_path", solution_paths, ids=[str(p) for p in solution_paths]
        )
