from sqlalchemy.orm import Session
from models import Quote, Author
from schemas import QuoteCreate, AuthorCreate
from fastapi import HTTPException

def get_quotes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Quote).offset(skip).limit(limit).all()

def get_quote_by_id(db: Session, quote_id: int):
    return db.query(Quote).filter(Quote.id == quote_id).first()
    
    

def create_quote(db: Session, quote: QuoteCreate):
    db_quote = Quote(**quote.dict())
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote
    

def update_quote(db: Session, quote_id: int, quote: QuoteCreate):
    db_quote = db.query(Quote).filter(Quote.id == quote_id).first()
    db_quote.text = quote.text
    db_quote.author = quote.author
    db_quote.tags = quote.tags
    db_quote.source = quote.source
    db.commit()
    db.refresh(db_quote)
    return db_quote

def delete_quote(db: Session, quote_id: int):
    db_quote = db.query(Quote).filter(Quote.id == quote_id).first()
    db.delete(db_quote)
    db.commit()
    return db_quote

def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Author).offset(skip).limit(limit).all()

def get_author_by_id(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()     

def create_author(db: Session, author: AuthorCreate):
    db_author = Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author