from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import text


import src.config as config

def setup_db():
    user = config.DB_USER
    password = config.PASSWORD
    host = config.HOST
    db_name = config.DATABASE
    
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{db_name}')
    
    db_session = scoped_session(
        sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )
    )
    
    result = db_session.execute(text("SELECT * FROM users"))
    
    for row in result.mappings():
        print(row)

# テーブルを作成する
# Base = declarative_base()
# Base.query  = db_session.query_property()

# # テーブルを定義する
# # Baseを継承
# class Wine(Base):
#   """ワインの情報をもつCSVファイルのクラス

#   Args:
#       Base (_type_): DeclarativeBase
#   """
#   # テーブル名
#   __tablename__ = 'wines'
#   # カラムの定義
#   id = Column(Integer, primary_key=True, autoincrement=True)
#   wine_class = Column(Integer, unique=False)
#   alcohol = Column(Float, unique=False)
#   ash = Column(Float, unique=False)
#   hue = Column(Float, unique=False)
#   proline = Column(Integer, unique=False)
  
#   def __init__(self, wine_class=None, alcohol=None, ash=None, hue=None, proline=None):
#     self.wine_class = wine_class
#     self.alcohol = alcohol
#     self.ash = ash
#     self.hue = hue
#     self.proline = proline

# Base.metadata.create_all(bind=engine)
