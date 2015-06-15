a = 0b10111011      # 187
mask = 0b100        # 4
desired = a | mask  # 0b10111011 (187), or 0b10111111 (191)
# print a, mask, desired
print bin(desired)
