import csv
import psycopg2

username = 'iliasnoskov'
password = 'admin'
database = 'iliasnoskov_DB'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

csv_out = 'nbaOUT.csv'

with conn:
    cur = conn.cursor()
    cur.execute('''
        select * from players
	        join colleges on colleges.p_college = players.p_college
	        join height on height.p_id = players.p_id
        ''')
    fields = [x[0] for x in cur.description]
    with open(csv_out, 'w') as outfile:
        csv.writer(outfile).writerow(fields)
        for row in cur:
            csv.writer(outfile).writerow([str(x) for x in row])