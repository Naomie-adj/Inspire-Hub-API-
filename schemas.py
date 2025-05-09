from pydantic import BaseModel
from typing import List, Optional

class Quote(BaseModel):
    id: int
    text: str
    author: str 
    tags:str
    source:str

class Author(BaseModel):
    id: int
    first_name: str
    last_name: str
    bio: str
    quotes: List[Quote] = []  

class QuoteCreate(BaseModel):
    text: str 
    author: str
    tags:str
    source:str

class AuthorCreate(BaseModel):   
    first_name: str
    last_name: str
    bio: str 

class QuoteUpdate(BaseModel):
    text: Optional[str]
    author: Optional[str]
    tags: Optional[str]
    source: Optional[str]

class AuthorUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    bio: Optional[str]    


    
