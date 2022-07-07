from fastapi import FastAPI, UploadFile, File
from PIL import Image,ImageFile
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
from typing import List
from werkzeug.utils import secure_filename
import logging
import cv2
import os
import shutil
import numpy as np


app= FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s'
    )
logger=logging.getLogger()

async def get_uploaded_file(file):
    logger.info("File Uploading ...")
    try:
        filename = secure_filename(file.filename)
        with open(filename,"wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        logger.info(f"filename:{filename}")
    except:
        filename == ''
        logger.error("No file selected for uploading.")
        resp=JSONResponse(content={'error_msg':'no file selected for uploading'})
        resp.status_code=200
        return resp
    return filename


@app.post("/Upload")
def upload_image(file:UploadFile=File(...)):
    with open(f'{file.filename}',"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
    return {"file_name":file.filename}


@app.post("/grey_file/")
async def create_upload_file(file:UploadFile):
    filename= await get_uploaded_file(file)
    img = Image.open(filename)
    imgGray =img.convert('L')
    imgGray.save('test_gray.jpg')
    return FileResponse("test_gray.jpg")

