# amstrong of a number
def is_asmtrong(num):
    num_str = str(num)
    n = len(num_str)
    digit_sum = sum(int(digit) ** n for digit in num_str)
    return digit_sum == num
