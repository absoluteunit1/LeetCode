
# My first solution; using brute force. O(n**2). However, the question asks that this problem is solved in O(n).

def productExceptSelf(nums):
    product = 0
    list_of_products = []
    i = 0

    while(i < len(nums)):
        nums2 = nums[:i] + nums[i+1:]
        product = nums2[0]
        for j in range(1, len(nums2)):
            product *= nums2[j]
        list_of_products.append(product)
        i += 1

    return list_of_products


# My second solution; an extended list. Still exceeds time limit. 17/18 passed

def productExceptSelf2(nums):
    long_list = []
    final_list = []

    max_count = len(nums) - 1
    count = 1
    num = 1

    for i in range(len(nums)):
        long_list += nums[:i] + nums[i+1:]

    for i in range(len(long_list)):
        num *= long_list[i]

        if count == max_count:
            final_list.append(num)
            num = 1
            count = 1
        else:
            count += 1

    return final_list

# Most optimal solution 

def productExceptSelf3(nums):
    ans = [1 for _ in nums]
            
    left = 1
    right = 1
    
    for i in range(len(nums)):
        ans[i] *= left
        ans[-1-i] *= right
        left *= nums[i]
        right *= nums[-1-i]
    
    return ans