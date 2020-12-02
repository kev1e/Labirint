class LabirintTurtle():
    def __init__(self):
        self.file = None
        self.correct_map = []
        self.matrix_game = []
        self.koordinats = []
        self.is_map_valid = True
        self.check_map = True
        self.graph = None

    def load_map(self, name):
        self.file = open(name)
        s = self.file.read().split('\n')
        for i in range(len(s) - 2):
            self.matrix_game.append(list(s[i]))
        self.koordinats.append(int(s[-2]))
        self.koordinats.append(int(s[-1]))
        self.file.close()

    def show_map(self, turtle=False):
        if turtle == True:
            x = self.koordinats[0]
            y = self.koordinats[1]
            self.matrix_game[x][y] = "A"
        for i in self.matrix_game:
            print(*i, sep='\t')

    def check_map(self):
        

    def exit_count_step(self):
        pass

    def exit_show_step(self):
        pass

    def making_graph(self):
        graph = dict()
        for i in range(len(self.matrix_game)):
            for j in range(len(self.matrix_game[i])):
                if self.matrix_game[i][j] == ' ':
                    a = str(i) + ',' + str(j)
                    if self.matrix_game[i + 1][j] == ' ':
                        if a not in graph.keys():
                            graph[a] = [str(i + 1) + ',' + str(j)]
                        else:
                            mass = graph[a]
                            mass.append(str(i + 1) + ',' + str(j))
                            graph[a] = mass
                    if self.matrix_game[i][j + 1] == ' ':
                        if a not in graph.keys():
                            graph[a] = [str(i) + ',' + str(j + 1)]
                        else:
                            mass = graph[a]
                            mass.append(str(i) + ',' + str(j + 1))
                            graph[a] = mass
                    if self.matrix_game[i][j - 1] == ' ':
                        if a not in graph.keys():
                            graph[a] = [str(i) + ',' + str(j - 1)]
                        else:
                            mass = graph[a]
                            mass.append(str(i) + ',' + str(j - 1))
                            graph[a] = mass
                    if self.matrix_game[i - 1][j] == ' ':
                        if a not in graph.keys():
                            graph[a] = [str(i - 1) + ',' + str(j)]
                        else:
                            mass = graph[a]
                            mass.append(str(i - 1) + ',' + str(j))
                            graph[a] = mass
        return graph

    def find_the_way(graph, start, goal): # start(x,y) goal(x,y)
        # finding the way out
        explored = []
        queue = [[start]]
        if start == goal:
            return []
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in explored:
                neighbours = graph[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == goal:
                        return new_path
                explored.append(node)
        return None


turtle = LabirintTurtle()
turtle.load_map("Table.txt")
turtle.show_map(turtle=True)
turtle.check_map()
