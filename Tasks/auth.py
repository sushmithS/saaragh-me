from fastapi import FastAPI
from pydantic import BaseModel
#from typing import Optional
import models


class CreateEmployee(BaseModel):
    first_name: str
    last_name: str
    city: str
    ctc: int
    age:int
    experience: int
    phone_number:int

app=FastAPI()

@app.post("/create/employee")
def create_new_employee(create_employee:CreateEmployee):
    create_new_model=models.new_employee()
    create_new_model.first_name= create_employee.first_name
    create_new_model.last_name = create_employee.last_name
    create_new_model.city = create_employee.city
    create_new_model.mobile = create_employee.mobile
    create_new_model.experience = create_employee.experience
    create_new_model.ctc = create_employee

    return create_new_model()




