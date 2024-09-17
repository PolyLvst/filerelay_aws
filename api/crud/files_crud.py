from fastapi import UploadFile,HTTPException,status
import api.dependencies as dependencies

# ... EDP ...
class FileRelay:
    def upload_file(file: UploadFile) -> dict:
        link = dependencies.aws_upload_file(file_obj=file.file,filename=file.filename)
        return {"link":link}