import json

class SegmentedCrossroad():
    
    def __init__(self, inner_nodes, border_nodes, edges_by_nodes, branches):
        self.inner_nodes = inner_nodes
        self.border_nodes= border_nodes
        self.edges_by_nodes = edges_by_nodes
        self.branches = branches

class SegmentedBranch():

    def __init__(self, inner_nodes, border_nodes, edges_by_nodes):
        self.inner_nodes = inner_nodes
        self.border_nodes= border_nodes
        self.edges_by_nodes = edges_by_nodes

class SegmentationReader():

    def __init__(self, path):
        self.data = json.load(open(path))
        self.crossroads = []

        # If there is more than one crossroad
        if isinstance(self.data[0], list):
            for crossroad in self.data:
                self.crossroads.append(self.__read_crossroad_data(crossroad))
        else:
            self.crossroads.append(self.__read_crossroad_data(self.data))

    def getNumberOfCrossRoads(self):
        return len(self.crossroads)

    def getCrossroads(self):
        return self.crossroads

    def __read_crossroad_data(self, data):
        crossroad = None
        branches = []
        for el in data:
            inner_nodes =       el['nodes']['inner']
            border_nodes =      el['nodes']['border']
            edges_by_nodes =    el['edges_by_nodes']
            if el['type'] == 'crossroad':
                crossroad = SegmentedCrossroad(inner_nodes, border_nodes, edges_by_nodes, None)
            else:
                branches.append(SegmentedBranch(inner_nodes, border_nodes, edges_by_nodes))
        crossroad.branches = branches
        return crossroad