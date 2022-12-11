class Monkey:
    def __init__(self, items, num, op_string, test, if_true, if_false):
        self.items = items
        self.num = num
        self.op_string = op_string
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.num_inspects = 0

    def inspect_throw(self):
        old = self.items[0]
        new = float(eval(self.op_string))
        new = int(new / 3)
        self.items[0] = new
        self.num_inspects += 1
        to_throw = self.items.pop(0)
        if int(to_throw % self.test) == 0:
            return (self.if_true, to_throw)
        else:
            return (self.if_false, to_throw)

    def inspect_throw_2(self, product):
        old = self.items[0]
        new = float(eval(self.op_string))
        self.items[0] = new
        self.num_inspects += 1
        to_throw = self.items.pop(0)
        if int(to_throw % self.test) == 0:
            return (self.if_true, to_throw)
        else:
            return (self.if_false, to_throw)