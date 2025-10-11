import sys
import os

def pytest_collection_finish(session):
    """
    Called after collection has been performed.
    """
    for item in session.items:
        solution_dir = os.path.dirname(item.fspath)
        if solution_dir not in sys.path:
            sys.path.insert(0, solution_dir)