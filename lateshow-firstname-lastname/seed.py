import csv
from app import app, db
from models import Episode, Guest

with app.app_context():
    db.drop_all()
    db.create_all()

    with open('data/seed.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            episode = Episode(date=row['date'], number=row['number'])
            db.session.add(episode)
            guest = Guest(name=row['guest_name'], occupation=row['guest_occupation'])
            db.session.add(guest)
        db.session.commit()