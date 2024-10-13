from sqlalchemy import create_engine, MetaData
from eralchemy import render_er

engine = create_engine('sqlite:///db.sqlite3')
metadata = MetaData()
metadata.reflect(bind=engine)

# Create the ERD
render_er(metadata, 'erd_diagram.png')