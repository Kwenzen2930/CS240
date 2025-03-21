from collections import defaultdict, deque

class Graph:
    def __init__(self, is_directed=False):
        self.graph = defaultdict(list)
        self.is_directed = is_directed

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if not self.is_directed:
            self.graph[v].append(u)

    def dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=' ')
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        print("\n🔍 DFS Traversal starting from node", start)
        self.dfs_util(start, visited)
        print()

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        print("\n🚀 BFS Traversal starting from node", start)
        while queue:
            node = queue.popleft()
            print(node, end=' ')
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    def has_cycle_directed_util(self, node, visited, rec_stack):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.has_cycle_directed_util(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    def has_cycle_directed(self):
        visited = set()
        rec_stack = set()

        for node in list(self.graph.keys()):
            if node not in visited:
                if self.has_cycle_directed_util(node, visited, rec_stack):
                    return True
        return False

    def has_cycle_undirected_util(self, node, visited, parent):
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.has_cycle_undirected_util(neighbor, visited, node):
                    return True
            elif parent != neighbor:
                return True
        return False

    def has_cycle_undirected(self):
        visited = set()
        for node in list(self.graph.keys()):
            if node not in visited:
                if self.has_cycle_undirected_util(node, visited, -1):
                    return True
        return False

    def graph_statistics(self):
        num_nodes = len(self.graph)
        num_edges = sum(len(neighbors) for neighbors in self.graph.values()) // (1 if self.is_directed else 2)
        print(f"\n📊 Graph Statistics:")
        print(f"Number of nodes: {num_nodes}")
        print(f"Number of edges: {num_edges}")

    def display_graph(self):
        print("\n🌐 Graph Representation:")
        for node, neighbors in self.graph.items():
            print(f"{node} -> {', '.join(map(str, neighbors))}")

def main():
    try:
        while True:
            print("🎯 Welcome to the Graph Traversal Program!")

            graph_type = input("Is your graph directed? (yes/no): ").strip().lower()
            is_directed = graph_type == 'yes'

            g = Graph(is_directed=is_directed)

            while True:
                print("\n✨ What would you like to do?")
                print("1. Add Edge")
                print("2. Perform DFS")
                print("3. Perform BFS")
                print("4. Show Graph Statistics")
                print("5. Display Graph")
                if is_directed:
                    print("6. Check for Cycle (Directed Graph)")
                    print("7. Exit")
                else:
                    print("6. Check for Cycle (Undirected Graph)")
                    print("7. Exit")
                choice = input("Enter your choice: ")

                if choice == '1':
                    u, v = map(int, input("Enter edge (u v): ").split())
                    g.add_edge(u, v)
                elif choice == '2':
                    start = int(input("Enter the starting node for DFS: "))
                    g.dfs(start)
                elif choice == '3':
                    start = int(input("Enter the starting node for BFS: "))
                    g.bfs(start)
                elif choice == '4':
                    g.graph_statistics()
                elif choice == '5':
                    g.display_graph()
                elif choice == '6' and is_directed:
                    has_cycle = g.has_cycle_directed()
                    if has_cycle:
                        print("⚠️ Cycle detected in the directed graph!")
                    else:
                        print("✅ No cycles detected in the directed graph.")
                elif choice == '6' and not is_directed:
                    has_cycle = g.has_cycle_undirected()
                    if has_cycle:
                        print("⚠️ Cycle detected in the undirected graph!")
                    else:
                        print("✅ No cycles detected in the undirected graph.")
                elif choice == '7':
                    print("👋 Exiting. Thanks for using the program!")
                    break
                else:
                    print("⚠️ Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\n👋 Program interrupted. Exiting gracefully.")

if __name__ == "__main__":
    main()