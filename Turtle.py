def find_the_way(graph, start, goal):  # start(x,y) goal(x,y)
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


class LabirintTurtle():
    def __init__(self):
        self.file = None
        self.correct_map = []
        self.matrix_game = []
        self.koordinats = []
        self.graph = None
        self.x = None
        self.y = None
        self.exits = []
        self.paths = []

    def load_map(self, name):
        self.file = open(name)
        s = self.file.read().split('\n')
        for i in range(len(s) - 2):
            self.matrix_game.append(list(s[i]))
        try:
            self.x = self.koordinats.append(int(s[-2]))
            self.y = self.koordinats.append(int(s[-1]))
            if self.check_map() == "Ошибка":
                print("Карта не валидна")
                self.load_map(input())
        except ValueError:
            print("Координат черепахи нет")
            self.load_map(input())
        self.file.close()

    def show_map(self, turtle=False):
        if turtle == True:
            x = self.koordinats[0]
            y = self.koordinats[1]
            self.matrix_game[x][y] = "A"
        for i in self.matrix_game:
            print(*i, sep='\t')

    def check_map(self):
        for i in range(len(self.matrix_game)):
            for j in range(len(self.matrix_game[i])):
                if self.matrix_game[i][j] != ' ' and self.matrix_game[i][j] != '*':
                    return "Ошибка"
        if self.matrix_game[self.koordinats[0]][self.koordinats[1]] == '*':
            return "Ошибка"
        for i in range(len(self.matrix_game)):
            for j in range(len(self.matrix_game[i])):
                if i == 0 or j == 0 or i == len(self.matrix_game) - 1 or i == len(self.matrix_game[0]) - 1:
                    if self.matrix_game[i][j] == ' ':
                        self.exits.append([i, j])
        if self.exits == []:
            return "Ошибка"
        start = str(self.koordinats[0]) + ',' + str(self.koordinats[1])
        for exit in self.exits:
            exit_str = str(exit[0]) + ',' + str(exit[1])
            result = find_the_way(self.making_graph(), start, exit_str)
            if result != None:
                self.paths.append(result)
        if self.paths == []:
            return "Ошибка"
        return '.'
        

    def exit_count_step(self):
        print(len(self.paths[0]))

    def exit_show_step(self):
        for i in range(len(self.paths[0])):
            x = int(self.paths[0][i][0])
            y = int(self.paths[0][i][2])
            self.matrix_game[x][y] = '.'
        self.show_map()
        for i in range(len(self.paths[0])):
            x = int(self.paths[0][i][0])
            y = int(self.paths[0][i][2])
            self.matrix_game[x][y] = ' '

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




#turtle = LabirintTurtle()
#turtle.load_map("Table.txt")
#turtle.show_map(turtle=True)
#print('---------------------')
#turtle.exit_show_step()
