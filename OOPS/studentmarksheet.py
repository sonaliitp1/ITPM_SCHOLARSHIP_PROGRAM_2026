class Result:
    def get_info(self):

        self.sid = 101
        self.sname ="Pranav"
        self.m1 = 67
        self.m2 = 56
        self.m3 = 90
        self.city ="Pune"
        

    def calculate_total(self):
        self.total = self.m1 + self.m2 +self.m3
        self.per = self.total/3 

    def show_info(self):
        print(f"{self.sid} {self.sname} {self.m1} {self.m2} {self.m3} {self.total} {self.per} ")


obj = Result()
obj.get_info()
obj.calculate_total()
obj.show_info()




    

        


    


#student deatils -- sid sname m1 m2 m3 total per 