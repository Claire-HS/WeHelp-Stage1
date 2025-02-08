from fastapi import FastAPI, Path, Form
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, FileResponse
from pathlib import Path
from typing import Annotated
from urllib.parse import unquote
import secrets
from starlette.middleware.sessions import SessionMiddleware



 
app = FastAPI()

# 指定模板目錄
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=Path(__file__).parent)

# 使用Jinja2模板
@app.get("/")
async def read_homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {
        "request": request, 
        "fields_1": "帳號",
        "fields_2": "密碼",
        "checkbox_1": "同意條款",
    })


# 登入API
@app.post("/signin") 
async def signin(request: Request, user: Annotated[str, Form()], pwd: Annotated[str, Form()]):
    if user == "test" and pwd == "test":
        request.session["signed_in"] = True
        return RedirectResponse(url="/member", status_code = 303)
    elif user == "" or pwd == "":
        return RedirectResponse(url="/error?message=請輸入帳號密碼",status_code = 303)
    else:
        return RedirectResponse(url="/error?message=帳號或密碼錯誤",status_code = 303)

#檢查使用者登入狀態        
async def create_random_session_string():
    return secrets.token_urlsafe(32)
session_token = create_random_session_string()
app.add_middleware(SessionMiddleware, secret_key = session_token)


@app.get("/member")
async def member(request: Request):
    print("member", request.session) 
    response = RedirectResponse(url="/")
    s = request.session.get("signed_in")
    if s == True:
        response = FileResponse("member.html")
    response.headers["Cache-Control"] = "no-store"
    return response


@app.get("/error")
async def error(request: Request):
    m = request.query_params.get('message') 

    return templates.TemplateResponse("error.html", {
        "request":request,
        "message":unquote(m)
    })

@app.get("/signout")
async def signout(request: Request):
    request.session["signed_in"] = False
    response = RedirectResponse(url="/")
    response.headers["Cache-Control"] = "no-cache"
    return response


@app.get("/square/{num}")
def calculate_square(request: Request,num: int):
    square_result = num * num
    formatted_result = f"{square_result:,}"
    return templates.TemplateResponse("squaredNumber.html",{
        "request": request,
        "message": formatted_result
    })










