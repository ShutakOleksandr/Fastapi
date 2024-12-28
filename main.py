hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"},
    {"id": 3, "title": "Мальдивы", "name": "maldivi"},
    {"id": 4, "title": "Геленджик", "name": "gelendzhik"},
    {"id": 5, "title": "Москва", "name": "moscow"},
    {"id": 6, "title": "Казань", "name": "kazan"},
    {"id": 7, "title": "Санкт-Петербург", "name": "spb"},
]





@router.get("")
def get_hotels(
    id: int = Query(None),
    title: str = Query(None),
    page: int = Query(1),
    per_page: int = Query(3),
):
    filtered_hotels = [
        hotel for hotel in hotels
        if (id is None or hotel["id"] == id) and (title is None or title.lower() in hotel["title"].lower())
    ]
    start = (page - 1) * per_page
    end = start + per_page
    return filtered_hotels[start:end]
