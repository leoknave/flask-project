from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()
    
    user1 = User(name="John Doe", email="john@example.com")
    user2 = User(name="Jane Doe", email="jane@example.com")

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    print("Sample data inserted!")
