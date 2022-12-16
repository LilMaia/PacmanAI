# Rafael de Paula Maia
# Luam Gonçalves
# Celia Regina
# Lucas Coelho
# Gustavo Vieira

import util


class SearchProblem:
    """Esta classe descreve a estrutura de um problema de pesquisa, mas não implementa
    qualquer um dos métodos (na terminologia orientada a objetos: uma classe abstrata)."""

    def getStartState(self):
        """Retorna o estado inicial do problema de pesquisa."""
        util.raiseNotDefined()

    def isGoalState(self, state):
        """estado: estado de pesquisa
        Retorna True se e somente se o estado for um estado de objetivo válido."""
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """estado: estado de pesquisa
        Para um determinado estado, isso deve retornar uma lista de triplos, (sucessor,
        action, stepCost), onde 'successor' é um sucessor do atual
        estado, 'action' é a ação necessária para chegar lá e 'stepCost' é
        o custo incremental de expansão para esse sucessor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """ações: Uma lista de ações a serem executadas

        Este método retorna o custo total de uma determinada sequência de ações.
        A sequência deve ser composta por jogadas legais.
        """
        util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Busca em largura: pesquisa primeiro os nós mais rasos na árvore de pesquisa."""
    s,S,q,P,goal = problem.getStartState(),set(),[],{},None
    S.add(s)
    for i in problem.getSuccessors(s):
        P[i] = (s,None,None)
        q.append(i)
    while q:
        u = q.pop(0)
        if problem.isGoalState(u[0]):
            goal = u
            break
        for j in problem.getSuccessors(u[0]):
            if j[0] in S: continue
            S.add(j[0])
            q.append(j)
            P[j] = u
    path,node = [],goal
    while node != (s,None,None):
        path.append(node[1])
        node = P[node]
    path.reverse()
    return path

def nullHeuristic(state, problem=None):
    """Uma função heurística estima o custo do estado atual para o mais próximo
    meta no SearchProblem fornecido. Essa heurística é trivial."""
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Pesquisa primeiro o nó que tem o menor custo combinado e a heurística."""
    visited = set()
    start = problem.getStartState()
    from util import PriorityQueue
    frontLine = PriorityQueue()
    startPri = 0 + heuristic(start, problem)
    frontLine.push((start, [], 0), startPri)
    while not frontLine.isEmpty():
        (point, actions, cost) = frontLine.pop()
        visited.add(point)
        if problem.isGoalState(point):
            return actions
        for (p, action, stepCost) in (s for s in problem.getSuccessors(point) if s[0] not in visited):
            newCost = cost + stepCost
            newActions = actions[:]
            newActions.append(action)
            newPri = newCost + heuristic(p, problem)
            frontLine.push((p, newActions, newCost), newPri)

# Abreviações
bfs = breadthFirstSearch
astar = aStarSearch
