from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, DATETIME, create_engine
from datetime import datetime

connection_str = "sqlite:///C:\\Users\\ktamilraj\\Documents\\GitHub\\PythonPrograms\\SQLite_example\\example.db"

Base = declarative_base()

engine = create_engine(connection_str, echo=True)
Session = sessionmaker()

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    created_at = Column(DATETIME(), default=datetime.now())

    def __repr__(self):
        return f"<Users name={Users.name} email={Users.email}>"


#User.__tablename__
#User.__table__ # table metadata

