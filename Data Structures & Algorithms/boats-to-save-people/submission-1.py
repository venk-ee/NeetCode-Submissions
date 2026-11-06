class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)-1
        ans=0
        people.sort()
        
        heviest=n
        lighest=0
        while lighest<=heviest:
            weight=people[lighest]+people[heviest]
            if weight <=limit:
                ans+=1
                heviest-=1
                lighest+=1
            elif people[heviest] <=limit:
                ans+=1
                heviest-=1
            else:
                lighest+=1
            
        return ans

            

