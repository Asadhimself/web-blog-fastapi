from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.repository.blog import create_new_blog, delete_blog, list_blogs, retreive_blog, update_blog
from schemas.blog import CreateBlog, ShowBlog
from db.session import get_db


router = APIRouter()


@router.post("/create/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog


@router.get("/{id}/", response_model=ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )
    return blog


@router.get("/", response_model=list[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs


@router.put("/update/{id}/", response_model=ShowBlog)
def update_blog_by_id(id: int, db: Session = Depends(get_db)):
    blog = update_blog(id=id, blog=blog, author_id=1, db=db)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    return blog


@router.delete("/delete/{id}/")
def delete_blog_by_id(id: int, db: Session = Depends(get_db)):
    message = delete_blog(id=id, author_id=1, db=db)
    if message.get("error"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="error")
    return {"msg": f"Successfully deleted blog with id {id}"}
