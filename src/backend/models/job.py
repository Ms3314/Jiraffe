# this represents as the status of the creation of the story
from sqlalchemy import Column , JSON , String , Integer , DateTime , Boolean , ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class StoryJob():
    __tablename__ = "story_jobs"
    
    id = Column(Integer,index=True,primary_key=True)
    job_id = Column(String , index=True , unique=True )
    session_id = Column(String , index=True)
    theme = Column(String)
    status = Column(String)
    story_id = Column(String , nullable=True)
    error = Column(String , nullable=True)
    created_at = Column(DateTime(timezone=True) , server_default=func.now())
    completed_at = Column(DateTime(timezone=True) , server_default=func.now() , nullable=True)