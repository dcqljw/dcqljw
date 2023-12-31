from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://root:Dcq.159357@8.210.229.44:3306/dcqljw?charset=utf8"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Dcq.159357@8.210.229.44:3306/dcqljw?charset=utf8"
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:dcq.159357@127.0.0.1:3306/dcqljw?charset=utf8"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
