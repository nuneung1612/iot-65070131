from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/area/{width}/{height}')
def triangle(width: int, height: int, response: Response):
    if (int(width) == width and int(height) == height):
        ans = (0.5)*(width)*height
        return ans
    response.status_code = 404
    return {
        'message': 'input number only'
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)