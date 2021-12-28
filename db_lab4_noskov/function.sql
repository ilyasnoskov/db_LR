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