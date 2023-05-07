import json
import os
import pandas as pd
import psycopg2
import sys

import dotenv #for the scrt ky
#import django_heroku
from pathlib import Path
import dj_database_url


vowels = ["a", "e", "i", "o", "u"]

dotenv_file = os.path.join('/home/fsmith/GeoRiddleGame/georiddle/', ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD' : os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)


conn = psycopg2.connect(
    host= os.environ['DATABASE_HOST'],
    user= os.environ['DATABASE_USER'],
    password= os.environ['DATABASE_PASSWORD'],
    database= os.environ['DATABASE_NAME'],
)
curr = conn.cursor()
area_rank = {}
lat_rank = {}
long_rank = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'

###############
#
# Riddles: Have created every version of North/South/Largest Area with starts, ends, includes, doesnt include a single letter from lengths 5-8
#

############


try:

    curr.execute("""SELECT name from geo_country2 gc order by population desc""")
    pop_desc_countries = curr.fetchall()

    curr.execute("""SELECT name from geo_country2 gc order by density desc""")
    density_desc = curr.fetchall()

    lines = []
    lengths = [5,6,7,8]
    countryset_length =5

    answers = []
    for country in pop_desc_countries:
        for letter in country[0].lower():
            if letter == 'f':
                answers.append(country[0])
                if len(answers) == 5:
                    break
                pass

        #if country[0].lower()[-1:] == 'e':
            # answers.append(country[0])
            # if len(answers) == 5:
            #     break
    print(answers)
    submit = input("submit this riddle?  ")

    if submit == 'y':
        try:
            curr.execute("""SELECT max(id) from geo_riddle gr""")
            riddle_id = curr.fetchone()
            for ans in answers:
                curr.execute("""INSERT INTO geo_riddle_answers (riddle_id, country2_id) VALUES(%s,%s) RETURNING id;""", [riddle_id, ans])
            
            conn.commit()
            print('Submitted')
        except Exception as exc:
            print("Error executing SQL: %s"%exc)


except Exception as exc:
    print("Error executing SQL: %s"%exc)



