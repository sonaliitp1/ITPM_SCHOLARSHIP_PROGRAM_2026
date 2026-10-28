class employee:

    # def __new__(cls,*args):
    #     print("Object Creating",args)
    
    company_name ="ITP"
    @classmethod
    def total_employee(cls):
        return cls.company_name
    

    def __init__(self,eid,ename,city):
        self.eid = eid
        self.ename = ename 
        self.city = city

    def __del__(self):
        print("object deleted :-", self.eid)
        

    def show(self):
       print(f"{self.eid} {self.ename} {self.city} {employee.company_name}")

e1 = employee(101,"ABC","Pune")
e2 = employee(102,"XYZ","MUmbai")
del e2
e3 = employee(103,"PQR","Nashik")

# e1.show()
# e2.show()
# e3.show()

# for i in (e1,e2,e3):
#     i.show()



# Encapsulation --- class --- class members -- access specifiers -- public,private,protected