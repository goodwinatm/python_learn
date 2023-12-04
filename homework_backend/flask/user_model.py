from sqlalchemy import *
from sqlalchemy.orm import declarative_base, sessionmaker, Session

Base = declarative_base()

engine = create_engine("sql:///test.db")

DBSession = sessionmaker(bind=engine)
db_session: Session = DBSession()

class User(Base):
    __tablename__="user"
    id = Column(Integer,primary_key=True)
    username = Column(String(20),default=None,nullable=False,comment="用户姓名")
    password = Column(String(20),default=None,nullable=False,comment="用户密码")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    #print(db_session.query(User).all())
    # user = User(username="zs",password="123")
    # db_session.add(user)
    # db_session.commit()
