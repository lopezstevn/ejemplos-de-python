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
per1 =User("lopez","21182@utsc.edu.mx")
per1.send_email()

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
    {}
    #definir si es aprovado con true o false metodo (b0ol) 
    def is_approved(self):
        if self.score is not None:
            return self.score >=8
        

dict1 = dict()
for i,uuid_str in enumerate(list1):
    dict1[uuid_str]= Student(
        name="student"+str (i),
        email="email"+str(i)+"@ust",
        id=uuid_str
        )

student_score1=Student(
    name ="Esteban",
    email="21182@virtual.utsc.edu.mx",
    id=uuid.uuid4(),
    score=random.randint(6,10),
 )
db=dict()
for i in range(10):
    id=uuid.uuid4()
    db[str(id)]=Student(
        id=id,
        name="Nombre_"+str(i),
        email="correo_"+str(i)+"@email.com",
        score= random. randint(6,10),
    )
print(db)
