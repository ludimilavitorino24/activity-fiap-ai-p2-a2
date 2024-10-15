-- @block Drop all tables

DO $$ 
DECLARE 
    r RECORD;
BEGIN 
    -- Loop through all tables in the current schema
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') 
    LOOP 
        -- Dynamically execute the drop statement
        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE'; 
    END LOOP; 
END $$;

-- @block Show DataLog data
SELECT * FROM t_wc_datalog;

-- @block Delete all DataLog data
DELETE FROM t_wc_datalog;

-- @block Insert a sample to 2024-10-15
INSERT INTO t_wc_datalog (id_animal_collar, temperature, heartrate, latitude, longitude, created_at, updated_at)
VALUES (31, 37.5, 80, 37.7749, -122.4194, '2024-10-15 00:00:00', '2024-10-15 00:00:00');

-- @block Query DataLog data

SELECT 
    id_datalog as id_datalog,
    species.id_species as id_species,
    species.name as species_name,
    breeds.id_breed as id_breed,
    breeds.name as breed_name,
    animals.id_animal as id_animal,
    animals.name as animal_name,
    datalog.id_animal_collar as id_animal_collar,
    cast(datalog.temperature as float) as temperature,
    cast(datalog.heartrate as float) as heartrate,
    cast(datalog.latitude as float) as latitude,
    cast(datalog.longitude as float) as longitude,
    datalog.created_at as created_at,
    datalog.updated_at as updated_at
FROM t_wc_datalog datalog
LEFT JOIN t_wc_animals_collars animal_collars ON datalog.id_animal_collar = animal_collars.id_animal_collar
LEFT JOIN t_wc_animals animals ON animal_collars.id_animal = animals.id_animal
LEFT JOIN t_wc_species species ON animals.id_species = species.id_species
LEFT JOIN t_wc_breeds breeds ON animals.id_breed = breeds.id_breed
WHERE datalog.created_at >= TO_DATE('2024-10-14','YYYY-MM-DD') AND datalog.created_at < TO_DATE('2024-10-14','YYYY-MM-DD') + INTERVAL '1' DAY;
