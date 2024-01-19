from fastapi import FastAPI

app = FastAPI()


@app.get('/calculate/')
def calculate(number: int):
    result = [i * number for i in range(1, 11)]
    return result
