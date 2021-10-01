class Solution:
    # log(n)
    @classmethod
    def isPowerOfTwoSolution1(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

    # log(1)
    @classmethod
    def isPowerOfTwoSolution2(self, n: int) -> bool:
        if n == 0:
            return False
        return (n & -n) == n
    
if __name__ == "__main__":
    test_cases = [1, -4, 6, 7, 12380, 0, -123]
    test_results = [True, True, False, False, False, False, False]
    
    if len(test_cases) == len(test_results):
        for i, (test_case, test_result) in enumerate(zip(test_cases, test_results)):
            print(f"Test case {i}:")
            
            print("Solution 1:")
            print("\tpassed") if (Solution.isPowerOfTwoSolution1(test_case) == test_result) else print("\tfailed")
            
            print("Solution 2:")
            print("\tpassed") if (Solution.isPowerOfTwoSolution2(test_case) == test_result) else print("\tfailed")
            
    else:
        raise Exception("The number of test cases doesn't match the number of test results.")
    