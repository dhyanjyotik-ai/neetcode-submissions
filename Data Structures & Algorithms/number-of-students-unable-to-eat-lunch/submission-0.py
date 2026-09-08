class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        sandwich_index = 0
        rotation_without_match = 0
        while q and rotation_without_match < len(q):
            if q[0] == sandwiches[sandwich_index]:
                q.popleft()
                sandwich_index += 1
                rotation_without_match = 0
            else:
                q.append(q.popleft())
                rotation_without_match += 1
        return len(q)

        