from fastapi import FastAPI, File, HTTPException, UploadFile, HTTPException
from pathlib import Path
import json
from fastapi.responses import RedirectResponse
from deta import Deta  # Import Deta
from services import  deta_put_many #function for inserting amny values into deta_database

# Initialize with a Project Key if you are not working inside a project with Deta sdk installed 
# i.e. deta= Deta('project_key')
deta = Deta()

# Connect to a database named fastapi_file_upload_example_database. 
# Deta will create the database if it does not exist.
deta_database = deta.Base("fastapi_file_upload_example_database")

#initialize fastapi
app= FastAPI()

# create a get endpoint that directs to the project documentation 
@app.get('/', tags=['Documentation'])
def docs():
    # redirect to the project Swagger UI documentation
    return RedirectResponse(url='/docs')


#create a post endpoint:
@app.post("/upload/file", tags=["File Upload Example"],status_code=201)
async def upload_stations(file: UploadFile=File(...)):
    # expects json file types
    content = await file.read()
    file_type=Path(file.filename).suffix
    if file_type != ".json":
        # raise httpexception if the file type is not json
        raise HTTPException(status_code=415, detail=f"Incorrect File type, expected json, got {file_type} file")

    else:
        # do whatever you wish with the file 
        # store the data inside the deta_database
        stations=json.loads(content)
        response= deta_put_many(stations,deta_database)
        return {"filename": file.filename, "filetype": Path(file.filename).suffix, "data":stations[0],
            "contentType":file.content_type}
    