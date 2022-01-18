from main import Session, engine, User
from sqlalchemy import select

with Session(bind=engine) as session:
    users = session.query(User) \
                 .all()  # querying all
                # .filter(User.name == "Kannan") \
                #.first() # get one row


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d

for user in users:
    print(user.name)

for user in users:
    d = row2dict(user)
    print(d)


