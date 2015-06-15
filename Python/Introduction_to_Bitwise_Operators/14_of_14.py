def flip_bit(number, n):
    mask = (0b1 << n-1) # One less than n
    result = number ^ mask
    return bin(result)
