from typing import List
import heapq

class Solution:
    def stableMarriage(self, men: List[List[int]], women: List[List[int]]) -> List[int]:
        n = len(men)
        
        # Precompute inverse ranks for women: rank[w][m] = position of m in women[w]
        rank = [[0] * n for _ in range(n)]
        for w in range(n):
            for r, m in enumerate(women[w]):
                rank[w][m] = r
        
        wife = [-1] * n
        husband = [-1] * n
        
        # Next woman index for each free man
        next_prop = [0] * n
        
        free_men = list(range(n))  # Use queue-like list
        
        while free_men:
            m = free_men[0]
            proposed = False
            
            for i in range(next_prop[m], n):
                w = men[m][i]
                next_prop[m] = i + 1
                
                if husband[w] == -1:
                    # Accept proposal
                    wife[m] = w
                    husband[w] = m
                    free_men.pop(0)
                    proposed = True
                    break
                else:
                    m_curr = husband[w]
                    # w prefers m over m_curr if rank[w][m] < rank[w][m_curr]
                    if rank[w][m] < rank[w][m_curr]:
                        # Reject m_curr, accept m
                        wife[m_curr] = -1
                        husband[w] = m
                        wife[m] = w
                        free_men.pop(0)
                        free_men.append(m_curr)
                        proposed = True
                        break
            
            if not proposed:
                # No more women to propose (guaranteed not happen)
                free_men.pop(0)
        
        return wife
