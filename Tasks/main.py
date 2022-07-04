from fastapi import FastAPI, Depends, HTTPException
#depends only when you get data from db
import models
from database import engine
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from pydantic import BaseModel, Field


app =FastAPI()

models.Base.metadata.create_all(bind=engine)
#emp_data = {"first_name": input("enter your first name : "),
                   #  "last_name": input("enter your last name : "),
                   #  "employe_id": "A2022:001",
                    # "city": input("enter the city : "),
                    # "experience": int(input("enter the experience in months : ")),
                    # "ctc": int(input("enter your ctc : ")),
                    # "age": int(input("enter the age : ")),
                    # "contact_no": int(input("enter the contact number : "))
                    # }


#Task1
#@app.get("/")
#def task_1():
    #return {"Hello World"}

#to fetch data which you created in Database
def get_db():
    try:
        db= SessionLocal()
        yield db
    finally:
        db.close()

class Emp(BaseModel):
    ctc:int
    f_name :str
    l_name :str
    city:str
    emp_age: int
    Mobibe : str
    experience : int

#to fetch data which you created in Database
@app.get("/")
async def read_all(db:Session= Depends(get_db)):
   return db.query(models.Emp).all()

@app.get("/Emp/{emp_id}")
async def read_Emp(emp_id:int,db:Session=Depends(get_db)):
    #emp_model is the varible assigned
    emp_model=db.query(models.Emp)\
        .filter(models.Emp.emp_id==emp_id)\
        .first()
    if emp_model is not None:
        return emp_model
    raise HTTPException(404, "Emp not found")
    #.filter-allows us to filter your sqlitecommnad to navigate with the records of the table

#postmethod to get emp
@app.post("/")
async def create_emp(Emp:Emp,db:Session=Depends(get_db)):
    emp_model=models.Emp()
    emp_model = models.Emp()
    emp_model.f_name= Emp.f_name
    emp_model.L_name = Emp.l_name
    emp_model.city = Emp.city
    emp_model.emp_age=Emp.emp_age
    emp_model.Mobile = Emp.Mobibe
    emp_model.Experience = Emp.experience
    emp_model.ctc = Emp.ctc
    db.add(emp_model)
    db.commit()
    return {
        'status':201,
        'created':'successful'
    }

#task2
#@app.post("/")
#def read_Emp_data(first_name: str,last_name:str,emp_id: str,city:str,experience:int,CTC:int,age:int,contact:int):
    #return (first_name,last_name,emp_id,city,experience,CTC,age,contact)



#@app.post("/task2/create/employee")
#def create_new_employee(create_employee:CreateEmployee):
    #create_new_model=models.new_employee()
    #create_new_model.first_name= create_employee.first_name
    #create_new_model.last_name = create_employee.last_name
    #create_new_model.city = create_employee.city
   # create_new_model.mobile = create_employee.mobile
   # create_new_model.experience = create_employee.experience
   # create_new_model.ctc = create_employee

    #return create_new_model