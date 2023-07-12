arr=list(map(int,input("Enter the Array elements:").split()))
class Equality:
    @staticmethod
    def time_to_equality(arr):
        max_element = 0
        for i in arr:
            if i>max_element:
                max_element =i
        count=0
        for j in arr:
            diff=max_element-j
            count+=diff
        return count
obj = Equality()
print(obj.time_to_equality(arr))
