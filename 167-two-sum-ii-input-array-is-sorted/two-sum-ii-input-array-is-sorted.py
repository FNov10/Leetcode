class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers)-1
        while L<R:
            summ = numbers[L] + numbers[R]
            if summ == target:
                return [L+1, R+1]
            if summ>target:
                R-=1
            else:
                L+=1
        
            
        