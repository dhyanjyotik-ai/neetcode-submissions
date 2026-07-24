from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    name = [""]
    score = [-1]
    for x, y in scores:
        if y > 0 and y > score[0]:
            name[0] = x
            score[0] = y
    return name[0]



# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
