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
    #GET AREA RANK
    curr.execute("""SELECT name, lat, id from geo_country gc where landlocked = True""")
    area_order = curr.fetchall()
    lines = []
    lengths = [5,6,7,8]
    countryset_length =5

    question_details = ' LANDLOCKED countries that have DOUBLE LETTERS (same letter twice in a row) '
    question= "Name the " + str(countryset_length) + question_details 
    # question += "'"
    filename = "Name the " + question_details
    path = filename + '.txt'
    
    count=0
    ### for finding letter patterns in the words
    country_ids = []
    countries_to_write = ', '
    def all_vowels_same(word):
        vowels = "aeiou"
        vowel_set = set([char.lower() for char in word if char.lower() in vowels])
        return len(vowel_set) == 1

        vowels = "aeiou"
        count = 0
        for char in word:
            if char.lower() in vowels:
                count += 1
                if count > 1:
                    return False
        return count == 1
    for country in area_order:
        if country[0] != 'Heard Island and McDonald Islands' and country[0]!='Jersey':
            if all_vowels_same(country[0]):
               print(country[0])
            # for letter in country[0]:
            #     if letter in vowels:
            #         vowel_count+=1
            # if vowel_count <3:
            #     print(country[0])
            #     print(vowel_count)

    ###################
    # This is for getting countries based off a geographical feature and with one letter quality
    ################


    # for og_country_set in lengths:
    #     country_set = og_country_set



        # try:
        #     os.remove('riddles.txt')
        # except Exception as e:
        #     print(e)


        # for letter in alphabet:

        #     ## this part is for generating the question and file that will be used to save as a txt and for inserting to the riddle db
        #     question_details = 'countries CLOSEST to the equator that do NOT INCLUDE the letter '
        #     question= "Name the " + question_details + "'" + letter.upper()
        #     question += "'"
        #     filename = "Name the " + str(og_country_set) + ' ' + question_details
        #     path = filename + '.txt'
            
        #     ###
        #     i =0
        #     count = 0
        #     countries_to_write = ''
        #     country_ids = []
        #     for country in area_order:
        #         if country[0] != 'Heard Island and McDonald Islands' and country[0]!='Jersey':
        #             if letter not in country[0].lower():
        #                 count+=1
        #                 if count <= country_set:
        #                     print(country[0])
        #                     countries_to_write += country[0]
        #                     countries_to_write += ', '
        #                     country_ids.append(country[2])
        #                 #area_rank[i]=country[0]
        #             i+=1

#################### Where you can write riddles to db and to txt file ###########################


        #     if country_set == len(country_ids):
                
    # curr.execute("""INSERT INTO public.geo_riddle (question) VALUES(%s) RETURNING id;""", [question])
    # riddle_id = curr.fetchone()[0]
    # print(riddle_id)
    # for id in country_ids:
    #     # try:
    #     curr.execute("""INSERT INTO public.geo_riddle_answers (riddle_id, country_id) VALUES(%s, %s);""", [riddle_id, id])   

        # conn.commit()
        #print("Name the " + str(counftry_set) + ' biggest countries that start with the letter ' + letter)  


        #print("Name the %s biggest countries that include the letter '%s", [country_set, letter])    
    # lines.append(str(riddle_id) + ': ' + question)
    # lines.append('------------')
    # lines.append(countries_to_write)
    # lines.append('============')
    #     # else:
    #     #     print("Culprit: ", letter, ' ', len(country_ids))

            
    # with open(path, 'w') as f:
        
    #     f.write('\n'.join(lines))

    # curr.execute("""SELECT name, area, id, lat from geo_country gc order by lat desc""")
    # lat_order = curr.fetchall()
    # i =0
    # for country in lat_order:
    #     i+=1
    #     # if 'q' in country[0].lower():
    #     #     print(i)
    #     #     print(country[3])
    #     #     print(country[0])
    #     #     print("ID: ", country[2])
    #     #     print('============')
    #     lat_rank[i]=country[0]

    # curr.execute("""SELECT name, area, id from geo_country gc order by long desc""")
    # long_order = curr.fetchall()
    # i =0
    # for country in long_order:
    #     i+=1

    #     long_rank[i]=country[0]

    # #### Getting word stuff



    # curr.execute("""SELECT name, count(gc.id), gc.id
    # FROM geo_country gc
    # full join geo_country_borders gcb ON gc.id = gcb.from_country_id 
    # group by gc.id
    # """)
    # borders = curr.fetchall()
    # # for bord in borders: 
    # #     if bord[1] == 2 and len(bord[0])<7:
    # #         print(bord[2])
    # #         print(bord[0])

        
    # # for country in area_order:
    # #     #print(country[0])
    # #     vowel_count = 0
    # #     for letter in country[0]:
    # #         if letter in vowels:
    # #             vowel_count+=1
        
except Exception as exc:
    print("Error executing SQL: %s"%exc)



