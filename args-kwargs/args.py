# function to sum multiple variables
def sum_multiple(*args):
    sum = 0;
    for x in args:
        sum+=x;
    return sum;

print(sum_multiple(4,5,7,8,6));