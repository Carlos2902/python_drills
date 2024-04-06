bill_total = 201;

discount1 = 10;
discount2 = 20;

if bill_total > 100 and bill_total<200 :
        print("Bill total is grater than 100 but less than 200");
elif bill_total > 200 :
        print("Bill total is grater than 200, with the discount will be: " + str((bill_total-discount2)));
else :
        print("Im an else");