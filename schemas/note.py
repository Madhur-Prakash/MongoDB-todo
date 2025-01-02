#  this will determine how the note will be displayed in the output 

def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
        "important": item["important"],
        "sno": item["sno"]
    }


def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]