from collections import defaultdict, deque

def task_scheduler(tasks, dependencies):
    graph = defaultdict(list)
    indegree = {task: 0 for task in tasks}

    # Build graph and indegree
    for task, prereq in dependencies:
        graph[prereq].append(task)
        indegree[task] += 1

    # Queue for nodes with no prerequisites
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
# Task Scheduler
tasks1 = ["A", "B", "C", "D"]
dependencies1 = [("B", "A"), ("C", "B"), ("D", "A")]
print(task_scheduler(tasks1, dependencies1))  # Example output: ['A', 'D', 'B', 'C']
