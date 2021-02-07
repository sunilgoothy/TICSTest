import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('sqlite:///test.db', echo = False)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Employees(Base):
   __tablename__ = 'employees'
   
   eid = Column(Integer, primary_key=True)
   Name = Column(String)
   Address = Column(String)
   Phone = Column(String)
   Join_Date = Column(String)

   
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

for i in range(100001,1000001,1):
    name = 'Sunil'+str(i)
    join_date = datetime.datetime.strptime('2020-04-01 09:15:00.001', '%Y-%m-%d %H:%M:%S.%f')
    new_employee = Employees(Name=name, Phone=8888, Join_Date=join_date, Address='Bangalore')
    session.add(new_employee)
    # print(f"Added {name}")

session.commit()