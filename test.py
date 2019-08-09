nums = [4,9,6,7,9,6]
b = 0
c = 0
for num in nums:
    if c > nums.count(num): 
        b = b
    else:
        b = num

print(b)