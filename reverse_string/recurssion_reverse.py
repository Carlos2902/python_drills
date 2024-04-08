def reversed_string(str):
    if len(str) == 0:
        return str
    else:
        #slice method [start,end,step]
        return reversed_string(str[1:]) + str[0]
                                        #str[0] apends the first orginal char in string to be the last
    
str = "example"
save_function_value = reversed_string(str);

print(save_function_value)



def recurssion_strings_reverse(word):
    if len(word) == 0:
        return word
    else:
        return recurssion_strings_reverse(word[1:]) + word[0]
    
word = "example";
result = recurssion_strings_reverse(word)

print(result)