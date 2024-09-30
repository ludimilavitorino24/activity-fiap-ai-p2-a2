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
