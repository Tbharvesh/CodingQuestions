from typing import List


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited =[False]*n
        cnt = 0
        for i in range(n):
            if visited[i] == False:
                visited[i] = True
                cnt += 1
                elem = i
                q=[elem]
                while q:
                    elem = q[0]
                    q.pop(0)
                    for j in range(n):
                        if isConnected[elem][j] ==1 and visited[j] ==False:
                            q.append(j)
                            visited[j] = True
        return cnt
                
