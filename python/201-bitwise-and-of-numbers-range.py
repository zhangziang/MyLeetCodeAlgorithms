from math import pow

'''
思路: 将 m 转换为二进制串 s, 检验s中为1的位是否在and操作后仍为1, 因为 m 到 n 为连续的，所以判断 n 是否在某个范围内从而得到结果
'''

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 0:
            return 0

        m_bin = bin(m)[2:]
        m_len = len(m_bin)
        result = 0

        limited_min = ['0' for i in range(m_len)]
        limited_min[0] = '1'
        limited_max = ['1' for i in range(m_len)]

        if n >= pow(2, m_len):
            return result
        else:
            result += int(pow(2, m_len-1))

        for i in range(1, m_len):
            if m_bin[i] == '0':
                limited_max[i] = '0'
            else:
                limited_min[i] = '1'
                min_value = int(''.join(limited_min), 2)
                max_value = int(''.join(limited_max), 2)
                if n>=min_value and n<=max_value:
                    result += int(pow(2, m_len-i-1))

        return result
