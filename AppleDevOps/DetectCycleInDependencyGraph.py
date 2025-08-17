# =============================================================
# 10) Detect Cycle in Dependency Graph
# Problem:
#   Given a graph of dependencies, detect if a cycle exists.
# Example:
#   A->B, B->C, C->A -> True
# =============================================================
def has_cycle(deps: dict[str, list[str]]) -> bool:
    WHITE, GRAY, BLACK = 0,1,2                # states: unvisited, visiting, done
    color = {node: WHITE for node in deps}
    for lst in deps.values():                 # ensure all nodes included
        for v in lst:
            if v not in color: color[v]=WHITE

    def dfs(u: str) -> bool:
        if color[u]==GRAY: return True        # back-edge -> cycle
        if color[u]==BLACK: return False      # already processed
        color[u]=GRAY                         # mark as visiting
        for v in deps.get(u, []):
            if dfs(v): return True            # recurse neighbors
        color[u]=BLACK                        # mark as done
        return False

    return any(dfs(n) for n in color if color[n]==WHITE)
