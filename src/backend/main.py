from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

# this is the information about the api 
app = FastAPI(
    title = "Jiraffe",
    description = "api to generate pretty stories",
    version="0.01",
    doc="/doc",
    redoc="/redoc"
)

# this is the major middleware which lets me allow cors origin to everybody
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# running the app using uvicorn and making this only run from the main file only 
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)