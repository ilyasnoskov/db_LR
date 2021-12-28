create table collegescopy as select * from colleges;
delete from collegescopy;
select * from collegescopy;

DO $$
DECLARE
    collegeName collegescopy.p_college%TYPE;
    countryName collegescopy.country%TYPE;


BEGIN
    collegeName := '))';
    countryName := 'iloveU';
    FOR i IN 1..10
        LOOP
            INSERT INTO collegescopy(p_college, country)
            VALUES (CONCAT(2*i , collegeName),CONCAT(3*i , countryName));
        END LOOP;
END;
$$