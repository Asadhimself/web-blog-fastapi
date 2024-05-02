from datetime import date
from pydantic import BaseModel, model_validator
from slugify import slugify


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: str | None

    @model_validator(pre=True)
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = slugify(values.get("title"))


class ShowBlog(BaseModel):
    title: str
    content: str | None
    created_at: date

    class Config:
        orm_mode = True


class UpdateBlog(CreateBlog):
    pass
