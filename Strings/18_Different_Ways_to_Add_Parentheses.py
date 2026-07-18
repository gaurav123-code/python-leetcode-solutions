class Solution:
    def diffWaysToCompute(self, expression):
       
        if expression.isdigit():
            return [int(expression)]
            
        results = []
        
        for i in range(len(expression)):
            char = expression[i]
            
            
            if char == '+' or char == '-' or char == '*':
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                
                
                for left in left_results:
                    for right in right_results:
                        if char == '+':
                            results.append(left + right)
                        elif char == '-':
                            results.append(left - right)
                        elif char == '*':
                            results.append(left * right)
                            
        return results

print(Solution().diffWaysToCompute("2-1-1"))