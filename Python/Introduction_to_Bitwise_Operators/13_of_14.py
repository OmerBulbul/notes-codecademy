a = 0b11101110      # 238
mask = 0b11111111   # 255 
desired = a ^ mask  # 0b10001 (17)
print bin(desired)
