
wait_for = {
    'P1': ['P2'],
    'P2': ['P3'],
    'P3': ['P1']   
}

def detect_deadlock(graph):
    visited = set()
    rec_stack = set()

    def dfs(process):
        visited.add(process)
        rec_stack.add(process)
        for neighbor in graph.get(process, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                # Cycle found
                return True
        rec_stack.remove(process)
        return False

    for p in graph:
        if p not in visited:
            if dfs(p):
                return True
    return False

def recover_deadlock(graph):
    # Simple recovery: abort one process in cycle (lowest name)
    victim = sorted(graph.keys())[0]
    print(f"Recovering by aborting {victim}")
    graph.pop(victim)
    for waits in graph.values():
        if victim in waits:
            waits.remove(victim)

print("Initial Wait-For Graph:", wait_for)
if detect_deadlock(wait_for):
    print("Deadlock detected!")
    recover_deadlock(wait_for)
else:
    print("No deadlock detected.")

print("Graph after recovery:", wait_for)
if detect_deadlock(wait_for):
    print("Still deadlocked!")
else:
    print("System is now deadlock-free.")
