from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

database = "postgresql"
dialect = "psycopg2"
username = "mateusholanda"
password = "123456"
database_url = "localhost"
port = "5432"
db_name = "test"

# f"postgresql+psycopg2://mateusholanda:123456@localhost:5432/test"
engine = create_engine(
  f"{database}+{dialect}://{username}:{password}@{database_url}:{port}/{db_name}"
)

session = Session(engine)

Base = declarative_base()