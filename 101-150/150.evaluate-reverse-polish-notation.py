class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        i = 0
        while len(tokens) > 1:
            if tokens[i] == '+':
                tokens[i-2] = int(tokens[i-2])+int(tokens[i-1])
                tokens.pop(i)
            	tokens.pop(i-1)
            	i = i-2
            elif tokens[i] == '-':
                tokens[i-2] = int(tokens[i-2])-int(tokens[i-1])
                tokens.pop(i)
            	tokens.pop(i-1)
            	i = i-2
            elif tokens[i] == '*':
                tokens[i-2] = int(tokens[i-2])*int(tokens[i-1])
                tokens.pop(i)
            	tokens.pop(i-1)
            	i = i-2
            elif tokens[i] == '/':
                tokens[i-2] = abs(int(tokens[i-2]))//abs(int(tokens[i-1]))
                if int(tokens[i-2])*int(tokens[i-1]) < 0:
                	tokens[i-2] = -tokens[i-2]
                tokens.pop(i)
            	tokens.pop(i-1)
            	i = i-2
            else:
            	i += 1
        
        return int(tokens[0])
