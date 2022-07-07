
from fastapi import FastAPI, UploadFile, File
from PIL import Image,ImageFile
from fastapi.responses import JSONResponse
from typing import List
from werkzeug.utils import secure_filename
import logging
import cv2
import os
import shutil
import numpy as np


app= FastAPI()



@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.post("/Upload")
def upload_image(file:UploadFile=File(...)):
    with open(f'{file.filename}',"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
    return {"file_name":file.filename}


@app.post("/Grey_image")
def grey_image(file:UploadFile=File):
    filename=await get_uploaded_file(file)
    img =Image.open(filename)
    imgGray=img.convert('L')
    imgGray.save('Grey_Image.jpg')
    return FileResponse('Grey_Image.jpg')

