from sqlalchemy.orm import Session
from db.models.blog import Blog
from schemas.blog import CreateBlog, UpdateBlog


def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    blog = Blog(**blog.model_dump(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retrieve_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def list_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active == True).all()
    return blogs


def update_blog(id: int, blog: UpdateBlog, author_id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db:
        return
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.commit()
    return blog_in_db


def delete_blog(id: int, author_id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id)
    if not blog_in_db.first():
        return {"error": f"Could not find blog with id {id}"}
    blog_in_db.delete()
    db.commit()
    return {"message": f"Blog with id {id} has been deleted"}
