from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import datetime
app = FastAPI()

# 허용할 도메인 (여기에 클라이언트 도메인을 추가)
origins = [
    "http://127.0.0.1:5500",  # 로컬 클라이언트 도메인 (현재 브라우저가 있는 도메인)
]

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 허용할 도메인 목록
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST, etc.)
    allow_headers=["*"],   # 모든 헤더 허용
)
class acc_(BaseModel):
    id : str
    category : str
    date : str

anomaly_list = ["None"]


@app.get("/get_acc")
def get_item():
    de_dict = {
            "label": "G",
            "name": "펜스 A",
            "lat": 37.527462,
            "lng": 127.018122,
            "description": anomaly_list[-1],
        }
    print(de_dict)
    return de_dict



# Fence_damage
@app.post("/acc")
async def create_item(item: acc_):
    item_dict = item.dict()
    str_idict = f"{item_dict["date"]} : {item_dict["id"]}_Anomaly Detected"
    anomaly_list.append(str_idict)
    print(str_idict)
    return 0