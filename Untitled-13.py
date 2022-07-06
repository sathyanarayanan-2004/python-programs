nums = [] 
for i in range(5): 
	num = int(input('Give me a number:')) 
	nums.append(num)
print("The list is:" +str(nums))  
for i in nums: 
	if i % 5 == 0: 
		print(i)