

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
 

user = 'root'
password = 'shrashra12'
host = '127.0.0.1'
port = 3306
database = 'OrgFlow'

engine = create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
)

Base = declarative_base()

class Admin(Base):
    __tablename__ = 'admins'

    admin_id = Column(Integer, primary_key=True)
    fname = Column(String(255))
    lname = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


def add_admin_entry(admin_id, fname, lname, email, password):
    entry = Admin(admin_id=admin_id, fname=fname, lname=lname, email=email, password=password)
    session.add(entry)
    session.commit()

add_admin_entry(admin_id=1, fname='shra', lname='V', email='abcdefg@syr.edu', password='password12')


session.close()