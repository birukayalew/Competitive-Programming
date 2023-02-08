class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)

        for i, route in enumerate(routes):
            for r in route:
                graph[r].add(i)

        if source == target: return 0
        if source not in graph: return -1

        queue = [(x, 1) for x in graph[source]]
        visited = set([x for x,_ in queue])

        while queue:
            rid, b = queue.pop(0)

            for stop in routes[rid]:
                if stop == target:
                    return b
                for i in graph[stop]:
                    if i not in visited:
                        queue.append((i, b+1))
                        visited.add(i)
        return -1