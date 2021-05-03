nums = []
def collatz_conjecture(num):
    while num!=1:    
        if num%2==0:
            num/=2
        else:
            num=num*3+1
        nums.append(num)
    return nums
num = int(input())
print(collatz_conjecture(num))
