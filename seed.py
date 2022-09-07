"""sample files"""

from models import Pet, db
from app import app

# create all tables
db.drop_all()
db.create_all()

Pet.query.delete()

p1 = Pet(name='Sprinkles', species='cat', age=13, notes='Ugly as hellll', available=True, photo_url='https://i.guim.co.uk/img/media/67f70805c64b8bdc45175068c5ec37f7d743987d/0_250_4255_2553/master/4255.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=265bdd10b9ee876d2e404c5631fbbaf3')
p2 = Pet(name='Sally', species='horse', age=5, notes='Is a horse', available=False, photo_url='https://cdn.britannica.com/96/1296-050-4A65097D/gelding-bay-coat.jpg')
p3 = Pet(name='Sindy with an S', species='meerkat', age=1, notes='Cute but may murder you', available=True, photo_url='https://qph.cf2.quoracdn.net/main-qimg-cce8fb119862327c9e3afa4eb8551212-lq')

db.session.add_all([p1,p2,p3])
db.session.commit()