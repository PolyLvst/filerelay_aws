from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi import FastAPI
import api.dependencies as dependencies
from api.routers import files

load_dotenv()
title = dependencies.get_settings().app_name
version = dependencies.get_settings().version
app = FastAPI(title=title,version=version)

# Jika frontend berada di domain berbeda
origins = [
    "http://*.localhost.com",
    "http://localhost",
    "localhost:8000",
    "http://localhost:8000",
    "http://localhost:8008",
    "http://domain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # Cookies etc ...
    allow_methods=["*"], # GET POST etc ...
    allow_headers=["*"], # Accept, Accept-Language, Content-Language etc ...
)

# ----------- API END POINT ------------- #
# ... Files ...
app.include_router(files.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)