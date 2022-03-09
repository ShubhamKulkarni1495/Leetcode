class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a= sorted(score, reverse=True)
        b={}
        c=[]
        print(a)
        for i in range(len(a)):
            if i == 0:
                b[a[i]] = "Gold Medal"
            elif i == 1:
                b[a[i]] = "Silver Medal"
            elif i == 2:
                b[a[i]] = "Bronze Medal"
            else:
                b[a[i]] = str(i+1)
        for i in score:
            c.append(b[i])
        return c