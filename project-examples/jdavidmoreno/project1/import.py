import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://nggwnvgfupsrjz:7c2041516ecbc9a607948829621da9eb6e8b7d58d6304aca7ee03f1c876ff5ae@ec2-54-221-212-15.compute-1.amazonaws.com:5432/d7hsdqrsa9hrsm"
)
db = scoped_session(sessionmaker(bind=engine))

def main():
    with open('books.csv') as file:
        file.readline()
        books = csv.reader(file)

        count = 0
        for isbn, name, author, year in books:

            if db.execute("SELECT id FROM author WHERE name = :author", {"author": author}).rowcount == 0:
                db.execute("INSERT INTO author (name) VALUES (:author)",  {"author": author})
                db.commit()
            author_id = db.execute("SELECT id FROM author WHERE name = :author", {"author": author}).fetchone()

            if db.execute("SELECT id FROM year WHERE year = :year", {"year": year}).rowcount == 0:
                db.execute("INSERT INTO year (year) VALUES (:year)",  {"year": year})
                db.commit()
            year_id = db.execute("SELECT id FROM year WHERE year = :year", {"year": year}).fetchone()

            db.execute("INSERT INTO books (isbn, title, author_id, year_id) VALUES (:isbn, :name, :author_id, :year_id)",
                      {"isbn": isbn, "name": name, "author_id": author_id.id, "year_id": year_id.id })

            print(count)
            count += 1
            db.commit()

if __name__ == "__main__":
    main()
