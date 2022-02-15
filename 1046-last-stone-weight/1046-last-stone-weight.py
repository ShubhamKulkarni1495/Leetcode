class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            a = max(stones)
            stones.remove(a)
            b = max(stones)
            stones.remove(b)
            if a == b:
                pass
            else:
                c = a - b
                stones.append(c)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
