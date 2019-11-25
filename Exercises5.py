class Employee:
    def __init__(self, empNum, name, address, salary, jobTitle):
        self.empNum = int(empNum)
        self.__name = str(name)
        self.__address = str(address)
        self.__salary = float(salary)
        self.__jobTitle = str(jobTitle)
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.__address
    
    def setAddress(self, Address):
        self.__address = Address
        
    def getSalary(self):
        return self.__salary
    
    def getJobTitle(self):
        return self.__jobTitle
    
    def printInfoH(self):
        print("Employee1 Information: ","Employee Number: ",self.empNum, "Name: ",self.__name, "Address: ", self.__address, "Salary: ", self.__salary, "Job Title ",self.__jobTitle)
        
    def printInfoV(self):
        print("Employee2 Information","\nEmployee Number: ",self.empNum, "\nName: ",self.__name, "\nAddress: ", self.__address, "\nSalary: ", self.__salary, "\nJob Title ",self.__jobTitle)
    
    def __del__( self ):
        print(self.__name+" has been deleted")
        
   
    
Employee1 = Employee(1, "Mohammed Khalid","Amman,Jordan",255,"Consultant")

Employee2 = Employee(2, "Hala Rana","Aqaba,Jordan",750,"Manager")


Employee1.setAddress("USA")

print("===============================================================================")

print("The highlighted formats: ",Employee1.getAddress())

print("===============================================================================")

Employee1.printInfoH()
print("===============================================================================")
Employee2.printInfoV()
print("===============================================================================")
del Employee1
del Employee2