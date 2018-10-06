import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():

    # Open a file using Python's CSV reader.
    f = open("flights.csv")
    reader = csv.reader(f)

    # Iterate over the rows of the opened CSV file.
    for row in reader:

        # Execute database queries, one per row; then print out confirmation.
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:x, :y, :z)",
                    {"x": row[0], "y": row[1], "z": row[2]})
        print(f"Added flight from {row[0]} to {row[1]} lasting {row[2]} minutes.")

    # Technically this is when all of the queries we've made happen!
    db.commit()

if __name__ == "__main__":
    main()
