class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Get list of available nodes from equations
        nodes = []
        for eq in equations:
            if eq[0] not in nodes:
                nodes.append(eq[0])
            if eq[1] not in nodes:
                nodes.append(eq[1])
        print nodes

        # Populate graph from equations and values
        numNodes = len(nodes)
        graph = [[0] * numNodes for i in range(numNodes)]
        numEq = len(equations)
        for inx in range(numEq):
            eq = equations[inx]
            inx1 = nodes.index(eq[0])
            inx2 = nodes.index(eq[1])
            graph[inx1][inx2] = values[inx]
            graph[inx2][inx1] = 1.0 / values[inx]
        print graph

        # Search for solutions in queries using DFS
        ans = []
        for que in queries:
            if que[0] not in nodes or que[1] not in nodes:
                ans.append(-1)
            