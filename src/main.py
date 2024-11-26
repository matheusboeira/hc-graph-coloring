import networkx as nx
import random
import matplotlib.pyplot as plt
from simple_term_menu import TerminalMenu
from colored import Fore, Style

seed = 42

def generate_edges(num_nodes, num_edges: int = 2):
    edges = []
    random.seed(seed)

    # Se o número de arestas for 1, faz uma conexão em "minhoca" (sequencial)
    if num_edges == 1:
        for i in range(num_nodes - 1):
            edges.append((i, i + 1)) 
        return edges

    # Caso contrário, gera as arestas de forma aleatória
    for i in range(num_nodes):
        _num_edges = random.randint(1, num_edges) 

        for _ in range(_num_edges):
            # Escolhe um nó aleatório para conectar (evita conectar o nó consigo mesmo)
            neighbor = random.choice([n for n in range(num_nodes) if n != i])

            # Verifica se a aresta já foi adicionada (evita arestas duplicadas)
            if (i, neighbor) not in edges and (neighbor, i) not in edges:
                edges.append((i, neighbor))

    return edges


class GraphColoringHillClimbing:
    show_graph = False

    def __init__(self, graph, max_colors=5):
        """
        Inicializa o algoritmo de coloração de grafos com subida de encosta.

        :param graph: Grafo de entrada (NetworkX)
        :param max_colors: Número máximo de cores disponíveis
        """
        self.graph = graph
        self.max_colors = max_colors
        self.nodes = list(graph.nodes())


    def set_show_graph(self, show_graph: bool):
        self.show_graph = show_graph


    def initial_solution(self):
      """
      Generates a consistent initial random coloring solution.

      :return: Dictionary of colors for each node
      """
      random.seed(seed)  # Set a fixed seed for deterministic randomness
      return {node: random.randint(0, self.max_colors - 1) for node in self.nodes}
    

    def conflicts(self, coloring):
        """
        Conta o número de conflitos de coloração.

        :param coloring: Dicionário de cores atual
        :return: Número de conflitos
        """
        conflicts = 0

        for edge in self.graph.edges():
            if coloring[edge[0]] == coloring[edge[1]]:
                conflicts += 1
        return conflicts


    def hill_climbing_first_choice_coloring(self, max_iterations=500_000):
      current_coloring = self.initial_solution()
      current_conflicts = self.conflicts(current_coloring)

      print("Número de conflitos iniciais:", current_conflicts)
      
      if self.show_graph:
        self.visualize_graph(current_coloring)
      
      for _ in range(max_iterations):  
          if current_conflicts == 0 or _ == max_iterations - 1:
              print("Número de iterações: ", _ + 1)

          if current_conflicts == 0:
              return current_coloring
          
          if _ == max_iterations - 1:
              print("---")
              print("Algoritmo parou.")
              print("Máximo de iterações atingido ou solução ótima não encontrada.")
              print("---")
              break
          
          conflicted_nodes = [
              node for node in self.nodes 
              for neighbor in self.graph.neighbors(node) 
              if current_coloring[node] == current_coloring[neighbor]
          ]
          
          if conflicted_nodes:
              node_to_recolor = random.choice(conflicted_nodes)
              
              # Primeira melhora encontrada
              for new_color in random.sample(range(self.max_colors), self.max_colors):
                  if new_color == current_coloring[node_to_recolor]:
                      continue
                  
                  test_coloring = current_coloring.copy()
                  test_coloring[node_to_recolor] = new_color
                  test_conflicts = self.conflicts(test_coloring)
                  
                  if test_conflicts < current_conflicts:
                      current_coloring = test_coloring
                      current_conflicts = test_conflicts
                      break
      
      return current_coloring
    

    def hill_climbing_steepest_coloring(self, max_iterations=500_000):
      current_coloring = self.initial_solution()
      current_conflicts = self.conflicts(current_coloring)

      print("Número de conflitos iniciais:", current_conflicts)

      if self.show_graph:
        self.visualize_graph(current_coloring)

      for iteration in range(max_iterations):
          if current_conflicts == 0:
              print(f"Solução encontrada em {iteration + 1} iterações.")
              return current_coloring

          best_coloring = None
          best_conflicts = current_conflicts

          # Itera por todos os nós em conflito
          conflicted_nodes = [
              node for node in self.nodes
              for neighbor in self.graph.neighbors(node)
              if current_coloring[node] == current_coloring[neighbor]
          ]

          if not conflicted_nodes:
              print("Nenhum nó em conflito encontrado, mas ainda há conflitos.")
              break

          for node_to_recolor in conflicted_nodes:
              for new_color in range(self.max_colors):
                  if new_color == current_coloring[node_to_recolor]:
                      continue

                  test_coloring = current_coloring.copy()
                  test_coloring[node_to_recolor] = new_color
                  test_conflicts = self.conflicts(test_coloring)

                  # Atualiza se encontrar uma solução melhor
                  if test_conflicts < best_conflicts:
                      best_coloring = test_coloring
                      best_conflicts = test_conflicts

          # Se nenhuma melhoria foi encontrada, estamos presos em um platô
          if best_coloring is None:
              print("---")
              print("Nenhuma melhoria encontrada, algoritmo parou.")
              break

          # Aceita a melhor solução encontrada
          current_coloring = best_coloring
          current_conflicts = best_conflicts

      print("Máximo de iterações atingido ou solução ótima não encontrada.")
      print("---")
      return current_coloring

    def visualize_graph(self, coloring):
        """
        Visualiza o grafo com a coloração encontrada.

        :param coloring: Dicionário de cores
        """
        plt.figure(figsize=(5, 5))
        pos = nx.spring_layout(self.graph, seed=seed)
        colors = [coloring[node] for node in self.nodes]
        nx.draw(
            self.graph,
            pos,
            node_color=colors,
            with_labels=True,
            cmap=plt.cm.Set3,
            node_size=700
        )
        plt.title("Coloração de Grafos - Subida de Encosta")
        plt.show()

# Exemplo de uso
def main():
    G = nx.Graph()

    options = [
      "Gerar 100 Vértices", 
      "Gerar 50 Vértices", 
      "Gerar 10 Vértices", 
      "Inserir quantidade"
    ]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    nodes_map = { 0: 100, 1: 50, 2: 10 }
    option = nodes_map.get(menu_entry_index, None)

    if option != None:
        num_max_edges = int(input(f"{Fore.BLUE}Digite o número de arestas{Style.RESET}: "))
        G.add_edges_from(generate_edges(option, num_max_edges))

    if option == None:
        _input = int(input(f"{Fore.BLUE}Número de vértices{Style.RESET}: "))
        num_max_edges = int(input(f"{Fore.BLUE}Digite o número de arestas{Style.RESET}: "))
        G.add_edges_from(generate_edges(_input, num_max_edges)) 
        
    # Inicializa o algoritmo
    gc_hc = GraphColoringHillClimbing(G, max_colors=3)

    show_graph = input(f"{Fore.BLUE}Deseja visualizar o grafo? (S/N){Style.RESET}: ")
    show_graph = show_graph.lower() == "s"

    if show_graph:
        gc_hc.set_show_graph(show_graph)

    # Executa a coloração
    options = ["Steepest", "First Choice"]
    terminal_menu = TerminalMenu(options)
    print(f"{Fore.BLUE}Escolha a variação do algoritmo:{Style.RESET}", end="\n")
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        solution = gc_hc.hill_climbing_steepest_coloring()
    elif menu_entry_index == 1:
        solution = gc_hc.hill_climbing_first_choice_coloring()

    # Imprime resultados
    conflicts = gc_hc.conflicts(solution)
    print(f"{Fore.YELLOW}Número de conflitos{Style.RESET}:", conflicts)

    # Visualiza o grafo
    if show_graph:
        gc_hc.visualize_graph(solution)

# Executa o exemplo
if __name__ == "__main__":
    main()