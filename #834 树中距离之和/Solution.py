from typing import List

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        ans = []
        for i in range(0, N):
            temp_ans = 0
            for j in range(0, N):
                if i == j:
                    continue
                temp_ans += self.bfs(i, j, edges)
            ans.append(temp_ans)
        return ans
    
    def bfs(self, i: int, j: int, edges: List[List[int]]) -> int:
        pathes = [[i]]
        seen = []
        while pathes:
            path = pathes.pop()
            node_a = path[-1]
            for pair in edges:
                if node_a in pair:
                    node_b = pair[pair.index(node_a) - 1]
                    if node_b in seen:
                        continue
                    new_path = path + [node_b]
                    if node_b == j:
                        return len(new_path) - 1
                    pathes.insert(0, new_path)
            seen.append(node_a)
        return 0