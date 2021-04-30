# モデルの定義
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

# userテーブルのモデルUserTableを定義
class UserTable():
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)

# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class User(BaseModel):
    id: int
    name: str
    age: int
