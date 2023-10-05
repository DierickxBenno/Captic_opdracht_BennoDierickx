# create fast api app
paths_to_modules = ["./metadata", "./routers"]

from fastapi import FastAPI, APIRouter
import json
import sys

for path in paths_to_modules:
    if path not in sys.path:
        sys.path.append(path)


print(sys.path)
import name_router as name

app = FastAPI()
app.include_router(name.router)


def status_code(p_code):
    return {"status code": p_code}


@app.get("/")
async def root():
    return " Go to: http://localhost:8000/docs "
