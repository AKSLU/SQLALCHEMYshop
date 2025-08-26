from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    category = Column(String)
    article = Column(String)

    def __repr__(self):
        return f"Product(id={self.id}, price={self.price}, category='{self.category}', article='{self.article}')"

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ur_address = Column(String)

    def __repr__(self):
        return f"Store(id={self.id}, name='{self.name}', ur_address='{self.ur_address}')"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"

engine = create_engine('sqlite:///example.db', echo=False)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

def add_user(username, email):
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    print(f"Добавлен: {user}")

def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"delate: {user}")
    else:
        print("user не найден")


if __name__ == "__main__":
    p1 = Product(price=200, category="Food", article="A1")
    p2 = Product(price=60, category="Cundy", article="A2")
    session.add_all([p1, p2])


    s1 = Store(name="Shop1", ur_address="adress1")
    session.add(s1)


    add_user("akslu1", "akslu@1")
    add_user("akslu2", "akslu@2")

    session.commit()
    delete_user(1)


    print("All products:")
    for p in session.query(Product).all():
        print(p)


    print("All shops:")
    for s in session.query(Store).all():
        print(s)


    print("all users:")
    for u in session.query(User).all():
        print(u)

