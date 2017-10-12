nums=[1, 2, 3]
print(nums)
i=0;
for index in nums:
    k=nums[i]
    k+=1
    nums[i]=k
    i+=1
    
print(nums)

for index in range(1,6):
    print("This is sentence number {} ".format(index))
