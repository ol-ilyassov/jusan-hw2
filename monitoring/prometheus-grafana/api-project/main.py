
## Init:

from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from prometheus_client import Counter, Histogram, Gauge, make_asgi_app
from pydantic import BaseModel
import time

app = FastAPI()

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

## Metrics:

http_requests_total = Counter(
    "http_requests_total", 
    "Number of HTTP requests received", 
    ["method", "endpoint"]
)

http_requests_milliseconds = Histogram(
    "http_requests_milliseconds", 
    "Duration of HTTP requests in milliseconds", 
    ["method", "endpoint"]
)

last_sum1n = Gauge("last_sum1n", "Value stores last result of sum1n")
last_fibo = Gauge("last_fibo", "Value stores last result of fibo")
list_size = Gauge("list_size", "Value stores current list size")
last_calculator = Gauge("last_calculator", "Value stores last result of calculator")
errors_calculator_total = Counter("errors_calculator_total", "Number of errors in calculator")

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

item_list = []

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
    
    start_time = time.time()
    
    result = 0
    for i in range(n+1):
        result += i
    
    last_sum1n.set(result)
    
    duration = (time.time() - start_time) * 1000
    http_requests_milliseconds.labels(method="GET", endpoint="/sum1n").observe(duration)

    http_requests_total.labels(method="GET", endpoint="/sum1n").inc()
    
    return {"result": result}

@app.get("/fibo", tags=["Task"])
async def fibonacci(n:int):
    if n < 1:
        return JSONResponse(status_code=400, content={"error": NaturalNumError})
    
    start_time = time.time()
    
    result = fib_num(n)
    
    last_fibo.set(result)

    duration = (time.time() - start_time) * 1000
    http_requests_milliseconds.labels(method="GET", endpoint="/fibo").observe(duration)
    
    http_requests_total.labels(method="GET", endpoint="/fibo").inc()
    
    return {"result": result}

@app.post("/reverse", tags=["Task"])
async def Reverse(string:str = Header(...)):
    start_time = time.time()
    
    result = string[::-1]
    
    duration = (time.time() - start_time) * 1000
    http_requests_milliseconds.labels(method="POST", endpoint="/reverse").observe(duration)
    
    http_requests_total.labels(method="POST", endpoint="/reverse").inc()
    
    return {"result": result}

@app.get("/list", tags=["Task"])
async def get_list():
    start_time = time.time()
    
    list_size.set(len(item_list))
    
    duration = (time.time() - start_time) * 1000
    http_requests_milliseconds.labels(method="GET", endpoint="/list").observe(duration)
    
    http_requests_total.labels(method="GET", endpoint="/list").inc()
    
    return {"result": item_list}

@app.put("/list", tags=["Task"])
async def save_list(input:ListInput):
    start_time = time.time()
    
    item_list.append(input.element)
    
    duration = (time.time() - start_time) * 1000
    http_requests_milliseconds.labels(method="PUT", endpoint="/list").observe(duration)
    
    http_requests_total.labels(method="PUT", endpoint="/list").inc()
    
    return {"status": "ok", "added_element": input.element}

@app.post("/calculator", tags=["Task"])
async def calculator(input:CalcInput):
    start_time = time.time()
    
    parts = input.expr.split(',')
    if len(parts) != 3:
        errors_calculator_total.inc()
        return JSONResponse(status_code=400, content={"error": InvalidError})
    
    try:
        num1 = float(parts[0])
        operator = parts[1].strip()
        num2 = float(parts[2])
    except ValueError:
        errors_calculator_total.inc()
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
                errors_calculator_total.inc()
                return JSONResponse(status_code=403, content={"error": ZeroDivError})
            result = num1 / num2
        case _:
            errors_calculator_total.inc()
            return JSONResponse(status_code=400, content={"error": InvalidError})
    
    last_calculator.set(result)
    
    duration = (time.time() - start_time) * 1000
    http_requests_milliseconds.labels(method="POST", endpoint="/calculator").observe(duration)
    
    http_requests_total.labels(method="POST", endpoint="/calculator").inc()
    
    return {"result": result}
