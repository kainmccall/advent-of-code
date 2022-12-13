class Cave:
    def __init__(self, name):
        self.name = name
        if self.name.isupper():
            self.is_big = True
        else:
            self.is_big = False
        self.connections = []

    def explore(self, current_path, path_list):
        current_path = current_path + '-' + self.name
        if self.name == 'end':
            path_list.append(current_path)
            return
        else:
            for cv in self.connections:
                if cv.is_big or (not cv.check_for_visits(current_path)):
                    cv.explore(current_path, path_list)

    def check_for_visits(self, current_path):
        caves_visited = current_path.split('-')
        if self.name in caves_visited:
            return True
        else:
            return False

    def explore_2(self, current_path, path_list, small_caves):
        current_path = current_path + '-' + self.name
        #print("Current path: " + current_path)
        if self.name == 'end':
            path_list.append(current_path)
            #print("New valid path found: " + current_path)
            return
        else:
            for cv in self.connections:
                #print("Testing " + cv.name)
                if cv.is_big or (not cv.check_for_visits_2(current_path, small_caves)):
                    #print("Exploring " + cv.name)
                    cv.explore_2(current_path, path_list, small_caves)

    def check_for_visits_2(self, current_path, small_caves):
        if self.name == 'start':
            #print(self.name + " failed at start")
            return True
        caves_visited = current_path.split('-')
        limit_reached = False
        for cv in small_caves:
            if caves_visited.count(cv) > 1:
                limit_reached = True
        if limit_reached:
            if self.name in caves_visited:
                return True
            else:
                return False
        else:
            return False