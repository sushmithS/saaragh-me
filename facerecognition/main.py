import os
import cv2
from fastapi import FastAPI,UploadFile, File,responses
#responses -for getting image as response
from deta import Drive
from fastapi.responses import FileResponse
app=FastAPI()
path= "/saaragh_sushmithAPI/facerecognition"
#deta=Deta("")#configure your deta project
#drive=deta.Drive("images")#acess to your drive


@app.get("/")
def index():
    return {"hello"}

@app.get("/hp")
def hp():
    return FileResponse("HP.jpg")

@app.get("/hp/Grey_scale")
def grey_image():
    for image in grey_image():
        grey_image=cv2.cvtColor("HP.jpg", cv2.COLOR_BGR2GRAY)
    return grey_image

#@app.get("/hp_and etc")
#def HP():
   #file_path=os.path.join(path,"saaragh_sushmithAPI/facerecognition/HP.jpg")
   # if os.path.exists(file_path):
   #     return FileResponse(file_path)
  #  return {"error":"file not found "}

#@app.post("/single_image")
#def image(file: UploadFile = File(...)):
 #   return files.put(file.filename,file.file)

#@app.get("/")
#def list_files():
  #  return files.list()
#
#@app.get("/{name}")
#def serve(name):
   # img=files.get(name)
    #ext =name.split(".")[1]
   # return responses.StreamingResponse(img.iter_chunks(),media_type=f"images/{ext}")
