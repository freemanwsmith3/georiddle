SELECT gc.id, "name", capital_id, continent_id, regions_id, currency_id, area, code, lat, long, landlocked, count(gc.id)
FROM geo_country gc
full join geo_country_borders gcb ON gc.id = gcb.from_country_id 
group by gc.id
having count(gc.id) = 6
order by area 
