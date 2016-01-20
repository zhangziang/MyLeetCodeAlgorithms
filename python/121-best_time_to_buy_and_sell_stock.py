# 题目是求差值最高的一段。该方法求每一个数(第二个数起)作为最大值结尾得到的结果，在所有结果中选最大值即为最终结果。

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        array_len = len(prices)
        if array_len<2:
            return 0
        d_min = prices[0]
        result = 0
        for i in range(1, array_len):
            gap = prices[i] - d_min
            if gap > result:
                result = gap
            if prices[i] < d_min:
                d_min = prices[i]
        return result
