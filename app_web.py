from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.controller.web_controlador import WebControlador
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

if __name__ == "__main__":
    app = FastAPI()
    web_controlador = WebControlador()
    app.add_middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(web_controlador.router)
    app.mount("/", StaticFiles(directory="src/view/web", html=True), name="static")
    uvicorn.run(app=app, host="192.168.1.52", port=8000)
