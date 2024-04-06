#local scope inside a function
# def get_total(a,b):
#     suma = a + b;
#     return suma;
    
# print(get_total(2,2));


# enclosing scope: when a function is nested inside another function
# def get_total(a,b):
#     suma = a + b;

    # def double():
    #     double_it = suma * 2;
    #     print(double_it);
    # double();
#     return suma;

# print(get_total(2,2));

# global scope
special = 5;

def get_total(a,b):
    suma = a + b;
    print("accessing to the global scope val: ",special);
    print("local value: ", suma)


    def double():
            double_it = suma * 2;
            print(double_it);
            double();
get_total(2,2)