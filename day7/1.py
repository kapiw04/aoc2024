with open("example") as f:
    equations = f.readlines()

equations = [(equation.split(":")[0], equation.split(":")[1]) for equation in equations]

def check_valid(res, nums):
    if len(nums) == 1:
        return res == nums[0]
             
    if res % nums[-1] == 0:
        if check_valid(res // nums[-1], nums[:-1]):
            return True    
    
    return check_valid(res - nums[-1], nums[:-1])

total_calibration_result = 0

for equation in equations:
    res, nums = int(equation[0]), list(map(int, equation[1].strip().split(" ")))
    if check_valid(res, nums):
        total_calibration_result += res

print(total_calibration_result)