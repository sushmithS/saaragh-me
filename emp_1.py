from fastapi import FastAPI

app = FastAPI()
#get method
@app.get("/")
def just_start():
    return {"message is":'Hello World'}


#post method
@app.post("/")
def create_emp_1(first_name:str,last_name:str,experience_in_months:int,city:str,CTC:int,emp_age:str,Contact_no:str,):
    return {first_name,last_name,experience_in_months,city,CTC, emp_age,Contact_no}


#empoyee id - (should be generated - first employee -- A2022-001, next employee - A2022-002 - this should happen automatically) - you should NOT get from user

