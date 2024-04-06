employee_id = {
    12343:{
        "id":12343,
        "name": "Jhon",
        "Department": "Kitchen"
    },
    94783:{
        "id":94783,
        "name": "Clio",
        "Department": "Software"
    }

}

def getEmployeInfo(id):
    return employee_id[id];

print(getEmployeInfo(94783));