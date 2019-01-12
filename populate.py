#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurants.db')
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


# Menu for Billy's Burger
restaurant1 = Restaurant(name="Billys' Burger")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Chili Cheese Fries", description="Thick cut steak fries loaded with our famous homemade chili and natural cheddar cheese with jalapenos", price="$8.99", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Bacon Burger", description="Juicy grilled sirloin patty with bacon piled on top", price="$9.50", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Chicken Breast BLT", description="Juicy grilled chicken breast with bacon, tomato, lettuce, and mayo", price="$5.50", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Double Chocolate Cake", description="Freshly baked and served with Chocolate ice cream", price="$3.99", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

# Menu for Hanks' Bistro
restaurant2 = Restaurant(name="Hanks' Bistro")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Goat Cheese Bruschetta", description="Toasted baguettes with a thin layer of Goat cheese topped with bruschetta tomatoes, Parmesan cheese and fresh basil",
                     price="$7.99", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    name="Chipotle Chicken Wrap", description="Crispy chicken, salsa, corn, lettuce, onions, pepper jack and cheddar cheese topped with Chipotle dressing on a whole wheat wrap", price="$9.99", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Lobster Raviolis", description="Lobster and cheese filled raviolis with Roma tomatoes and baby spinach tossed in a lemon cream sauce", price="$19.99", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Tiramisu", description="A luxurious Italian dessert consisting of alternating layers of lady fingers and mascarpone cheese soaked in espresso with a hint of Kahlua", price="$6.99", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

print "Added new items!"
