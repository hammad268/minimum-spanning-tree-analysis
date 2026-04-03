import matplotlib.pyplot as plt
import networkx as nx
import heapq
import random

# -------------------------
# Disjoint Set (Union-Find)
# -------------------------
class DisjointSet:
    """Union-Find (Disjoint Set) for Kruskal Algorithm"""
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

# -------------------------
# Graph + MST Algorithms
# -------------------------
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # Edge list: (weight, u, v)
        self.nodes = list(vertices)
    
    def add_edge(self, u, v, w):
        # allow duplicate edges; graph undirected
        self.graph.append((w, u, v))
    
    # ================= KRUSKAL'S ALGORITHM =================
    def kruskal_mst(self):
        mst = []
        total_weight = 0
        
        # Sort edges by weight
        self.graph.sort()
        
        ds = DisjointSet(self.nodes)
        
        print("\n--- Kruskal's Algorithm Execution ---")
        for weight, u, v in self.graph:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                mst.append((u, v, weight))
                total_weight += weight
                print(f"Added edge: {u} -- {v} (Weight: {weight})")
        
        print(f"\nTotal MST Weight (Kruskal): {total_weight}")
        return mst, total_weight
    
    # ================= PRIM'S ALGORITHM =================
    def prim_mst(self):
        if not self.nodes:
            return [], 0
        mst = []
        total_weight = 0
        visited = set()
        min_heap = []
        
        start_vertex = self.nodes[0]
        visited.add(start_vertex)
        
        # Add all edges incident to start_vertex
        for weight, u, v in self.graph:
            if u == start_vertex:
                heapq.heappush(min_heap, (weight, u, v))
            elif v == start_vertex:
                heapq.heappush(min_heap, (weight, v, u))
        
        print("\n--- Prim's Algorithm Execution ---")
        while min_heap and len(visited) < len(self.nodes):
            weight, u, v = heapq.heappop(min_heap)
            
            if v not in visited:
                visited.add(v)
                mst.append((u, v, weight))
                total_weight += weight
                print(f"Added edge: {u} -- {v} (Weight: {weight})")
                
                # Add adjacent edges of newly added vertex v
                for w, x, y in self.graph:
                    if x == v and y not in visited:
                        heapq.heappush(min_heap, (w, x, y))
                    elif y == v and x not in visited:
                        heapq.heappush(min_heap, (w, y, x))
        
        print(f"\nTotal MST Weight (Prim): {total_weight}")
        return mst, total_weight

    # ================= VISUALIZATION =================
    def draw_graph(self, mst_edges=None, title="Graph", save_prompt=True):
        """
        Draws the graph. Uses a fixed layout for the sample graph A..F (so visualization looks stable),
        otherwise uses kamada_kawai_layout (clean).
        If save_prompt is True, shows a prompt after drawing asking whether to save the PNG.
        """
        G = nx.Graph()

        # add nodes explicitly (so isolated nodes also show)
        G.add_nodes_from(self.nodes)
        for w, u, v in self.graph:
            G.add_edge(u, v, weight=w)
        
        # Choose layout:
        sample_nodes = ['A','B','C','D','E','F']
        if set(self.nodes) == set(sample_nodes):
            # manual fixed positions for a stable, human-meaningful layout
            pos = {
                'A': (2.0, 0.0),
                'B': (3.0, 1.0),
                'C': (1.0, 0.0),
                'D': (0.0, 1.0),
                'E': (2.0, 2.0),
                'F': (0.0, 2.0)
            }
        else:
            # nicer deterministic layout for general graphs
            pos = nx.spring_layout(G, seed=42)


        plt.figure(figsize=(10, 7))
        nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=600)
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

        # Mark MST edges (undirected set)
        mst_set = set()
        if mst_edges:
            for u, v, _ in mst_edges:
                mst_set.add(frozenset((u, v)))

        all_edges = [(u, v) for w, u, v in self.graph]
        normal_edges = [e for e in all_edges if frozenset(e) not in mst_set]
        mst_edge_list = [tuple(e) for e in (list(map(tuple, (list(pair) for pair in mst_set))) )] if mst_edges else []

        # draw edges
        if normal_edges:
            nx.draw_networkx_edges(G, pos, edgelist=normal_edges, edge_color='gray', width=1)
        if mst_edges:
            # mst_edge_list constructed from mst_edges directly to preserve ordering:
            mst_edge_list = [(u, v) for u, v, w in mst_edges]
            nx.draw_networkx_edges(G, pos, edgelist=mst_edge_list, edge_color='red', width=3)

        # edge labels
        edge_labels = {}
        for w, u, v in self.graph:
            edge_labels[(u, v)] = w
            edge_labels[(v, u)] = w  # ensure undirected labeling coverage

        try:
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
        except Exception:
            # in case of any mismatch, ignore labels
            pass

        plt.title(title, fontsize=16)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

        # Optionally prompt to save
        if save_prompt:
            try:
                ans = input("Save this plot to a PNG file? (y/n) [n]: ").strip().lower() or "n"
                if ans == 'y':
                    fname = input("Enter filename (e.g. graph.png): ").strip() or "graph.png"
                    plt.savefig(fname, dpi=200, bbox_inches='tight')
                    print(f"Saved: {fname}")
            except Exception:
                # if running in an environment without stdin, skip saving prompt
                pass

# ================= SAMPLE GRAPHS =================
def create_sample_graph():
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    g = Graph(vertices)
    
    # Adding edges (u, v, weight)
    edges = [
        ('A', 'E', 4), ('A', 'C', 2), ('B', 'C', 1), ('B', 'D', 5),
        ('C', 'D', 8), ('C', 'E', 10), ('D', 'E', 2), ('D', 'F', 6),
        ('E', 'F', 3), ('B', 'E', 11)
    ]
    
    for u, v, w in edges:
        g.add_edge(u, v, w)
    
    return g

def create_random_graph(num_nodes=7, num_edges=15):
    nodes = [chr(65 + i) for i in range(num_nodes)]  # A, B, C...
    g = Graph(nodes)
    
    # Ensure connected graph (chain)
    for i in range(num_nodes - 1):
        g.add_edge(nodes[i], nodes[i+1], random.randint(1, 20))
    
    # Add more random edges (without duplicating already added chain edges)
    import itertools
    all_pairs = [p for p in itertools.combinations(nodes, 2)]
    random.shuffle(all_pairs)
    added = set(frozenset((nodes[i], nodes[i+1])) for i in range(num_nodes - 1))
    count = 0
    for u, v in all_pairs:
        if count >= (num_edges - (num_nodes - 1)):
            break
        if frozenset((u, v)) in added:
            continue
        g.add_edge(u, v, random.randint(1, 30))
        added.add(frozenset((u, v)))
        count += 1
    
    return g

# ================= MAIN MENU =================
def main():
    print("="*60)
    print("     MINIMUM SPANNING TREE (MST) PROJECT")
    print("     Kruskal's & Prim's Algorithm in Python")
    print("="*60)
    
    while True:
        print("\n" + "="*50)
        print("MENU:")
        print("1. Use Sample Graph")
        print("2. Generate Random Graph")
        print("3. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            g = create_sample_graph()
        elif choice == '2':
            print("Generating random connected graph...")
            # ask size
            try:
                n = int(input("Number of nodes (default 7): ").strip() or 7)
                m = int(input("Number of edges (default 15): ").strip() or 15)
            except Exception:
                n, m = 7, 15
            g = create_random_graph(num_nodes=n, num_edges=m)
        elif choice == '3':
            print("Thank you for using MST Project! Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")
            continue
        
        # Display original graph
        print("\nOriginal Graph Edges:")
        for w, u, v in sorted(g.graph):
            print(f"  {u} -- {v} : {w}")
        
        g.draw_graph(title="Original Graph")
        
        while True:
            print("\nSelect Algorithm:")
            print("1. Kruskal's Algorithm")
            print("2. Prim's Algorithm")
            print("3. Both Algorithms")
            print("4. Back to Main Menu")
            
            algo = input("Choose (1-4): ").strip()
            
            if algo == '1':
                mst_edges, weight = g.kruskal_mst()
                g.draw_graph(mst_edges=mst_edges, title=f"Kruskal's MST (Weight: {weight})")
            elif algo == '2':
                mst_edges, weight = g.prim_mst()
                g.draw_graph(mst_edges=mst_edges, title=f"Prim's MST (Weight: {weight})")
            elif algo == '3':
                print("\n" + "="*30 + " RUNNING BOTH " + "="*30)
                mst_k, w_k = g.kruskal_mst()
                g.draw_graph(mst_edges=mst_k, title=f"Kruskal's MST (Weight: {w_k})")
                
                mst_p, w_p = g.prim_mst()
                g.draw_graph(mst_edges=mst_p, title=f"Prim's MST (Weight: {w_p})")
            elif algo == '4':
                break
            else:
                print("Invalid option!")

if __name__ == "__main__":
    main()
