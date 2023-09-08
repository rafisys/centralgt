class person:
    name = "harry"
    occupation = "software dev"
    networth = 10
    def info(self):
        print(f"{self.name} os a {self.occupation}")
    
a = person()
# a.name = "shubham"
# a.occupation = "accountant"
# print(a.name, a.occupation)    
a.info()
    