
## Init:

from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

## Swagger Documentation details:

app.title="FastAPI-Final"
app.version="1.0.0"
app.description="Jusan Singularity course. DevOps direction. Homework #4. FastAPI."
app.contact={"name":"Olzhas Ilyassov", "url":"https://github.com/ol-ilyassov/jusan-hw2"}
app.license_info={"name":"MIT License", "url":"https://opensource.org/licenses/MIT"}

## Errors:

NegativeNumError = "n must be a non-negative integer"
NaturalNumError = "n must be a positive integer"
InvalidError = "invalid"
ZeroDivError = "zerodiv"

## Domain:

def fib_num(n: int) -> int:
    n -= 1 # индексация первого числа начинается с 1.
    
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

list = []

class ListInput(BaseModel):
    element:str

class CalcInput(BaseModel):
    expr:str

## Routes:

@app.get("/healthcheck", tags=["Base"])
async def healthcheck():
    return {"status": "ok"}

@app.get("/sum1n/{n}", tags=["Task"])
async def sum1n(n:int):
    if n < 0:
        return JSONResponse(status_code=400, content={"error": NegativeNumError})
    
    result = 0
    for i in range(n+1):
        result += i
    return {"result": result}

@app.get("/fibo", tags=["Task"])
async def fibonacci(n:int):
    if n < 1:
        return JSONResponse(status_code=400, content={"error": NaturalNumError})
    
    result = fib_num(n)
    return {"result": result}

@app.post("/reverse", tags=["Task"])
async def Reverse(string:str = Header(...)):
    result = string[::-1]
    return {"result": result}

@app.get("/list", tags=["Task"])
async def get_list():
    return {"result": list}

@app.put("/list", tags=["Task"])
async def save_list(input:ListInput):
    list.append(input.element)

@app.post("/calculator", tags=["Task"])
async def calculator(input:CalcInput):
    parts = input.expr.split(',')
    if len(parts) != 3:
        return JSONResponse(status_code=400, content={"error": InvalidError})
    
    try:
        num1 = float(parts[0])
        operator = parts[1].strip()
        num2 = float(parts[2])
    except ValueError:
        return JSONResponse(status_code=400, content={"error": InvalidError})
    
    match operator:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                return JSONResponse(status_code=403, content={"error": ZeroDivError})
            result = num1 / num2
        case _:
            return JSONResponse(status_code=400, content={"error": InvalidError})
    
    return {"result": result}
