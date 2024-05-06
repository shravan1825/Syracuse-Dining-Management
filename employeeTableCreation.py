from sqlalchemy import create_engine, Column, Integer, String, Sequence
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

class Employee(Base):
    __tablename__ = 'employee'

    emp_SUID = Column(String(10), primary_key=True)
    fname = Column(String(50))
    lname = Column(String(50))
    email = Column(String(100), unique=True)
    password = Column(String(255))
    points = Column(Integer)
Base.metadata.bind = engine


Session = sessionmaker(bind=engine)
session = Session()


def add_employee_entry(emp_SUID, fname, lname, email, password, points):
    new_employee = Employee(emp_SUID=emp_SUID, fname=fname, lname=lname, email=email, password=password, points=points)
    session.add(new_employee)
    session.commit()

SUIDs = [891432969, 566811047, 154705819, 448825239, 243333892]
indian_names = ["Shravan Dharkar", "Khushi Shah", "Pratham Shetty", "Shweta Hiremath", "Gyana Harsha Meeli"]
email_ids =['sdharkar@syr.edu', 'khus@syr.edu', 'pshett01@syr.edu', 'skhirema@syr.edu', 'gharsh@syr.edu']
password = "Password12"
points = [7, 2, 2, 7, 4]


index_emp = 0
for i in SUIDs:

    add_employee_entry(i, indian_names[index_emp].split()[0], indian_names[index_emp].split()[1], email_ids[index_emp], password, points[index_emp])
    index_emp+=1

session.close()
