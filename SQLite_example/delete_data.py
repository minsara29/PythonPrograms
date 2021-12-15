from main import Session, engine, User
from sqlalchemy import select, delete

with Session(bind=engine) as session:
    user = session.query(User) \
                .filter(User.name == "Pranav")\
                .first() # get one row
                # .all() # querying all


    session.delete(user)
    session.commit()
