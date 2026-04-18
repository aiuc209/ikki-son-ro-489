def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def find_lcm_pairs(nums):
    lcm_pairs = []
    for i in range(0, len(nums), 2):
        if i + 1 < len(nums):
            lcm_pairs.append(lcm(nums[i], nums[i+1]))
    return lcm_pairs

nums = [2, 7, 3, 9, 4, 6]
print(find_lcm_pairs(nums))
