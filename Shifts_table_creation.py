from sqlalchemy import create_engine, Column, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import random

from sqlalchemy import create_engine
 
# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = 'shrashra12'
host = '127.0.0.1'
port = 3306
database = 'OrgFlow'
 
# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT

engine = create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
)


Base = declarative_base()

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
    temp_shift1 = Column(DateTime)
    temp_shift2 = Column(DateTime)
    temp_shift3 = Column(DateTime)

Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to add entries to the master_shifts_record table
def add_shift_entry(emp_SUID, shift1, shift2, shift3, shift4, shift5, shift6, shift7,
                    shift1_sub_status, shift2_sub_status, shift3_sub_status, shift4_sub_status,
                    shift5_sub_status, shift6_sub_status, shift7_sub_status,
                    temp_shift1, temp_shift2, temp_shift3):
    entry = MasterShiftsRecord(
        emp_SUID=emp_SUID,
        shift1=shift1, shift2=shift2, shift3=shift3, shift4=shift4, shift5=shift5, shift6=shift6, shift7=shift7,
        shift1_sub_status=shift1_sub_status, shift2_sub_status=shift2_sub_status,
        shift3_sub_status=shift3_sub_status, shift4_sub_status=shift4_sub_status,
        shift5_sub_status=shift5_sub_status, shift6_sub_status=shift6_sub_status, shift7_sub_status=shift7_sub_status,
        temp_shift1=temp_shift1, temp_shift2=temp_shift2, temp_shift3=temp_shift3
    )
    session.add(entry)
    session.commit()

# List of emp_SUIDs
emp_SUIDs = [891432969, 566811047, 154705819, 448825239, 243333892]

# Add entries for each emp_SUID
for emp_SUID in emp_SUIDs:
    # Generate random day and time values for each shift between 7 AM and 10 PM
    shift1 = datetime.now() + timedelta(days=random.randint(0, 6), hours=random.randint(7, 22))
    shift2 = shift1 + timedelta(hours=random.randint(1, 6))  # Ensuring shift2 is at least 1 hour after shift1
    shift3 = shift2 + timedelta(hours=random.randint(1, 6))
    shift4 = shift3 + timedelta(hours=random.randint(1, 6))
    shift5 = shift4 + timedelta(hours=random.randint(1, 6))
    shift6 = shift5 + timedelta(hours=random.randint(1, 6))
    shift7 = shift6 + timedelta(hours=random.randint(1, 6))

    add_shift_entry(
        emp_SUID=emp_SUID,
        shift1=shift1, shift2=shift2, shift3=shift3, shift4=shift4, shift5=shift5, shift6=shift6, shift7=shift7,
        shift1_sub_status=False, shift2_sub_status=False, shift3_sub_status=False, shift4_sub_status=False,
        shift5_sub_status=False, shift6_sub_status=False, shift7_sub_status=False,
        temp_shift1=None, temp_shift2=None, temp_shift3=None
    )

# Close the session
session.close()