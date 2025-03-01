from fastapi import FastAPI, Path, Form, Query, Body
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, JSONResponse
from pathlib import Path
from typing import Annotated
from urllib.parse import unquote
import secrets
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector
from pydantic import BaseModel
import json


app = FastAPI()

class DeleteMessageRequest(BaseModel):
    message_id: int

class NameUpdateRequest(BaseModel):
    name: str


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=Path(__file__).parent)


# 如果css沒有刷新,先嘗試清除瀏覽器快取
@app.get("/")
async def read_homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {
        "request" : request, 
        "fields_1" : "姓名",
        "fields_2" : "帳號",
        "fields_3" : "密碼"
    })


# 資料庫連線
db_connect = mysql.connector.connect(
    user="root",
    password="Ling0424J",
    host="localhost",
    database="website",
)
# 建立cursor物件，用來對database下SQL指令 
# cursor = db_connect.cursor()
# print("Database ready!")


app.add_middleware(SessionMiddleware, secret_key = "4J1e8_T4a2e4_L5i1n1g_O5r2m7")


# for signing up 
@app.post("/signup")
async def signup(request: Request, user: Annotated[str, Form()], username: Annotated[str, Form()], pwd: Annotated[str, Form()]):
    cursor = db_connect.cursor()
    cursor.execute("SELECT username FROM member WHERE BINARY username=%s", (username,))
    existing_username = cursor.fetchone()
    if existing_username:
        return RedirectResponse(url="/error?message=該帳號已存在",status_code = 303)
        # print("Repeated username")
    else:
        cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (user, username, pwd))
        db_connect.commit()
        # print("Signup successful!")
        return RedirectResponse(url="/", status_code = 303)


# for signing in 
@app.post("/signin")
async def signin(request: Request, username: Annotated[str, Form()], pwd: Annotated[str, Form()]):
    cursor = db_connect.cursor()
    cursor.execute("SELECT * FROM member WHERE BINARY username=%s AND BINARY password=%s", (username, pwd))
    member_checked = cursor.fetchone()
    # print(member_checked)
    if member_checked:
        request.session["signed_in"] = True #登入狀態
        request.session["member_id"] = member_checked[0]   # ID
        request.session["username"] = member_checked[2]   # username
        request.session["name"] = member_checked[1]       # name
        return RedirectResponse(url="/member", status_code = 303)
    else:
        return RedirectResponse(url="/error?message=帳號或密碼輸入錯誤", status_code = 303)


@app.get("/member")
async def member(request: Request):
    # print("Session內容:", request.session)
    cursor = db_connect.cursor(dictionary=True) #回傳dict而非tuple
    response = RedirectResponse(url="/")
    status_check = request.session.get("signed_in")
    if status_check == True:         
        member_name = request.session.get("name")
        cursor.execute("SELECT member.name, message.id, message.content FROM message JOIN member ON message.member_id = member.id ORDER BY message.time DESC")
        messages = cursor.fetchall()
        # print(messages)
        response = templates.TemplateResponse("member.html",{
            "request" : request,
            "member_name" : member_name,
            "messages" : messages,
        })
        response.headers["Cache-Control"] = "no-store"
        return response
    else:
        return response



@app.get("/signout")
async def signout(request: Request):
    request.session.clear()
    response = RedirectResponse(url="/")
    return response


@app.post("/createMessage")
async def create_message(request: Request, text: Annotated[str, Form()]):
    member_id = request.session.get("member_id")
    cursor = db_connect.cursor()
    cursor.execute("INSERT INTO message(member_id, content) VALUES (%s, %s)", (member_id, text))
    db_connect.commit()
    # print("訊息已成功送出！")
    return RedirectResponse(url="/member", status_code = 303)


@app.post("/deleteMessage")
async def delete_message(request: Request, body: DeleteMessageRequest):
    user_id = request.session.get("member_id") #當前使用者ID
    cursor = db_connect.cursor()
    cursor.execute("SELECT member_id FROM message WHERE id=%s", (body.message_id,)) #查詢留言對應的member_id
    message_writer_id = cursor.fetchone()
    if user_id == message_writer_id[0]:
        cursor.execute("DELETE FROM message WHERE id = %s", (body.message_id,))
        db_connect.commit()
        return RedirectResponse(url="/member", status_code = 303)
    else:
        return JSONResponse(
            status_code=403,
            content={"message": "非留言者，無權刪除此留言"},
        )





@app.get("/error")
async def error(request: Request, message: Annotated[str, Query()] = "Unknown error"): 
    return templates.TemplateResponse("error.html", {
        "request" : request,
        "message" : unquote(message),
    })


@app.get("/api/member")
async def name_query(request: Request, username: Annotated[str,None]):
    cursor = db_connect.cursor()
    cursor.execute("SELECT id, name, username FROM member WHERE BINARY username=%s", (username,))
    existing_username = cursor.fetchone()
    status_check = request.session.get("signed_in")
    if existing_username and status_check:
        result = {
            "id": existing_username[0],
            "name": existing_username[1],
            "username": existing_username[2]
        }
        return {"data":result}
    else:
        return{"data": None }
    

@app.patch("/api/member")
async def name_update(request: Request, body: NameUpdateRequest):
    status_check = request.session.get("signed_in") 
    if status_check:
        user_id = request.session.get("member_id") #當前使用者ID
        cursor = db_connect.cursor()
        cursor.execute("UPDATE member SET name=%s WHERE id=%s", (body.name, user_id))
        request.session["name"]=body.name
        db_connect.commit()
        return{"ok": True}
    else:
        return{"error": True}



    





