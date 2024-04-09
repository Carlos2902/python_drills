def string_reversal(str):
    if len(str)==0:
        return str
    else:
        return string_reversal(str[1:]) + str[0]


str = 'example'
#save the value in a variable:
reverse = string_reversal(str)

print(reverse)
