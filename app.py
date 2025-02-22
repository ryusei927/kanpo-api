from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from kanpo import normalized_kampo_data  # `kanpo.py` からデータをインポート

app = FastAPI(root_path="/")  # root_path を設定

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "漢方APIが正常に動作しています！"}

@app.get("/search")
def search_kampo(numbers: List[str] = Query([])):
    """ 漢方番号を受け取り、成分の合計を返すAPI """
    result = {}

    for num in numbers:
        normalized_num = str(int(num))  # "001" → "1" に変換
        if normalized_num in normalized_kampo_data:
            for ingredient, amount in normalized_kampo_data[normalized_num].items():
                result[ingredient] = result.get(ingredient, 0) + amount

    return {"total_ingredients": result}
