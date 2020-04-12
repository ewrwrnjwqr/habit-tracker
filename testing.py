#!/usr/bin/python3

from firebase import Firebase

config = {
  "apiKey": "AIzaSyDkkiDWhsRhnTVGzAP38UmVVd-lCZkJkZ8",
  "authDomain": "habit-tracking-dfbc2.firebaseapp.com",
  "databaseURL": "https://habit-tracking-dfbc2.firebaseio.com/",
  "storageBucket": "habit-tracking-dfbc2.appspot.com"
}

firebase = Firebase(config)

db = firebase.database()

usernames = db.child("users").get()
for user in usernames.each():
    print(user.val()[2])

