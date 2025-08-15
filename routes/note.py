from fastapi import APIRouter,Request,status,HTTPException
from config.db import conn
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from bson import ObjectId  # --> to convert the string id to ObjectId type for mongodb

note=APIRouter()


# templates folder
templates = Jinja2Templates(directory="templates")

# home page
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    #  docs = conn.notes.notes.find_one({})  #--> conn.db-name.collection-name.find_one({}) --> get one document from collection
    #  print(docs)

    #  to get all docs from collection   --> conn.db-name.collection-name.find({})
     docs = await conn.notes.notes.find({}).to_list(length=None)     #--> get all documents from collection
     newDocs = []
     for doc in docs:
         newDocs.append({
              "id": doc["_id"],
              "title": doc["title"],  # -->fetching the title field from the document
              "desc": doc["desc"],    # -->fetching the desc field from the document
              "important": doc["important"]  # -->fetching the important field from the document
         })
     
     return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})  # only this way works, not the other way given in the documentation


@note.post("/")
async def create_item(request: Request):
   form = await request.form() 
   formDict=dict(form) 
   formDict["important"] = True if formDict.get("important")=="on" else False
   await conn.notes.notes.insert_one(formDict)     
   return RedirectResponse("http://127.0.0.1:8000",status_code=status.HTTP_302_FOUND)  # redirect to home page

@note.get("/Delete/{id}")
async def delete_item(id: str):
    object_id = ObjectId(id)
    res=await conn.notes.notes.find_one({"_id":object_id})
    if res:
        await conn.notes.notes.delete_one({"_id":res["_id"]})  # can also use object_id instead of res["_id"]
    return RedirectResponse("http://127.0.0.1:8000")  # redirect to home page


@note.get("/Update/{id}")
async def show_update_form(id: str, request: Request):
    try:
        object_id = ObjectId(id)
        res = await conn.notes.notes.find_one({"_id": object_id})
        if res:
            # Convert ObjectId to string for template
            res["id"] = str(res["_id"])
            return templates.TemplateResponse(
                "update.html",
                {"request": request, "res": res}
            )
        return RedirectResponse("http://127.0.0.1:8000", status_code=303)
    except Exception as e:
        print(f"Error loading note: {e}")
        return RedirectResponse("http://127.0.0.1:8000", status_code=303)

@note.post("/Update/{id}")
async def update_item(id: str, request: Request):
    try:
        object_id = ObjectId(id)
        form = await request.form()
        form_dict = dict(form)
        
        # Handle boolean conversion for checkbox
        form_dict["important"] = "important" in form_dict

        existing_doc = await conn.notes.notes.find_one({"_id": object_id})
        if existing_doc:
            await conn.notes.notes.update_one(
                {"_id": object_id},
                {"$set": form_dict}
            )
            # Redirect to home page or show success message
            return RedirectResponse("http://127.0.0.1:8000", status_code=303)
        
        return RedirectResponse("http://127.0.0.1:8000", status_code=303)
    except Exception as e:
        print(f"Error updating note: {e}")
        return RedirectResponse("http://127.0.0.1:8000", status_code=303)