class Valve:
    def __init__(self, name, flow_rate, connections):
        self.name = name
        self.flow_rate = int(flow_rate)
        self.connections = connections
