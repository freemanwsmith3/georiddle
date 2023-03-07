import os
import pandas as pd
import psycopg2
import sys

import dotenv #for the scrt ky
#import django_heroku
from pathlib import Path
import dj_database_url


def country_select(id):

    conn = psycopg2.connect(
        host= os.environ['DATABASE_HOST'],
        user= os.environ['DATABASE_USER'],
        password= os.environ['DATABASE_PASSWORD'],
        database= os.environ['DATABASE_NAME'],
    )
    curr = conn.cursor()
                    
    curr.execute("""SELECT id, continent_id, capital_id, name FROM public.geo_country where id = %s;""", [id,])
    country_data = curr.fetchone()
    return country_data


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
print(country_select(1))


def upload_capitals(self, capital):
    self.curr.execute("""SELECT id FROM public.geo_capital where name = %s;""", [capital,])
    capital_id = self.curr.fetchone()
    return(capital_id)