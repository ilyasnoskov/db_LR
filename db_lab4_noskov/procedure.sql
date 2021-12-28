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

select * from filtered_colleges