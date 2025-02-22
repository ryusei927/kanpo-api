from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# CORS設定（フロントエンドと通信するために必要）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番環境では特定のドメインに限定する
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 漢方データ
kampo_data = {
    "001": {"葛根": 3, "生姜": 2, "甘草": 1},
    "002": {"葛根": 2, "麻黄": 4, "甘草": 1},
    "003": {"桂枝": 3, "芍薬": 2, "甘草": 1}
}

# キーを整数化（"001" → "1" に変換）
normalized_kampo_data = {str(int(k)): v for k, v in kampo_data.items()}

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

@app.get("/")
def read_root():
    return {"message": "漢方APIが正常に動作しています！"}
