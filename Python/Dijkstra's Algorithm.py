class Dijkstra:
    def __init__(self, graph, costs, parents):
        self.graph = graph
        self.costs = costs
        self.parents = parents
        

    def find_lowest_cost_node(self):
        lowest_cost = float("inf")
        lowest_cost_node = None

        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        
        return lowest_cost_node

    def find_lowest_cost_path(self):
        processed = []
        node = find_lowest_cost_node(self.costs)
        
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]

            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if new_cost < self.costs[n]:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            
            processed.append(node)
            node = find_lowest_cost_node(processed)

        # return a list of path
        i = "finish"
        path = ["finish"]
        while not parents[i] == "start":
            path.append(parents[i])
            i = parents[i]
        path.append("start")

        return path

