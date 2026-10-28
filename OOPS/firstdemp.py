class Student:

    # attributes(instance variable)
  
    def get_data(self): # behavior
        self.sid =1  # instance variable
        self.sname="Rahul"
        self.age=23

    def show_data(self):
        print(f"{self.sid} {self.sname} {self.age}")

    
#creating object 
student1 = Student()

student1.get_data()
student1.show_data()

print(student1.sid)







