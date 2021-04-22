# モデルの定義
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
import db_connection

# userテーブルのモデルUserTableを定義
class UserTable(db_connection.my_sql.Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)

# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class User(BaseModel):
    id: int
    name: str
    age: int

def main():
    # テーブルが存在しなければ、テーブルを作成
    db_connection.my_sql.Base.metadata.create_all(bind=db_connection.my_sql.ENGINE)

if __name__ == "__main__":
    main()