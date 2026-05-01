class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        n = len(numbers)
        output = []
        while i<n:
            x = target - numbers[i]
            if x in numbers and numbers.index(x)!=i:
                ind = numbers.index(x)
                output = [ind+1, i+1]
                output.sort()
            i+=1
        return output
            


        