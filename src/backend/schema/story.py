# these are the type of data 
# to check what type of data is comign to the system 

from typing import List , Optional , Dict
from datetime import datetime
from pydantic import BaseModel

class StoryOptionsSchema(BaseModel):
    node_id : Optional[int] = None
    text : str

class StoryNodeBase(BaseModel):
    content : str 
    is_ending : bool = False
    is_winning_ending : bool = False 
    
  # response from the api  
  # the story can have some certain options and the options can be of the type storyOptionSchema 
class CompleteStoryNodeResponse(StoryNodeBase):
    id : int 
    options : List[StoryOptionsSchema] = []
    
    class Config:
        from_attributes = True
        
class StoryBase(BaseModel):
    title : str
    session_id : Optional[str] = None
    
    class Config:
        from_attributes = True

class CreateStoryRequest(BaseModel):
    theme : str

# this is the complete story Response     
class CompleteStoryResponse(StoryBase):
    id : int 
    created_at : datetime
    root_node : CompleteStoryNodeResponse
    all_nodes : Dict[int,CompleteStoryNodeResponse]
    
    class Config:
        from_attributes = True