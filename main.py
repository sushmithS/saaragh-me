
from fastapi import FastAPI, Depends
from sqlalchemy.orm import sessionmaker
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db= SessionLocal()
        yield db
    finally:
        db.close()

#get method
#@app.get("/")
#def just_start():
   # return {"message is":'Hello World'}

@app.get("/")
def read_employees(db:Session=Depends(get_db)):
    return db.query(models.Emp).all()

@app.get("/Emp/{emp_id}")
def read_emp(emp_id: int,db:Session = Depends(get_db)):
    emp_model = db.query(models.Emp)\
        .filter(models.Emp.id == emp_id)\
        .first()
    if emp_model is not None:
        return emp_model
    raise HTTPException(status_code=404,detail="Emp not found")




