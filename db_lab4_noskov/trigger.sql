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