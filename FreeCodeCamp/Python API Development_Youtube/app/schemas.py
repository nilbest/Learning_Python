from pydantic import BaseModel

#Schema of the BaseModel by pydabtic  
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    #rating: Optional[int] = None
    
class PostCreate(PostBase):
    pass
