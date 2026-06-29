class Solution:
    def isValid(self, s: str) -> bool:
        map_par={')':'(','}':'{',']':'['}

        stack=[]

        for c in s:
            if c not in map_par:
                stack.append(c)
            else:
                if not  stack:
                    return False
                else:
                    poped=stack.pop()
                    if poped!=map_par[c]:
                        return False
        
        return not stack
