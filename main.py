from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return JSONResponse(content={"message": "Hello,  World"}, status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3001, reload=True)

# Get : ดึงค่าจากพารามิเตอร์มาแสดง
#---------------------------------------------------
#path param
#
@app.get("/profile/{name}")
def get_path_parameter(name:str):
    return JSONResponse(
        content={"message": f"My name is : {name}"},
        status_code=200,
    )

#
# query param
#

@app.get("/profile/")
def get_path_parameter(start:int =0,limit:int=0):
    return JSONResponse(
        content={"message": f"profile start : {start} limit:{limit}"},
        status_code=200,
    )

#
# read list of book
# read ทั้งหมดในDB
@app.get("/books")
def get_books():
    dict_books=[
        {
            "book_id":1,
            "book_name": "harry potter and philosopher's stone",
            "page":223,
        },
        {
          "book_id":2,
            "book_name": "harry potter and the chamber of secrets",
            "page":251,  
        },
        {
            "book_id":3,
            "book_name": "harry potter and prisoner ofazkaban",
            "page":251,
        },
    ]
    return JSONResponse(content={"status": "ok",,"data":dict_books},
status_code=200)

#
# read แค่เฉพาะไอดีนั้นๆ
#
@app.get("/books(/{book_id}")
def get_books_by_id(book_id:int):
    book={
        "book_id":1,
        "book_name": "harry potter and philosopher's stone",
        "page":223,
    }
    responses={"status":"ok","data":book}
    return JSONResponse(content=responses,status_code=200)
    
#
#-----------------------------------------------
# post : create ข้อมูลโดยจะเก็บตามพารามิเตอร์ต่างๆที่กำหนดไว้ โดยต้องตรงตามชนิดที่กำหนดต้องครบทุกอันถึงจะแสดงค่า
#-----------------------------------------------

    class createBookPayload(BaseModel):
        id:str
        name:str
        page:int
#
# create endpoint
#
@app.post("/books")
def create_books(req_body:createBookPayload):
    req_body_dict=req_body.dict()
        id=req_body_dict["id"]
        name=req_body_dict["name"]
        page=req_body_dict["page"]
        book={
            "id":id,
            "name":name,
            "page":page,
        }
        responses={"status":"ok","data":book}
        return JSONResponse(content=responses,status_code=201)

#---------------------------------------------
# Patch : update ค่า
#---------------------------------------------

class updateBookPayload(BaseModel):
    name:str
    page:int

#
#
#
@app.patch("/books/{book_id}")
def update_book_by_id(req_body:updateBookPayload,book_id:str):
    req_body_dict=req_body.dict()

    name=req_body_dict["name"]
    page=req_body_dict["page"]  

    print(f"name:{name},page:{page}")

    update_massage=f"Update book id {book_id} is complete !! "
    responses={"status":"ok", "data": update_massage}
    return JSONResponse(content=responses,status_code=200)

#------------------------------------------------
# delete : delete
#------------------------------------------------


@app.delete("/books/{book_id}")
def delete_book_by_id(book_id:int):
    delete_massage=f"Delete book id {book_id} is complete !!"
    responses={"status":"ok","data":delete_massage}
    return JSONResponse(content=responses,status_code=200)
    
