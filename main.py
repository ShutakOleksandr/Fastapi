from os import name
from fastapi import FastAPI, Query, Body
from sqlalchemy import true
import uvicorn

app = FastAPI()

hotels = [
	{"id": 1, "title": "Sochi", "name": "sochi"},
	{"id": 2, "title": "Dubai", "name": "dubai"},
]


@app.get("/hotels")
def get_hotels(
    id: int = Query(description="Id hotel"),
	title: str = Query(description="Name hotel"),
):
    return [hotel for hotel in hotels if hotel["title"] == title and hotel["id"] == id ] 


@app.post("/hotels")
def create_hotel(
	title: str = Body(embed=True)
):
    global hotels
    
    hotels.append({
		"id": hotels[-1]["id"] + 1,
		"title": title,
	})

    return {"status": "ok"}


@app.put("/hotels/{hotel_id}")
def put_hotel(
    hotel_id: int,
    title: str = Body(..., embed=True, description="New title of the hotel"),
    name: str = Body(..., embed=True, description="New name of the hotel")
):
    global hotels
    
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["title"] = title
            hotel["name"] = name
            
            return {"status": "ok"}
        else:
            return {"status": "bad"}



@app.patch("/hotels/{hotel_id}")
def patch_hotel(
    hotel_id: int,
    title: str = Body(None, embed=True, description="Optional new title of the hotel"),
    name: str = Body(None, embed=True, description="Optional new name of the hotel")
):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            if title is not None:
                hotel["title"] = title
            if name is not None:
                hotel["name"] = name
            return {"status": "updated", "hotel": hotel}
        else:
            return {"status": "bad"}
      




@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    
    return {"status": "OK"}


if __name__ == '__main__':
	uvicorn.run("main:app", reload=True)
