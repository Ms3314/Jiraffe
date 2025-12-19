# this is where we write our end points 
import uuid 
from typing import Optional
from datetime import datetime
from fastapi import APIRouter , Depends , HTTPException , Cookie , Response , BackgroundTasks
from sqlalchemy.orm import Session

# from backend.db.database import get_db , sessionLocal
# from models.story import 
from backend.schema.job import StoryJobResponse 
from backend.schema.job import StoryJobCreate , StoryJobStatusResponse , StoryJobResponse , StoryJobStatusRequest
from backend.schema.story import CreateStoryRequest , CompleteStoryResponse
from backend.db.database import sessionLocal # ?? idk what this does
from backend.db.database import get_db

# from backend.models.story import 
from backend.models.job import StoryJob

router = APIRouter(
    prefix="/stories",
    tags=["stories"]
)

# we get the session id from here
def get_session_id(session_id : Optional[str] = Cookie(None)):
    if not session_id: #agar session id nahi hai toh 
        session_id = str(uuid.uuid4()) #so we are assigning the session id 
    return session_id # return session_id if no session id exists


# /api/stories
# this route will create a job now 
@router.post("/create" , response_model=StoryJobResponse)
def create_story(
    request :  CreateStoryRequest,
    background_tasks : BackgroundTasks,
    response : Response , 
    session_id : str = Depends(get_session_id),
    db : Session = Depends(get_db)
):
    # ook so we need to create a story 
    # for that we need to give the story creation request 
    # it will give us the response for the job status
    response.set_cookie(key="session_id",value=session_id , httponly=True)
    job_id = str(uuid.uuid4())
    
    # we initialize the job first ig
    job = StoryJob(
        job_id=job_id,
        session_id=session_id, # what is this used for ??
        theme=request.theme,
        status="pending"
    )
    db.add(job)
    db.commit() # adding the job pending state
    
    # need to add background tasks and generate story
    background_tasks.add_task(
        # the story will be generate in the background
        generate_story_task ,
        job_id=job_id ,
        theme=request.theme,
        session_id=session_id
    )
    
    return job
    
    # pass
      
      
def generate_story_task(job_id:str , theme:str , session_id:str):
    # this function will generate a story 
    # here comes the real story generation logic 
    db = get_db() #?? why cant i just do this ?? will this initalize a new db instance or someting 
    # nvm it does the same thing 
    try:
        job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()
        # we need to get the row which has the id of the given id 
        if not job:
            return 
        try :
            job.staus = "processing"
            db.commit()
            
            story = {} # we need to generate the story
            
            job.story_id = 1 # ?? why is this id 1  
            job.status = "completed"
            job.completed_at = datetime.now()
            db.commit()
                
        except Exception as e:
            job.status = "failed" 
            job.completed_at = datetime.now()
            job.error = str(e)
            db.commit()
            pass
    finally:
        db.close()
    

@router.get("/{story_id}/status" , response_class=StoryJobStatusResponse)
def get_job_status(
    request :  StoryJobStatusRequest,
    background_tasks : BackgroundTasks,
    response : Response , 
    db : Session = Depends(get_db)
):
    # I want to get the id 
    # then i will search in the db for the status of the job of that id 
    job = db.query(StoryJob).filter(
        StoryJob.job_id == request.job_id , 
    ).first()
    return {
        "job_id" : job.job_id ,
        "status" : job.status
    }

# not alot of idea maybe if it is completed then only 
@router.get("/{story_id}/complete" , response_model=)
    