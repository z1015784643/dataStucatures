
# def twoSum(self, nums: [2,7,11,15], target: 9):
nums=[11,15,2,7,11,15]
target=9
lens = len(nums)
j=-1
for i in range(1,lens):#(1,4)
    print(i)
    temp = nums[:i]#[:1]
    print(temp)
    if (target - nums[i]) in temp:
        print(target,'-',nums[i])
        j = temp.index(target - nums[i])
        print('索引',temp.index(target - nums[i]))
        print(j)
        break
if j>=0:
    print(j,i)

# l=[2,7,11,15]
# print(len(l))
# print(l[:2])