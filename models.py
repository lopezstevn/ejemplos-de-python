class User:
    name=None
    email=None
    def send_email(self):
        if self.email is not None:
            print("sendingemail"+self.email)
        else:
            print("error")

    def __init__(self,name,email):
        self.name=name
        self.email=email
    def __str__(self):
        return "User: " + self.email
        
class Student(User):
    id =None
    def __init__(self,
       name=None,
       email=None,
       id= None,
       score=None,
       ):
#constructor de la clase init
       super().__init__(name,email)
       self.id= id
       self.score=score
    def __str__(self):
        return "Student:"+str(self.id)+","+self.email
    def __repr__(self):
        return f"Student(name='{self.name}',email='{self.email}', id='{self.id}')"
 


