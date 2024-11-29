from api.blog import blog
from api.blog.blog import blog_router, get_blog_info, list_blog_posts, load_blog_content
from api.home import home
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from nicegui import ui

app = FastAPI()

origins = [
    "localhost:8000",
    "https://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(blog_router)

blog.init(app)
home.init(app)
