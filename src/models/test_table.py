# モデルの定義
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

# userテーブルのモデルUserTableを定義
class TestTable():
    __tablename__ = 'test_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)

# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class Test(BaseModel):
    id: int
    name: str
