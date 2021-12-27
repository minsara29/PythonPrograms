from main import Session, engine, User
from sqlalchemy import select, update

# with Session(bind=engine) as session:
#     user = session.query(User) \
#                 .filter(User.name == "Kannan")\
#                 .first() # get one row
#                 # .all() # querying all
#
#     user.name = "Pranav"
#     session.commit()


with Session(bind=engine) as session:
    user = session.query(User) \
                .filter(User.name == "Kannan")\
                .first() # get one row
                # .all() # querying all

    user.name = "Pranav"
    session.commit()
