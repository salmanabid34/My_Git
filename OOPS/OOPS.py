class School:
    school="Caset"
    def __init__(self,Eng_Marks,Urdu_Marks,Maths_Maks):
        self.eng_marks=Eng_Marks
        self.urdu_marks=Urdu_Marks
        self.maths_marks=Maths_Maks
    class Salman():  
        def ___init__(self):
            super().__init__()       
        def Printing_Marks(self):      
            print(self.eng_marks,self.urdu_marks,self.maths_marks)
    
        def getschool(cls):        
            return cls.school

s1=School(80,90,100)
s2=School(90,20,50)
s1.Printing_Marks()
print(s1.getschool())