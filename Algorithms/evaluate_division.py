class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def DFS(graph, nodes, a, b, value):
            gDim = len(nodes)
            #print nodes, a, b
            aInx = nodes.index(a)
            bInx = nodes.index(b)
            if graph[aInx][bInx] !=0 or graph[aInx][bInx] !=0:
                #print a, b, value
                return value * graph[aInx][bInx]

            for col in range(gDim):
                if graph[aInx][col] != 0 or graph[col][aInx] != 0:
                    #print "aInx=", aInx, "col=", col, nodes[col], b, value, graph[aInx][col]
                    return value*DFS(graph, nodes, nodes[col], b, graph[aInx][col])

        # Get list of available nodes from equations
        nodes = []
        for eq in equations:
            if eq[0] not in nodes:
                nodes.append(eq[0])
            if eq[1] not in nodes:
                nodes.append(eq[1])
        #print nodes

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
        #print graph

        # Search for solutions in queries using DFS
        ans = []
        for que in queries:
            if que[0] not in nodes or que[1] not in nodes:
                ans.append(-1.0)
            else:
                ret = DFS(graph, nodes, que[0], que[1], 1.0)
                ans.append(ret)
        return ans

[["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
[3.0,4.0,5.0,6.0]
[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]