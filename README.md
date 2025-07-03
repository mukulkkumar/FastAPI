# FastAPI

* Fast: High performance (built on Starlette and Pydantic)

* Pythonic: Type-hint support, auto validation

* Async: Native support for async and await

* Auto Docs: Swagger and Redoc UI out of the box


### *Install Package*

```
pip install fastapi

pip install "uvicorn[standard]"  # to run the server
```

### *Run Server*

`uvicorn main:app --reload`


### *Swagger UI:*

`http://127.0.0.1:8000/docs`
