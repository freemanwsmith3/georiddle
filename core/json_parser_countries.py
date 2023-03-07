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
                
#curr.execute("""SELECT id, continent_id, cap
    # print(code)ital_id, name FROM public.geo_country where id = %s;""", [id,])
#country_data = curr.fetchone()

def upload_borders(curr, country_id, border_id):

    try:
        curr.execute("""INSERT INTO public.geo_country_borders ("from_country_id", "to_country_id") VALUES(%s, %s) RETURNING id;""", [country_id, border_id])
        conn.commit()
    except Exception as exc:
        print("Error executing SQL: %s"%exc)

def upload_country_langs(curr, country_id, lang_id):

    try:
        curr.execute("""INSERT INTO public.geo_country_languages ("country_id", "language_id") VALUES(%s, %s) RETURNING id;""", [country_id, lang_id])
        conn.commit()
    except Exception as exc:
        print("Error executing SQL: %s"%exc)

def upload_languages(curr, language):
    curr.execute("""SELECT id FROM public.geo_language where name = %s;""", [language,])
    language_id = curr.fetchone()
    if language_id is None:
        try:
            curr.execute("""INSERT INTO public.geo_language ("name") VALUES(%s) RETURNING id;""", [language,])
            language_id = curr.fetchone()
            conn.commit()
        except Exception as exc:
            print("Error executing SQL: %s"%exc)
    return(language_id)

def upload_currency(curr, currency):
    try:
        curr.execute("""SELECT id FROM public.geo_currency where name = %s;""", [currency,])
        currency_id = curr.fetchone()
    except Exception as exc:
        print("No currencty data")
        pass
    if currency_id is None:
        try:
            curr.execute("""INSERT INTO public.geo_currency ("name") VALUES(%s) RETURNING id;""", [currency,])
            currency_id = curr.fetchone()
            conn.commit()
        except Exception as exc:
            print("Error executing SQL: %s"%exc)
    return(currency_id)


def upload_regions(curr, region):
    curr.execute("""SELECT id FROM public.geo_region where name = %s;""", [region,])
    region_id = curr.fetchone()
    if region_id is None:
        try:
            curr.execute("""INSERT INTO public.geo_region ("name") VALUES(%s) RETURNING id;""", [region,])
            region_id = curr.fetchone()
            conn.commit()
        except Exception as exc:
            print("Error executing SQL: %s"%exc)
    return(region_id)


def upload_continent(curr, continent):
    curr.execute("""SELECT id FROM public.geo_continent where name = %s;""", [continent,])
    continent_id = curr.fetchone()
    if continent_id is None:
        try:
            curr.execute("""INSERT INTO public.geo_continent ("name") VALUES(%s) RETURNING id;""", [continent,])
            continent_id = curr.fetchone()
            conn.commit()
        except Exception as exc:
            print("Error executing SQL: %s"%exc)
    return(continent_id)


def upload_capitals(curr, capital):
    curr.execute("""SELECT id FROM public.geo_capital where name = %s;""", [capital,])
    capital_id = curr.fetchone()
    if capital_id is None:
        try:
            curr.execute("""INSERT INTO public.geo_capital ("name") VALUES(%s) RETURNING id;""", [capital,])
            capital_id = curr.fetchone()
            conn.commit()
        except Exception as exc:
            print("Error executing SQL: %s"%exc)
    return(capital_id)

def upload_countries(curr, name, capital_id, continent_id, region_id, currency_id, area, code, lat, long, landlocked ):
    curr.execute("""SELECT id FROM public.geo_country where name = %s;""", [name,])
    country_id = curr.fetchone()
    if country_id is None:
        try:
            curr.execute("""INSERT INTO public.geo_country ("name", "capital_id", "continent_id", "regions_id", "currency_id", "area", "code", "lat", "long", "landlocked") VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;""", [name, capital_id,continent_id, region_id, currency_id, area, code, lat, long, landlocked])
            country_id = curr.fetchone()
            conn.commit()
        except Exception as exc:
            print("Error executing SQL: %s"%exc)
    return(capital_id)

file_path = '/home/fsmith/GeoRiddleGame/georiddle/countries.json'

with open(file_path, 'r', encoding='utf-8-sig') as f:
    
    data = json.load(f,  )
languages = set()
regions = set()

name = ''
capital = ''
code = ''
region  = ''
continent_id = None
currency_id = None
landlocked = False


curr.execute("""SELECT id, "code" FROM public.geo_country; """)
country_set =  curr.fetchall()
country_dict = {}
for country in country_set:
    country_dict[country[1]] = country[0]

curr.execute("""SELECT id, "name" FROM public.geo_capital; """)
capital_set =  curr.fetchall()
capital_dict = {}
for capital in capital_set:
    capital_dict[capital[1]] = capital[0]

curr.execute("""SELECT id, "name" FROM public.geo_currency; """)
currency_set =  curr.fetchall()
currency_dict = {}
for currency in currency_set:
    currency_dict[currency[1]] = currency[0]


curr.execute("""SELECT id, "name" FROM public.geo_continent; """)
continent_set =  curr.fetchall()
continent_dict = {}
for continent in continent_set:
    continent_dict[continent[1]] = continent[0]


curr.execute("""SELECT id, "name" FROM public.geo_language; """)
language_set =  curr.fetchall()
language_dict = {}
for language in language_set:
    language_dict[language[1]] = language[0]

curr.execute("""SELECT id, "name" FROM public.geo_region; """)
region_set =  curr.fetchall()
region_dict = {}
lat = None
long = None
for region in region_set:
    region_dict[region[1]] = region[0]


for country in data:
    print("======================")
    
    #################### name ####################3
    name = country['name']['common']
    
    ############## code #################
    code = country['cca3']

    ############3 area ################3
    area = country['area']

    if country['latlng']:
        ################## latitude ##############
        lat = round(country['latlng'][0],2)

        ############### longitude ###############3
        long = round(country['latlng'][1],2)

    ##################### captial #################3

    capital = country['capital']
    capital_id = capital_dict.get(capital)
    ########### Continent #################
    if country['region'] == 'Americas':
        if country['subregion'] == 'South America': 
            continent = 'South America'
        else: 
            continent = 'North America'
    else:
        continent = country['region'] 
    continent_id = continent_dict.get(continent)
    ############# region #####################

    region = country['subregion']
    region_id = region_dict.get(region)
    ################### currency ##############33
    if country['currency'] != []:
        currency = country['currency'][0]
        currency_id = currency_dict.get(currency)
    ############# language ########################
    for lang in country['languages']:
        languages.add(country['languages'][lang])



    ############# landlocked ########################
    
    landlocked = country['landlocked']

    ############## borders ###################3

    borders = country['borders']


    print("Name: ", name)
    print("Capital_id: ", capital_id)
    print("continent_id: ", continent_id)
    print("region_id: ", region_id)
    print("currency_id: ", currency_id)
    print("area: ", area)
    print("code: ", code)
    print("lat: ", lat)
    print("long: ", long)
    print("landlocked: ", landlocked)

    for lang in country['languages']:
        print(lang)
        lang_id = language_dict.get(country['languages'][lang])
        upload_country_langs(curr, country_dict.get(code), lang_id)


    ############ uncomment these if you need to upload the individual stuff again ##############
    ########## doesn't affect it but slows it down because has to do a select statement ##################'
    # for bord in borders:

    #     print("bord", bord)
    #     upload_borders(curr, country_dict.get(code), country_dict.get(bord))

    #upload_countries(curr, name, capital_id, continent_id, region_id, currency_id, area, code, lat, long, landlocked)
    # upload_regions(curr, country['subregion'])
    # if country['currency'] != []:
    #     currency = country['currency'][0]
    #     print(currency)
    #     upload_currency(curr, currency)
    # upload_capitals(curr, capital)
    # upload_continent(curr, continent)
  
# for lang in languages:
#     upload_languages(curr, lang)

