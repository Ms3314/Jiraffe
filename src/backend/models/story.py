# we are now going to create the db models for the api
from sqlalchemy import Column , JSON , String , Integer , DateTime , Boolean , ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

# some info about DB's

# indexing means that the lookups will be faster but then writes will be slower
# we can set a column to be unique 
# we can also keep required => true by doing nullable=False

class Story():
    __tablename__ = "stories"
    id = Column(Integer ,primary_key=True,index=True)
    title = Column(String , index=True)
    session_id = Column(String)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

    nodes = relationship(argument="StoryNode",back_populates="story")

class Story_nodes():
    __tablename__ = "story_node"
    id = Column(Integer,primary_key=True,index=True)
    story_id = Column(Integer , ForeignKey("stories.id"))   
    content = Column(String)
    is_root = Column(Boolean , default=False)
    is_ending = Column(Boolean , default=False)
    is_ending = Column(Boolean , default=False)
    is_winning = Column(Boolean , default=False)
    options = Column(JSON , default=list)
    
    story = relationship("Story" , back_populates="nodes")