from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    # return max(scores, key = lambda score: score[1])[0]
    best_name = None
    best_score = None
    for name,score in scores:
        if best_score is None or score>best_score:
            best_name = name
            best_score = score
    return best_name
    


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
