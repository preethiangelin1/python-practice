def sum_of_elements(nums):
    total = 0
    
    if not type(nums) == list:
        return total
    
    for num in nums:
        total = total + num
    
    return total

def count_even_numbers(nums):
    total_even_num = 0
    for num in nums:
        if num % 2 == 0:
            total_even_num += 1
    return total_even_num

def find_maximum_number(nums):
    if len(nums) == 0 or type(nums) != list:
        return
    
    largest_number = nums[0]
    for num in nums:
        if num > largest_number:
            largest_number = num
    return largest_number
