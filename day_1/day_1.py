import re

# Read input data
with open("day_1/input.txt", "r") as f:
    lines = f.read().strip().split("\n")

def extract_calibration_value(line: str) -> int:
    digits = re.findall(r'\d', line)
    calibration_string = digits[0] + digits[-1]
    return int(calibration_string)

def extract_calibration_value_pt_2(line: str) -> int:
    numbers = {"one": '1',"two": '2',"three": '3',"four": '4',"five": '5',"six": '6',"seven": '7',"eight": '8',"nine": '9'}
    # Lookahead is necessary to match overlapping numbers, like oneight
    pattern = r'(?=(\d|{}))'.format('|'.join(numbers.keys()))
    digits = re.findall(pattern, line)
    calibration_string = numbers.get(digits[0], digits[0]) + numbers.get(digits[-1], digits[-1])
    return int(calibration_string)

# Part 1
print(f"Part 1: answer is: {sum([extract_calibration_value(line) for line in lines])}")

# Part 2
calibration_value = sum([extract_calibration_value_pt_2(line) for line in lines])
print(f"Part 2: answer is: {calibration_value}")

