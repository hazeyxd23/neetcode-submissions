class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r

        while l<=r:
            k=(l+r)//2
            T=0
            for p in piles:
                T+=math.ceil(float(p)/k)
            if T<=h:
                res=k
                r=k-1
            else:
                l=k+1
        return res

