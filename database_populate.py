from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create admin user
User1 = User(name="Ben Ho", email="ben13ho@hotmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Create new category
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()

item1 = Item(user_id=1, category=category1, name="Jersey", description="Awesome jersey!")

session.add(item1)
session.commit()

item1 = Item(user_id=1, category=category1, name="Pads", description="Very comfortable pads")

session.add(item1)
session.commit()

item1 = Item(user_id=1, category=category1, name="T-shirt", description="Fit and relaxing t-shirt")

session.add(item1)
session.commit()

# Create new category
category1 = Category(user_id=1, name="Basketball")

session.add(category1)
session.commit()

item1 = Item(user_id=1, category=category1, name="Shoes", description="Very slick shoes!")

session.add(item1)
session.commit()

# Create new category
category1 = Category(user_id=1, name="Baseball")

session.add(category1)
session.commit()

item1 = Item(user_id=1, category=category1, name="Gloves", description="Glove fits for all sizes")

session.add(item1)
session.commit()

# Create new category
category1 = Category(user_id=1, name="Frisbee")

session.add(category1)
session.commit()

item1 = Item(user_id=1, category=category1, name="Goal posts", description="Sturdy posts for ultimate frisbee")

session.add(item1)
session.commit()

# Create new category
category1 = Category(user_id=1, name="Snowboarding")

session.add(category1)
session.commit()

item1 = Item(user_id=1, category=category1, name="Snowboard", description="Snowboard fits for both men and women sizes")

session.add(item1)
session.commit()

# Create new category
category1 = Category(user_id=1, name="Rock Climbing")

session.add(category1)
session.commit()

item1 = Item(user_id=1, category=category1, name="Chalk", description="3 liters of chalk - great for outdoor activities!")

session.add(item1)
session.commit()


# Create new category
category1 = Category(user_id=1, name="Foosball")

session.add(category1)
session.commit()

item1 = Item(user_id=1, category=category1, name="Table", description="5 foot Foosball table.  Amazing fun!")

session.add(item1)
session.commit()


# Create new category
category1 = Category(user_id=1, name="Skating")

session.add(category1)
session.commit()

item1 = Item(user_id=1, category=category1, name="Skates", description="Size 10 Men's skates")

session.add(item1)
session.commit()


# Create new category
category1 = Category(user_id=1, name="Hockey")

session.add(category1)
session.commit()

item1 = Item(user_id=1, category=category1, name="Goalie pads", description="Junior size pads")

session.add(item1)
session.commit()


print "added catalog items!"