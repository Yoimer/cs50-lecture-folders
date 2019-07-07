import os
import csv
import psycopg2

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

with open('zips.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        print(row)
        db.execute("INSERT INTO LOCATIONS (zipcode, city, state, lat, long, population) VALUES (:zipcode, :city, :state, :lat, :long, :population)", {"zipcode": row[0], "city": row[1], "state": row[2], "lat": row[3], "long": row[4], "population": row[5]})
db.commit()

# cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
#db.execute("INSERT INTO LOCATIONS (zipcode, city, state, lat,
#  long, population) VALUES (:zipcode, :city, :state, :lat, :long, :population)",
#            {"zipcode": col1, "city": col2, "state": col3, "lat": col4, "long": col5, "population": col6})

#f = open(r'C:\Users\n\Desktop\data.csv', 'r')
#cur.copy_from(f, temp_unicommerce_status, sep=',')
#f.close()