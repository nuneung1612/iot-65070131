from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import models
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
router_v1 = APIRouter(prefix='/api/v1')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils

@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router_v1.get('/books/{book_id}')
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

@router_v1.post('/books')
async def create_book(book: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newbook = models.Book(title=book['title'], author=book['author'], year=book['year'], is_published=book['is_published'])
    db.add(newbook)
    db.commit()
    db.refresh(newbook)
    response.status_code = 201
    return newbook

# @router_v1.patch('/books/{book_id}')
# async def update_book(book_id: int, book: dict, db: Session = Depends(get_db)):
#     pass

# @router_v1.delete('/books/{book_id}')
# async def delete_book(book_id: int, db: Session = Depends(get_db)):
#     pass

#---------student----------
@router_v1.get('/student')
async def get_stu(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@router_v1.get('/student/{stu_id}')
async def get_stu(stu_id: int, db: Session = Depends(get_db)):
    return db.query(models.Student).filter(models.Student.id == stu_id).first()

@router_v1.post('/student')
async def create_stu(stu: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newstu = models.Student(stu_id=stu['stu_id'], fname=stu['fname'], lname=stu['lname'], dob=stu['dob'], gender=stu['gender'])
    db.add(newstu)
    db.commit()
    db.refresh(newstu)
    response.status_code = 201
    return newstu


#------Delete Eror-----------
@router_v1.delete('/student/{stu_id}')
async def get_stu(stu_id: int, db: Session = Depends(get_db)):
    db.query(models.Student).filter(models.Student.id == stu_id).first()
    db.delete()
#------Delete Eror-----------
app.include_router(router_v1)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
