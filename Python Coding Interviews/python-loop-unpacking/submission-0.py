from typing import List, Tuple
from collections import namedtuple

# 1. Define the tuple template structure


def best_student(scores: List[Tuple[str, int]]) -> str:
    result = None
    for obj in scores:
        name, score = obj

        if score is 90 or score is 100:
            result = name


    return result




# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
