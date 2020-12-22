import uvicorn
from fastapi import FastAPI
from routers import posts

app = FastAPI(prefix="/")

app.include_router(posts.router, prefix="/post")
@app.get('/')
def get_hello():
    return {'message': 'Hello from FastAPI Server!'}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)