

nums = [1,2,1,4,5]

good_pairs = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if(nums[i] == nums[j]):
            good_pairs += 1
print(good_pairs) 


