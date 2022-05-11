from typing import List
from fastapi import APIRouter,Depends
from database import get_db
from sqlalchemy.orm import Session
from models import Blogs
from schemas import add_blog,show_blog, show_user
from oauth2 import current_user

router = APIRouter(
    tags = ["Blogs"]
)

@router.post('/blogs')
def create_blog(request: add_blog,db: Session = Depends(get_db),user : show_user = Depends(current_user)):
    blog = Blogs(title = request.title, body = request.body)
    db.add(blog)
    db.commit()
    db.close()
    return "Blog Created"

@router.get('/',response_model = List[show_blog])
def show_all_blog(db: Session = Depends(get_db),user : show_user = Depends(current_user)):
    all = db.query(Blogs).all()
    return all

@router.get('/blog/{id}',response_model = show_blog)
def show_blog_id(id: int,db: Session = Depends(get_db),user : show_user = Depends(current_user)):
    blog = db.query(Blogs).filter(Blogs.blog_id == id).first()
    return blog