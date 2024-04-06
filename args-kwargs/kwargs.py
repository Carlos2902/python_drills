# almost the same as args, but kwargs have the ability to acces to a given key value and manipulating them
# function to sum multiple variables


def sum_multiple(**kwargs):
    sum = 0;
    for key, value in kwargs.items():
        sum+=value;
    return sum;

print(sum_multiple(cofee=2, sandia=4));