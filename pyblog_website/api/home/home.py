from nicegui import ui
from fastapi import FastAPI
from ..style import title, subtitle

def init(app: FastAPI) -> None: 
    @ui.page('/')
    async def home_page():
        ui.label('Personal BB blog!').classes('text-2xl font-bold')
        ui.link('Blog', '/blog').classes('text-2xl font-bold text-blue-500')
    ui.run_with(
        app,
        title="BB's Blog"
    )