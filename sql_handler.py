from sqlalchemy import create_engine, Column, Integer, String, Sequence, DateTime, Boolean, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import random

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

class MasterShiftsRecord(Base):
    __tablename__ = 'master_shifts_record'

    emp_SUID = Column(Integer, primary_key=True)
    shift1 = Column(DateTime)
    shift2 = Column(DateTime)
    shift3 = Column(DateTime)
    shift4 = Column(DateTime)
    shift5 = Column(DateTime)
    shift6 = Column(DateTime)
    shift7 = Column(DateTime)
    shift1_sub_status = Column(Boolean)
    shift2_sub_status = Column(Boolean)
    shift3_sub_status = Column(Boolean)
    shift4_sub_status = Column(Boolean)
    shift5_sub_status = Column(Boolean)
    shift6_sub_status = Column(Boolean)
    shift7_sub_status = Column(Boolean)
    # temp_shift1 = Column(DateTime)
    # temp_shift2 = Column(DateTime)
    # temp_shift3 = Column(DateTime)



class SubBinder(Base):
    __tablename__ = 'sub_binder'
    pkpk = Column(Integer, primary_key=True)
    shift_owner = Column(Integer, primary_key=False)
    subs_id = Column(Integer, primary_key=False)
    shift_datetime = Column(DateTime, primary_key=False)

class Admin(Base):
    __tablename__ = 'admins'

    admin_id = Column(Integer, primary_key=True)
    fname = Column(String(255))
    lname = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))

Base.metadata.bind = engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def subbing_a_shift(suid, shift):
    record = session.query(MasterShiftsRecord).get(suid)
    return record

def drop_to_null(suid, colname):
    # Update the value to None
    if colname == 'shift1':
        session.execute(update(MasterShiftsRecord).where(MasterShiftsRecord.emp_SUID == suid).values(shift1=None))
    if colname == 'shift2':
        session.execute(update(MasterShiftsRecord).where(MasterShiftsRecord.emp_SUID == suid).values(shift2=None))
    if colname == 'shift3':
        session.execute(update(MasterShiftsRecord).where(MasterShiftsRecord.emp_SUID == suid).values(shift3=None))
    if colname == 'shift4':
        session.execute(update(MasterShiftsRecord).where(MasterShiftsRecord.emp_SUID == suid).values(shift4=None))
    if colname == 'shift5':
        session.execute(update(MasterShiftsRecord).where(MasterShiftsRecord.emp_SUID == suid).values(shift5=None))
    if colname == 'shift6':
        session.execute(update(MasterShiftsRecord).where(MasterShiftsRecord.emp_SUID == suid).values(shift6=None))
    if colname == 'shift7':
        session.execute(update(MasterShiftsRecord).where(MasterShiftsRecord.emp_SUID == suid).values(shift7=None))
    session.commit()

def add_to_subbinder(addedby, shift_details):
    pkpk = random.randint(1,9999)
    data_to_add = {'shift_owner':None, 'subs_id':addedby, 'shift_datetime':shift_details, 'pkpk':pkpk}
    with sessionmaker(bind=engine)() as session:
        sub_binder_instance = SubBinder(**data_to_add)

        session.add(sub_binder_instance)
        session.commit()
        return("Sub successful")


def add_to_schedule(addedby, shift_details):
    
    with sessionmaker(bind=engine)() as session:
        # Retrieve the record by primary key
        record_to_update = session.query(MasterShiftsRecord).get(addedby)

        # Update the shift7 column with the current timestamp
        record_to_update.shift6 = shift_details

        # Commit the changes to the database
        session.commit()




def get_employee_by_email(email):
    with Session() as session:
        return session.query(Employee).filter_by(email=email).first()
        
def get_employee_by_suid(suid):
    with Session() as session:
        return session.query(Employee).filter_by(emp_SUID=suid).first()
def get_admin_by_email(email):
    with Session() as session:
        return session.query(Admin).filter_by(email=email).first()

def update_points(suid, new_pts):
    with sessionmaker(bind=engine)() as session:
        record = session.query(Employee).filter_by(emp_SUID=suid).first()
        if record:
            # Update the column value
            record.points = new_pts

            # Commit the changes
            session.commit()


def get_all_employee_elements():
    with sessionmaker(bind=engine)() as session:
        # Query all elements from the specified table
        all_elements = session.query(Employee).all()

        # Print or process the retrieved records
        return all_elements
        # for element in all_elements:
        #     print(element.__dict__)

def sqlalchemy_object_to_dict(obj):
    return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}


def get_shifts_from_suid(suid):
    with Session() as session:
        record = session.query(MasterShiftsRecord).get(suid)
        # print(record.shift1)
        return sqlalchemy_object_to_dict(record)
    
def get_sub_binder_data(sub_name):
    with Session() as session:
        record = session.query(SubBinder).get(sub_name)
        # print(record.shift1)
        if record == None:
            return None
        return sqlalchemy_object_to_dict(record)

def get_id_from_email(email):
    result = session.query(Employee.emp_SUID).filter(Employee.email == email).scalar()
    return result

def get_all_subShifts():
    with Session() as session:

        records = session.query(SubBinder).all()

        # Organize the records into a list of lists
        result_list = []
        for record in records:
            if record == None:
                pass
            else:

                result_list.append([record.subs_id, record.shift_owner,record.shift_datetime ] ) 
                print(result_list)
        return result_list