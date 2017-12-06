class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # get symbols
        negative = (denominator*numerator) < 0
        denominator = abs(denominator)
        numerator = abs(numerator)

        result = []
        n_dic = {}  # dic is for checking recurring

        # handle integer part
        if numerator > denominator:
            result.append(str(numerator//denominator))
            numerator = numerator%denominator
            if numerator == 0:
                if negative:
                    result.insert(0, '-')
                return ''.join(result)
        else:
            result.append('0')

        
        if numerator == 0:
            if negative:
                result.insert(0, '-')
            return ''.join(result)
        
        # handle decimal part
        result.append('.')
        while numerator != 0:
            # n_dic saves duplicate positions, then we know where to add '()'
            n_dic[numerator] = len(result)
            result.append(str(10*numerator//denominator))
            numerator = 10*numerator%denominator
            if numerator in n_dic:
                result.insert(n_dic[numerator], '(')
                result.append(')')
                break

        if negative:
            result.insert(0, '-')
        return ''.join(result)
