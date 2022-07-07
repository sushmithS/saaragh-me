from fastapi import FastAPI, Depends, HTTPException
#depends only when you get data from db
import models
from database import engine
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
@app.get("/")
async def task_1():
    return {"Hello World"}

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
    Mobile : str
    experience : int

#to fetch data which you created in Database
@app.get("/emp_details")
async def read_all(db:Session= Depends(get_db)):
   return db.query(models.Emp).all()

@app.get("/Emp/{emp_id}")
async def read_emp(emp_id:int,db:Session=Depends(get_db)):
    #emp_model is the varible assigned
    emp_model=db.query(models.Emp)\
        .filter(models.Emp.emp_id==emp_id)\
        .first()

    if emp_model is not None:
        return emp_model
    raise HTTPException(404, "Emp not found")
    #.filter-allows us to filter your sqlitecommnad to navigate with the records of the table

#task2,{emp_id: str},Emp:Emp
@app.post("/")
async def read_emp_data(first_name: str,last_name:str,city:str,experience:int,CTC:int,age:int,contact:int,Emp:Emp, db:Session=Depends(get_db)):
    emp_model = models.Emp()
    emp_model.f_name = Emp.f_name
    emp_model.L_name = Emp.l_name
    emp_model.city = Emp.city
    emp_model.emp_age = Emp.emp_age
    emp_model.Mobile = Emp.Mobile
    emp_model.Experience = Emp.experience
    emp_model.ctc = Emp.ctc
    db.add(emp_model)
    db.commit()

    return {
       'status': 201,
       'created': 'successful'
    }

#postmethod to get emp
@app.post("/emp_id")
async def create_emp(Emp:Emp,db:Session=Depends(get_db)):
    emp_model = models.Emp()
    emp_model.f_name= Emp.f_name
    emp_model.L_name = Emp.l_name
    emp_model.city = Emp.city
    emp_model.emp_age=Emp.emp_age
    emp_model.Mobile = Emp.Mobile
    emp_model.Experience = Emp.experience
    emp_model.ctc = Emp.ctc
    db.add(emp_model)
    db.commit()
    return {
        'status':201,
        'created':'successful'
    }


@app.put("/Emp/{emp_id_update}")
async def update_emp(emp_id: int, Emp: Emp, db: Session=Depends(get_db)):
    emp_model = db.query(models.Emp) \
        .filter(models.Emp.emp_id == emp_id) \
        .first()
    if emp_model is None:
        raise HTTPException(404, "Emp not found")
    #emp_model = models.Emp()
    emp_model.f_name = Emp.f_name
    emp_model.L_name = Emp.l_name
    emp_model.city = Emp.city
    emp_model.emp_age = Emp.emp_age
    emp_model.Mobile = Emp.Mobile
    emp_model.Experience = Emp.experience
    emp_model.ctc = Emp.ctc
    db.add(emp_model)
    db.commit()
    return {
        'status': 200,
        'created': 'successful'
    }

@app.delete('/{emp_id}')
async def delete_emp(emp_id:int, db:Session= Depends(get_db)):
    emp_model = db.query(models.Emp)\
        .filter(models.Emp.emp_id == emp_id)\
        .first()
    if emp_model is None:
        raise HTTPException(404, "Emp not found")
    db.query(models.Emp)\
        .filter(models.Emp.emp_id == emp_id)\
        .delete()
    db.commit()
    return {
        'status': 201,
        'created': 'successful'
    }



