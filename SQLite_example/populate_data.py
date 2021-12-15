from main import Session, User, engine


local_session = Session(bind=engine)

new_user = User(
    name="kannan",
    email="kannan.Kannan@gmail.com"
)

#
# local_session.add(new_user)
#
# local_session.commit()

with Session(bind=engine) as session:
    session.add(new_user)
    session.commit()