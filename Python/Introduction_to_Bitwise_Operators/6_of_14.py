shift_right = 0b1100
shift_left = 0b1

# Your code here!
# shift_right >> 2 == 0b11
# shift_left << 2 == 0b100
shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)  # ==> 0b11 (3)
print bin(shift_left)   # ==> 0b100 (4)
