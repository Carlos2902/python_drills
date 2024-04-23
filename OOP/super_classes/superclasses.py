class Employee():
    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name


class Supervisor(Employee):
    def __init__(self, name, last_name, password) -> None:
        super().__init__(name, last_name)
        self.password = password


class Chef(Employee):
    def leave_request(self, days):
        return "may I leave for " + str(days) +  " days?"
    


margaret = Supervisor("Margaret", "Lopez", "apple")

emily = Chef("Emily", "Azu")

print(margaret.password)
print(emily.leave_request(21))