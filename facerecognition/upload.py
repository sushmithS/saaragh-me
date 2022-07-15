from fastapi import FastAPI, UploadFile, File
from PIL import Image,ImageFile
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
from typing import List
from werkzeug.utils import secure_filename
import logging
import sys
import cv2
import os
import aiofiles
import shutil #used to save the file


app= FastAPI()
sys.setrecursionlimit(1500)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s'
    )
logger=logging.getLogger()

async def get_uploaded_file(file):
  logger.info("File Uploading ...")
  try:
    filename = secure_filename(file.filename)
    with open(filename, "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
    logger.info(f"filename:{filename}")
  except:
    filename == ''
    logger.error("No file selected for uploading.")
    resp = JSONResponse(content={'error_msg': 'no file selected for uploading'})
    resp.status_code = 200
    return resp
  return filename



#single image_Color
@app.post("/Upload_single_clour")
async def upload_image(file:UploadFile=File(...)):
    with open(f'{file.filename}',"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
    return FileResponse(file.filename)


#single_image_Grey
@app.post("/single_grey")
async def create_upload_file(file:UploadFile):
    filename= await get_uploaded_file(file)
    img = Image.open(filename)
    imgGray =img.convert('L')
    imgGray.save('grey1.jpg')
    return FileResponse("grey1.jpg")

#double images
@app.post("/multi_clour")
async def double_image(files: List[UploadFile] = File(...)):
    for Images in files:
        with open(Images.filename, "wb") as buffer:
            shutil.copyfileobj(Images.file, buffer)
    return files

#double images grey
@app.post("/multi_grey")
async def multi_grey_images(file:List[UploadFile]):
    filename= await get_uploaded_file(file)
    img = Image.open(filename)
    img.convert("L").save("grey_result.jpg")
    return img("grey_result.jpg")

