from main import Session, engine, User
from sqlalchemy import select

with Session(bind=engine) as session:
    users = session.query(User) \
                 .all()  # querying all
                # .filter(User.name == "Kannan") \
                #.first() # get one row


for user in users:
    print(user.name)
