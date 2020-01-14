digits = [0, 1, 1, 2, 3, 5, 7, 12]  # define a list

for i in range(len(digits)):  # for int i = 0; i < digits.length; i++
    print(digits[0:i])  # print from 0 to i

window = 4
for i in range(len(digits) - (window - 1)):
    print(digits[i: i + window]) # need to fix last 2 cases, prints last two and then last one
