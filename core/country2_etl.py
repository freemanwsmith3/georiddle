import json
import os
import pandas as pd
import psycopg2
import sys

import dotenv #for the scrt ky
#import django_heroku
from pathlib import Path
import dj_database_url




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
                

df = pd.read_csv(r'/home/fsmith/GeoRiddleGame/georiddle/core/sporcle.csv')

to_db = [(
    row['Name'],
    row['Continent'],
    row['Capital'],
    row['Population'],
    row['Density'],
    row['Area'],
    row['Lat'],
    row['Long'],
)
for index, row in df.iterrows()]

curr.executemany("INSERT INTO geo_country2 (name, continent, capital, population, density, area, lat, long) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", to_db)

conn.commit()
