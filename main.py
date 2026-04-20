from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int

@app.get("/users/")
async def read_users(
    skip: int = Query(0, ge=0, le=100, description="Skip the first n users"),
    limit: int = Query(10, ge=1, le=100, description="Number of users to return")
):
    return {"skip": skip, "limit": limit}
```

```python
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int

@app.get("/users/")
async def read_users(
    skip: int = Query(0, ge=0, le=100, description="Skip the first n users"),
    limit: int = Query(10, ge=1, le=100, description="Number of users to return")
):
    return {"skip": skip, "limit": limit}
