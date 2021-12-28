import json
import psycopg2

username = 'iliasnoskov'
password = 'admin'
database = 'iliasnoskov_DB'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

query = '''
select * from players
	join colleges on colleges.p_college = players.p_college
	join height on height.p_id = players.p_id	
'''

data = {}
with conn:
    cur = conn.cursor()
    cur.execute(query)
    rows = []
    fields = [x[0] for x in cur.description]
    for row in cur:
      rows.append(dict(zip(fields, row)))
    data = rows

with open('nbaOUT.json', 'w') as json_out:
  json.dump(data, json_out, default=str)