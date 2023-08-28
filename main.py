import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = FastAPI()


origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

herbs = [
    {
        "id": 1,
        "name": "Basil",
        "price": 4,
        "description": "Basil is a fragrant herb with a distinct aroma. It is commonly used in Mediterranean cuisine "
                       "to add flavor to various dishes.",
        "uses": "Basil is widely used in cooking as a culinary herb. It pairs well with tomatoes, pasta, and salads.",
        "origin": "Mediterranean"
    },
    {
        "id": 2,
        "name": "Lavender",
        "price": 3,
        "description": "Lavender is an aromatic herb known for its calming fragrance. It is often used in "
                       "aromatherapy and culinary applications.",
        "uses": "Lavender is used in aromatherapy to promote relaxation and reduce stress. It can also be used in "
                "cooking to add a unique floral flavor to desserts.",
        "origin": "Mediterranean"
    },

    {
        "id": 3,
        "name": "Chamomile",
        "price": 2,
        "description": "Chamomile is a gentle herb with a soothing nature. It is commonly brewed as a tea for its "
                       "calming effects.",
        "uses": "Chamomile tea is popular for promoting relaxation and aiding in sleep. It also has anti-inflammatory "
                "properties and can be used in skincare products.",
        "origin": "Europe"
    },
    {
        "id": 4,
        "name": "Thyme",
        "price": 2,
        "description": "Thyme is a small low-growing shrub and is commonly cultivated as an annual, though it can "
                       "persist as an evergreen perennial in warm climates. The stems are somewhat woody and bear "
                       "simple leaves that are oval to linear and arranged oppositely.",
        "uses": "Thyme (Thymus vulgaris) is an herb with a distinct smell. The flowers, leaves, and oil are commonly "
                "used to flavor foods and are also used as medicine. Thyme contains chemicals that might help "
                "bacterial and fungal infections. It also might help relieve coughing and have antioxidant effects.",
        "origin": "Pakistan"
    },
    {
        "id": 5,
        "name": "Mint",
        "price": 2,
        "image": "@/assets/Mint.png",
        "description": "Mints have square stems and opposite aromatic leaves. Many can spread vegetatively by stolons "
                       "and can be aggressive in gardens. The small flowers are usually pale purple, pink, "
                       "or white in colour and are arranged in clusters, either forming whorls or crowded together in "
                       "a terminal spike",
        "uses": "Eating fresh or dried leaves: Used to treat bad breath. Inhaling essential oils: May improve brain "
                "function and cold symptoms. Applying it to the skin",
        "origin": "Europe"
    },
]


@app.get("/api/herbs")
def get_herbs():
    return herbs


@app.get("/api/herbs/{herb_id}")
def get_herb_detail(herb_id: int):
    herb = next((h for h in herbs if h["id"] == herb_id), None)
    if herb is None:
        return {"error": "Herb not found"}
    return herb


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
