OP_DICT = {'+':'-', '-':'+', '*': '/', '/':'*'}


class Monkey:
    def __init__(self, monkey_line):
        half_line = monkey_line.split(': ')
        self.name = half_line[0]
        terms = half_line[1].split(' ')
        self.inv_tup = (0, '+', 0)
        if len(terms) == 1:
            self.is_num = True
            self.value_tup = (0, '+', 0)
            self.value = int(terms[0])
        else:
            self.is_num = False
            self.value = 0
            self.value_tup = (terms[0], terms[1], terms[2])


    def get_value(self, monkeys, set_value=False):
        if self.is_num:
            return self.value
        else:
            monkey_a = monkeys[self.value_tup[0]].get_value(monkeys)
            monkey_b = monkeys[self.value_tup[2]].get_value(monkeys)
            value = int(eval(str(monkey_a) + ' ' + self.value_tup[1] + ' ' + str(monkey_b)))
            if set_value:
                self.is_num = True
                self.value = value
            return value

    # def populate_inverses(self, monkeys, target):
    #     print(self.name)
    #     if not self.is_num:
    #         a = self.value_tup[0]
    #         op = self.value_tup[1]
    #         b = self.value_tup[2]
    #         # if monkeys[a].inv_tup[0] == 0 or monkeys[b].inv_tup[0] == 0:
    #         #     print("Loop, maybe???")
    #         #     print(self.name)
    #         depend_a = [False]
    #         depend_b = [False]
    #         monkeys[a].find_dependent(monkeys, target, depend_a)
    #         monkeys[b].find_dependent(monkeys, target, depend_b)
    #         if depend_a[0]:
    #             monkeys[a].inv_tup = (self.name, OP_DICT[op], b)
    #         if depend_b[0]:
    #             if op == '+':
    #                 monkeys[b].inv_tup = (self.name, '-', a)
    #             elif op == '-':
    #                 monkeys[b].inv_tup = (a, '-', self.name)
    #             elif op == '*':
    #                 monkeys[b].inv_tup = (self.name, '/', a)
    #             elif op == '/':
    #                 monkeys[b].inv_tup = (a, '/', self.name)
    #         # print(self.name + ' = ' + a + ' ' + op + ' ' + b + ':')
    #         # print(monkeys[a].name + ' = ' + monkeys[a].inv_tup[0] + ' ' + monkeys[a].inv_tup[1] + ' ' + monkeys[a].inv_tup[2])
    #         # print(monkeys[b].name + ' = ' + monkeys[b].inv_tup[0] + ' ' + monkeys[b].inv_tup[1] + ' ' + monkeys[b].inv_tup[2])
    #         # print('\n')

    def populate_inverses(self, monkeys):
        # print(self.name)
        if not self.is_num:
            a = self.value_tup[0]
            op = self.value_tup[1]
            b = self.value_tup[2]
            # if monkeys[a].inv_tup[0] == 0 or monkeys[b].inv_tup[0] == 0:
            #     print("Loop, maybe???")
            #     print(self.name)
            monkeys[a].inv_tup = (self.name, OP_DICT[op], b)
            if op == '+':
                monkeys[b].inv_tup = (self.name, '-', a)
            elif op == '-':
                monkeys[b].inv_tup = (a, '-', self.name)
            elif op == '*':
                monkeys[b].inv_tup = (self.name, '/', a)
            elif op == '/':
                monkeys[b].inv_tup = (a, '/', self.name)
            # print(self.name + ' = ' + a + ' ' + op + ' ' + b + ':')
            # print(monkeys[a].name + ' = ' + monkeys[a].inv_tup[0] + ' ' + monkeys[a].inv_tup[1] + ' ' + monkeys[a].inv_tup[2])
            # print(monkeys[b].name + ' = ' + monkeys[b].inv_tup[0] + ' ' + monkeys[b].inv_tup[1] + ' ' + monkeys[b].inv_tup[2])
            # print('\n')

    def find_dependent(self, monkeys, dependent, dependency, tree):
        # print("searching dependency of " + self.name)
        # print(tree)
        if self.name == dependent:
            dependency[0] = True
        else:
            if not self.is_num:
                if dependent in self.value_tup:
                    dependency[0] = True
                    tree = tree + '-' + self.name
                else:
                    tree = tree + '-' + self.name
                    monkeys[self.value_tup[0]].find_dependent(monkeys, dependent, dependency, tree)
                    monkeys[self.value_tup[2]].find_dependent(monkeys, dependent, dependency, tree)

    # def get_value_from_inverse(self, monkeys, target, set_value=False):
    #     if self.is_num:
    #         print(self.name + '!')
    #         return self.value
    #     else:
    #         # print(self.name)
    #         print(self.name + '?')
    #         dep = [False]
    #         self.find_inv_dependent(monkeys, target, dep)
    #         if dep[0]:
    #             monkey_a = monkeys[self.inv_tup[0]].get_value_from_inverse(monkeys)
    #             monkey_b = monkeys[self.inv_tup[2]].get_value_from_inverse(monkeys)
    #         else:
    #             monkey_a = monkeys[self.value_tup[0]].get_value(monkeys)
    #             monkey_b = monkeys[self.value_tup[2]].get_value(monkeys)
    #         value = int(eval(str(monkey_a) + ' ' + self.inv_tup[1] + ' ' + str(monkey_b)))
    #         if set_value:
    #             self.is_num = True
    #             self.value = value
    #         return value

    def get_value_from_inverse(self, monkeys, set_value=False):
        if self.is_num:
            print(self.name + '!')
            return self.value
        else:
            # print(self.name)
            print(self.name + '?')
            monkey_a = monkeys[self.inv_tup[0]].get_value_from_inverse(monkeys)
            monkey_b = monkeys[self.inv_tup[2]].get_value_from_inverse(monkeys)
            value = int(eval(str(monkey_a) + ' ' + self.inv_tup[1] + ' ' + str(monkey_b)))
            if set_value:
                self.is_num = True
                self.value = value
            return value

    def find_inv_dependent(self, monkeys, dependent, dependency):
        print("searching inv. dependency of " + self.name + ': ' + self.inv_tup[0] + ', ' + self.inv_tup[2] + '; is_num = ' + str(self.is_num))
        if self.name == dependent:
            dependency[0] = True
        else:
            if not self.is_num:
                if dependent in self.inv_tup:
                    dependency[0] = True
                    return dependency
                else:
                    monkeys[self.inv_tup[0]].find_inv_dependent(monkeys, dependent, dependency)
                    monkeys[self.inv_tup[2]].find_inv_dependent(monkeys, dependent, dependency)