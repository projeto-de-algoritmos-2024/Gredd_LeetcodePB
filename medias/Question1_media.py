class Solution(object):
    def doesValidArrayExist(self, derived):
        n = len(derived)

        def simulate_with_first_value(first_value):
            original = [0] * n
            original[0] = first_value

            
            for i in range(1, n):
                original[i] = derived[i - 1] ^ original[i - 1]

            
            return (original[-1] ^ original[0]) == derived[-1]

       
        return simulate_with_first_value(0) or simulate_with_first_value(1)


solution = Solution()
print(solution.doesValidArrayExist([1, 1, 0]))  
print(solution.doesValidArrayExist([1, 0, 1]))  
