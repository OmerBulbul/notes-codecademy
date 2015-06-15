check_bit4(input):
    mask = 0b1000
    input = input & mask
    if input > 0:
        return "on"
    else:
        return "off"

# Test the function
check_bit4(0b1) # ==> "off"
check_bit4(0b11011) # ==> "on"
check_bit4(0b1010) # ==> "on"
