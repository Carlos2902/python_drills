def ispresent(person):
    names = ["Al", "Mo", "Ba"]
    if person in names:
        return True 
    else:
        return False
    

def nondigit(person):
    if person.isalpha():
        return True
    else:
        return False