INSERT INTO public.geo_riddle_answers (riddle_id, country_id) VALUES(2074, (select id from geo_country gc where name = 'Luxembourg')) 