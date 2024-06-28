from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"backend": "0.01"}


@app.get("/get_product_specification/")
def get_product_specification():
    """function to get product specification"""
    info = {
            "MANICURE": {
            "Acrilicas": "$150,000",
            "Polygel": "$125,000",
            "Press On": "$110,000",
            "Semipermanente": "$40,000",
            "Tradicional": "$20,000"
            },
            "PEDICURE": {
            "Semipermanente": "$50,000",
            "Tradicional": "$30,000"
            }
            }

    
    return{"result": info}


@app.get("/get_service_price/{category}/{subcategory}")
def get_service_price(category: str, subcategory: str):
    """function to get service price"""

    def get_service_price(self,category, subcategory):
        info = {
        "MANICURE": {
        "Acrilicas": "$150,000",
        "Polygel": "$125,000",
        "Press On": "$110,000",
        "Semipermanente": "$40,000",
        "Tradicional": "$20,000"
        },
        "PEDICURE": {
        "Semipermanente": "$50,000",
        "Tradicional": "$30,000"
        }
        }

        if category in info and subcategory in info[category]:
            return info[category][subcategory]
        else:
            return "Combination not found"
        
    result = get_service_price(category, subcategory)
    return {"result": result}