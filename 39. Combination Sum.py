class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # sort the candidates first, and do dfs. Prune the search tree when sum(candidates) > target
        candidates.sort()
        return self.dfs(candidates, target)
        
        
    def dfs(self, candidates, target):
        results = []
        
        for i in range(len(candidates)):
            if target-candidates[i] < 0: # no more combination available
                break
            elif target-candidates[i] == 0: # found, result append [[candidate]]
                results = results + [[candidates[i]]]
            else:
                # get candidate subsets and append current i
                rt = self.dfs(candidates[i:], target-candidates[i])
                results = results + [[candidates[i]]+sub_rt for sub_rt in rt]
            
        return results
        