to_21 = range(1,22)
odds = []
middle_third = []
for i in to_21:
    odds = to_21[::2]
    middle_third = to_21[len(to_21)*1/3:len(to_21)*2/3:]
print odds
print middle_third
