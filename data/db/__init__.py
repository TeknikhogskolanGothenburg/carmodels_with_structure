import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from .db_config import *

engine = sqlalchemy.create_engine(
    f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

Base = automap_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

Base.prepare(engine, reflect=True)
