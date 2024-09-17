from fastapi import APIRouter,Depends,HTTPException, UploadFile
import api.schemas as schemas
from api.crud import files_crud

router = APIRouter(
    prefix="/upload",
    tags=["upload"],
)

# , response_model=schemas.File
@router.post("/", description="Upload file to AWS, and return https link")
def upload_file(file:UploadFile):
    return files_crud.FileRelay.upload_file(file = file)