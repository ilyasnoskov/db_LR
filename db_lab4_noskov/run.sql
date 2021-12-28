CREATE OR REPLACE FUNCTION moreHeightPlayerInCountry(country_name varchar(256)) RETURNS int AS
$$
    DECLARE
        height integer;
    BEGIN
        select max(height.p_height) into height
		from players
	        join colleges on colleges.p_college = players.p_college
	        join height on height.p_id = players.p_id
	            where colleges.country = country_name;
        RETURN height;
    END;
$$ LANGUAGE 'plpgsql';

SELECT moreHeightPlayerInCountry('USA');
--в populate.sql тільки USA, тому при інших аргкментах функція не працює





CREATE OR REPLACE PROCEDURE filter_colleges_by_country(country_name varchar(250))
LANGUAGE 'plpgsql'
AS $$
BEGIN
	DROP TABLE IF EXISTS filtered_colleges;
	CREATE TABLE filtered_colleges
	AS
	(
	    select p_college, country from colleges
	    where  country = country_name
	);
END;
$$;

CALL filter_colleges_by_country('USA');

select * from filtered_colleges;






CREATE OR REPLACE FUNCTION replace_height()
RETURNS trigger AS
$$
	BEGIN
	    IF NEW.p_height = 2 THEN
            NEW.p_height = 200;
        END IF;
	        RETURN NEW;
	    END;
$$ LANGUAGE 'plpgsql';
DROP TRIGGER IF EXISTS insertHeight on height;

CREATE TRIGGER insertHeight
BEFORE UPDATE OR INSERT ON height
FOR EACH ROW
EXECUTE FUNCTION replace_height();

SELECT * FROM height;

update height
set p_height = 2
where p_id = 2;

SELECT * FROM height;