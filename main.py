from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import requests
import jwt
from datetime import datetime, timedelta 
from sqlalchemy.orm import Session
from schemas import Quote, Author
import json
import random



app = FastAPI(
    title="Inspire Hub API",
    description="API for managing inspiring quotes and authors",
    version="1.0.0"
)


db_quotes: List[Quote] = [
    
        Quote( 
        id=1,
        author= "Albert Einstein",  
        source= "https://en.wikiquote.org/wiki/Albert_Einstein",
        tags= "intelligence, knowledge, simplicity, understanding",
        text= "If you can't explain it simply, you don't understand it well enough."
        ),  

        Quote(  
        id=2,
        author= "Albert Gray",
        source= "https://www.goodreads.com/quotes/524224",
        tags= "winners, habit, losers",
        text= "Winners have simply formed the habit of doing things losers don't like to do."
        ),

        Quote(
        id=3,
        author= "Annie Dillard",
        source= "https://www.goodreads.com/quotes/530337",
        tags= "passion, try, live",
        text= "How we spend our days is, of course, how we spend our lives."
        ),

        Quote(
        id=4,
        author= "Arianna Huffington",
        source= "https://quotefancy.com/quote/1246163",
        tags= "Sleep, Ideas",
        text= "Discover the great ideas that lie inside you by discovering the power of sleep."
        ),

        Quote(
        id=5,
        author= "Aristotle",    
        source= "https://www.goodreads.com/quotes/1309500",
        tags= "Criticism",
        text= "Criticism is something you can easily avoid by saying nothing, doing nothing, and being nothing."
        ),

        Quote(
        id=6,
        author= "Benjamin Franklin",
        source= "https://www.goodreads.com/quotes/1332",
        tags= "future, success, plan",
        text= "By failing to prepare, you are preparing to fail."
        ),

        Quote(
        id=7,
        author= "Bill Gates",
        source= "https://www.goodreads.com/quotes/323288",
        tags= "inspirational",
        text= "Success is a lousy teacher. It seduces smart people into thinking they can't lose."
        ),

        Quote(
        id=8,
        author= "Brian Tracy",
        source= "https://www.goodreads.com/quotes/28134",
        tags= "future, inner power",
        text= "You have within you, right now, everything you need to deal with whatever the world can throw at you."
        ),

        Quote(
        id=9,
        author= "Bruce Garrabrandt",
        source= "https://www.google.com/search?q=Bruce+Garrabrandt+Creativity+doesn%27t+wait",
        tags= "creativity, creative, perfect, waiting, ordinary",
        text= "Creativity doesn't wait for that perfect moment. It fashions its own perfect moments out of ordinary ones."
        ),

        Quote(
        id=10,
        author= "Bruce Lee",
        source= "https://www.goodreads.com/quotes/4146-do-not-pray-for-an-easy-life-pray-for-the",
        tags= "life, stoic",
        text= "Do not pray for an easy life, pray for the strength to endure a difficult one"
        ),
        
        Quote(
        id=11,
        author= "Bruce Lee",
        source= "https://www.goodreads.com/quotes/19527-be-happy-but-never-satisfied",
        tags= "stoic, happiness",
        text= "Be happy, but never satisfied."
        ),

        Quote(
        id=12,
        author= "Buckminster Fuller",
        source= "https://www.goodreads.com/quotes/13119",
        tags= "future, progress, reality, new",
        text= "You never change things by fighting the existing reality. To change something, build a new model that makes the existing model obsolete"
        ),

        Quote(
        id=13,
        author= "Chelsea Leyland",
        source= "https://www.brainyquote.com/quotes/chelsea_leyland_624473",
        tags= "Beauty, Sleep, Secret",
        text= "Sleep is the real beauty secret, but I don't get enough of that."
        ),

        Quote(
        id=14,
        author= "Confucius",
        source= "https://www.goodreads.com/quotes/961585",
        tags= "future, tomorrow, past",
        text= "Think of tomorrow, the past can't be mended."
        ),

        Quote(  
        id=15,
        author= "Dalai Lama",
        source= "https://dailymeditate.com/meditation-quote-99-sleep-meditation-dalai-lama/",
        tags= "Mindful, Sleep, Meditation, Relaxing, Rest",
        text= "Sleep is the best meditation."
        ),

        Quote(
        id=16,
        author= "David Bowie",
        source= "https://www.goodreads.com/quotes/462535",
        tags= "future, life, listen",
        text= "Tomorrow belongs to those who can hear it coming"
        ),

        Quote(
        id=17,
        author= "Deepak Chopra",
        source= "https://www.goodreads.com/quotes/381641",
        tags= "future, choice, decision, change",
        text= "When you make a choice, you change the future."
        ),

        Quote(
        id=18,  
        author= "Dennis Gabor",
        source= "https://en.wikiquote.org/wiki/Dennis_Gabor",
        tags= "future, invention, society",
        text= "The future cannot be predicted, but futures can be invented. It was man's ability to invent which has made human society what it is." 
        ),

        Quote(
        id=19,
        author= "Dieter F. Uchtdorf",
        source= "https://www.goodreads.com/quotes/8070701",
        tags= "creative, creativity, soul",
        text= "The desire to create is one of the deepest yearnings of the human soul."
        ),

        Quote(
        id=20,
        author= "Diogenes",
        source= "https://www.goodreads.com/quotes/524180-when-some-one-reminded-him-that-the-people-of-sinope",
        tags= "stoic, outlook, mentality",
        text= "When some one reminded him that the people of Sinope had sentenced him to exile, he said, And I sentenced them  to stay at home." 
        ),

        Quote(
        id=21,
        author= "Doris Mortman",
        tags= "contentment, peace, self-acceptance",
        source= "https://www.goodreads.com/quotes/112887-until-you-make-peace-with-who-you-are-you-ll-never",
        text= "Until you make peace with who you are, you'll never be content with what you have."
        ),

        Quote(
        id=22,
        author= "Edith Södergran",
        source= "https://www.goodreads.com/quotes/11458",
        tags= "creativity, fire, passion",
        text= "The inner fire is the most important thing mankind possesses."
        ),

        Quote(
        id=23,
        author= "Epictetus",
        source= "https://www.goodreads.com/quotes/123453-there-is-only-one-way-to-happiness-and-that-is?page=2",  
        tags= "stoic, willpower",
        text= "There is only one way to happiness and that is to cease worrying about things which are beyond the power or our will. "
        ),

        Quote(
        id=24,
        author= "Eric Hoffer",
        source= "https://www.goodreads.com/quotes/10562",
        tags= "change, learners, learned, learn, world",
        text= "In times of change learners inherit the earth, while the learned find themselves beautifully equipped to deal with a world that no longer exists."
        ),

        Quote(
        id=25,
        author= "Florence Nightingale",
        source= "https://www.goodreads.com/quotes/161358",
        tags= "excuse, excuses, success",
        text= "I attribute my success to this: I never gave or took an excuse."
        ),

        Quote(
        id=26,
        author= "Fyodor Dostoevsky",
        source= "https://www.goodreads.com/author/quotes/3137322.Fyodor_Dostoyevsky",
        tags= "soul, children, healing",
        text= "The soul is healed by being with children."
        ),              

        Quote(
        id=27,
        author= "George Bernard Shaw",
        source= "https://www.goodreads.com/quotes/8727",
        tags= "meaning, creativity",
        text= "Life isn't about finding yourself. Life is about creating yourself."
        ),

        Quote(
        id=28,
        author= "Henri Matisse",
        source= "https://www.goodreads.com/quotes/21433",
        tags= "creativity, courage",
        text= "Creativity takes courage."
        )
]  

db_authors: List[Author] = [
    Author(
        id=1,
        first_name= "Albert",
        last_name= "Einstein",
        bio= "Albert Einstein was a German-born theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics. His work is also known for its influence on the philosophy of science."
    ),

    Author(
        id=2,
        first_name= "Albert",
        last_name= "Gray",
        bio= "Albert Gray was a well-known motivational speaker and author. He is best known for his book The Common Denominator of Success."
    ),

    Author(
        id=3,
        first_name= "Annie",
        last_name= "Dillard",
        bio= "Annie Dillard is an American author, best known for her narrative prose in both fiction and non-fiction. She has published works of poetry, essays, prose, and literary criticism, as well as two novels and one memoir."
    ),

    Author(
        id=4,
        first_name= "Arianna",
        last_name= "Huffington",
        bio= "Arianna Huffington is a Greek-American author, syndicated columnist, and businesswoman. She is the founder of The Huffington Post, the founder and CEO of Thrive Global, and the author of fifteen books."
    ),

    Author(
        id=5,
        first_name= "Aristotle",
        last_name= "Aristotle",
        bio= "Aristotle was a Greek philosopher and polymath during the Classical period in Ancient Greece. Taught by Plato, he was the founder of the Lyceum, the Peripatetic school of philosophy, and the Aristotelian tradition."
    ),

    Author(
        id=6,
        first_name= "Benjamin",
        last_name= "Franklin",
        bio= "Benjamin Franklin was one of the Founding Fathers of the United States. A polymath, he was a leading writer, printer, political philosopher, politician, Freemason, postmaster, scientist, inventor, humorist, civic activist, statesman, and diplomat."
    ),

    Author(
        id=7,
        first_name= "Bill",
        last_name= "Gates",
        bio= "Bill Gates is an American business magnate, software developer, and philanthropist. He is best known as the co-founder of Microsoft Corporation."
    ),

    Author( 
        id=8,
        first_name= "Brian",
        last_name= "Tracy",
        bio= "Brian Tracy is a Canadian-American motivational public speaker and self-development author. He is the author of over seventy books that have been translated into dozens of languages."
    ),

    Author(
        id=9,
        first_name= "Bruce",
        last_name= "Garrabrandt",
        bio= "Bruce Garrabrandt is a creative writer and author. He is best known for his book 'The Creative Writer's Notebook'."
    ),

    Author(
        id=10,
        first_name= "Bruce",
        last_name= "Lee",  
        bio= "Bruce Lee was a Hong Kong-American martial artist, actor, director, martial arts instructor, and philosopher. He was the founder of Jeet Kune Do, a hybrid martial arts philosophy drawing from different combat disciplines that is often credited with paving the way for modern mixed martial arts."
    ),
]



# le setup d'authentification
SECRET_KEY = "inspire"
ALGORITHM = "HS256"
security = HTTPBearer()

# creation du token
def create_token():
    expiration = datetime.utcnow() + timedelta(hours=1)
    payload = {"exp": expiration, "sub": "user"}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# verification du token
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

#endpoint pour recuperer le token
@app.get("/token")
def get_token():
    return {"token": create_token()}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Inspire Hub API!"}

#endpoint pour avoir toutes les citations
@app.get("/quotes", dependencies=[Depends(verify_token)])
async def read_quotes():
    return db_quotes

#endpoint pour rechercher une citation par son id
@app.get("/quotes/search{quote_id}", dependencies=[Depends(verify_token)])
async def read_quote(quote_id: int):
    for quote in db_quotes:
        if quote.id == quote_id:
            return quote
    raise HTTPException(status_code=404, detail="Quote not found")

#endpoint pour rechercher une citation et ses details grâce a une URL (API externe CiteAS)
@app.get("/quotes/details",dependencies=[Depends(verify_token)])
async def get_details(resource: str):
    url = f"https://api.citeas.org/product/{resource}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    raise HTTPException(status_code=404, detail=f"Citation not found for {resource}")


#endpoint pour créer une nouvelle citation
@app.post("/quotes/new_quote", dependencies=[Depends(verify_token)])
async def create_quote(new_quote: Quote):
    db_quotes.append(new_quote)
    return new_quote

#endpoint pour modifier une citation
@app.put("/quotes/{quote_id}", dependencies=[Depends(verify_token)])
async def update_quote(quote_id: int, updated_quote: Quote):
    for index, quote in enumerate(db_quotes):
        if quote.id == quote_id:
            db_quotes[index] = updated_quote
            return {"message": "Quote has been updated successfully"}
    raise HTTPException(status_code=404, detail="Quote not found")

#endpoint pour supprimer une citation
@app.delete("/quotes/{quote_id}", dependencies=[Depends(verify_token)])
async def delete_quote(quote_id: int):
    for quote in db_quotes:
        if quote.id == quote_id:
            db_quotes.remove(quote)
            return {"message": "Quote has been deleted successfully"}
    raise HTTPException(status_code=404, detail="Quote not found")

#endpoint pour avoir tous les auteurs
@app.get("/authors", dependencies=[Depends(verify_token)])
async def read_authors():
    return db_authors

#endpoint pour rechercher un auteur par son id
@app.get("/authors/search{author_id}", dependencies=[Depends(verify_token)])
async def read_author(author_id: int):
    for author in db_authors:
        if author.id == author_id:
            return author
    raise HTTPException(status_code=404, detail="Author not found")

#endpoint pour creer un nouvel auteur
@app.post("/authors/new_author", dependencies=[Depends(verify_token)])
async def create_author(new_author: Author):
    db_authors.append(new_author)
    return new_author

#endpoint pour modifier un auteur
@app.put("/authors/{author_id}", dependencies=[Depends(verify_token)])
async def update_author(author_id: int, updated_author: Author):
    for index, author in enumerate(db_authors):
        if author.id == author_id:
            db_authors[index] = updated_author
            return {"message": "Author has been updated successfully"}
    raise HTTPException(status_code=404, detail="Author not found")

#endpoint pour supprimer un auteur
@app.delete("/authors/{author_id}", dependencies=[Depends(verify_token)])
async def delete_author(author_id: int):
    for author in db_authors:
        if author.id == author_id:
            db_authors.remove(author)
            return {"message": "Author has been deleted successfully"}
    raise HTTPException(status_code=404, detail="Author not found")

#endpoint pour retourner une citation aleatoire par jour
@app.get("/quotes/dayquote", dependencies=[Depends(verify_token)])
async def get_day_quote():
    if not db_quotes:
        raise HTTPException(status_code=404, detail="No quotes available")
    
    return {"message": "Today's quote is:", "quote": random.choice(db_quotes)}

