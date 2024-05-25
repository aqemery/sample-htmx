from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_items():
    return open("index.html", "r").read()

@app.get("/pressed", response_class=HTMLResponse)
def pressed():
    return f"""
        <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" hx-get="/boom" hx-swap="outerHTML">Hey Stop!</button>
    """

@app.get("/boom", response_class=HTMLResponse)
def boom():
    return f"""
        💣💣💣
    """