from main import Session, engine, User
from sqlalchemy import select, desc

with Session(bind=engine) as session:
    users = session.query(User) \
        .order_by(User.name) \
        .all()  # querying all
    # .order_by(desc(User.name)) \
    # .filter(User.name == "Kannan") \
    # .first() # get one row

for user in users:
    print(user.name)
