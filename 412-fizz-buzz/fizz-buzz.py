class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [self.fizzMatch(index+1) for index in range(n)]
                
    def fizzMatch(self, number: int) -> str:
        if all([number%3==0,number%5==0]):
            return "FizzBuzz"
        elif number%3==0:
            return "Fizz"
        elif number%5==0:
            return "Buzz"
        else: return f"{number}"