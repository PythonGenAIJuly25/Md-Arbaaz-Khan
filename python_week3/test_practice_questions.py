
from collections import defaultdict, deque

# Task Scheduler Function
def task_scheduler(tasks, dependencies):
    graph = defaultdict(list)
    indegree = {task: 0 for task in tasks}

    for task, prereq in dependencies:
        graph[prereq].append(task)
        indegree[task] += 1

    queue = deque([task for task in tasks if indegree[task] == 0])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == len(tasks) else None

# Helper for topological sort validation
def is_valid_topo_order(order, tasks, dependencies):
    if order is None: return False
    position = {task: i for i, task in enumerate(order)}
    return all(position[prereq] < position[task] for task, prereq in dependencies)

# Merge Intervals Function
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

# === Test Cases ===

# Task Scheduler Tests
def test_task_scheduler():
    tasks1 = ["A", "B", "C", "D"]
    deps1 = [("B", "A"), ("C", "B"), ("D", "A")]
    assert is_valid_topo_order(task_scheduler(tasks1, deps1), tasks1, deps1)

    tasks2 = ["X", "Y", "Z"]
    deps2 = [("Y", "X"), ("Z", "Y"), ("X", "Z")]
    assert task_scheduler(tasks2, deps2) is None

    tasks3 = ["P", "Q", "R"]
    deps3 = []
    assert is_valid_topo_order(task_scheduler(tasks3, deps3), tasks3, deps3)

    tasks4 = ["compile", "test", "deploy", "build", "package"]
    deps4 = [("test", "compile"), ("deploy", "package"), ("package", "build"), ("build", "compile")]
    assert is_valid_topo_order(task_scheduler(tasks4, deps4), tasks4, deps4)

# Merge Intervals Tests
def test_merge_intervals():
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge_intervals([[1,4],[4,5]]) == [[1,5]]
    assert merge_intervals([[1,4],[2,3]]) == [[1,4]]
    assert merge_intervals([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]]
    assert merge_intervals([[1,4],[2,5],[3,6]]) == [[1,6]]
    assert merge_intervals([[6,7],[2,4],[5,9]]) == [[2,4],[5,9]]
    assert merge_intervals([[1,4]]) == [[1,4]]
    assert merge_intervals([[2,3],[4,5],[6,7],[8,9],[1,10]]) == [[1,10]]

if __name__ == "__main__":
    test_task_scheduler()
    test_merge_intervals()
    print("✅ All test cases passed.")
