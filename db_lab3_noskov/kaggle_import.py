import csv
import psycopg2

username = 'iliasnoskov'
password = 'admin'
database = 'iliasnoskov_DB'
host = 'localhost'
port = '5432'

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(con))

INPUT_CSV_FILE = 'nba.csv'

query_0 = '''
DELETE FROM height CASCADE;
DELETE FROM players CASCADE;
DELETE FROM colleges CASCADE;
'''

query_1 = '''
INSERT INTO colleges (p_college,country) VALUES (%s, %s)
'''
query_2 = '''
INSERT INTO players (p_id,p_name,p_college) VALUES (%s,%s, %s)
'''
query_3 = '''
INSERT INTO height (p_id,p_height) VALUES (%s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
    cur = conn.cursor()
    cur.execute(query_0)

    #first table
    colleges = []
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            if row['college'].rstrip() in colleges\
                    or row['college'] == ""\
                    or row['college'] == " "\
                    or row['college'] == None\
                    or row['college'] == 'None':
                continue
            else:
                colleges.append(row['college'].rstrip())
                values = (row['college'].rstrip(), row['country'])
                cur.execute(query_1, values)

    #second table
    colleges = []
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            if row['college'].rstrip() in colleges or row['college'] == "" or row['college'] == None or row['college'] == 'None':
                continue
            else:
                colleges.append(row['college'].rstrip())
                values = (row['id'], row['player_name'], row['college'] ) #'{0}{1}'.format(row['college'], ' '*(256-len(row['college'])))
                cur.execute(query_2, values)

    #third table
    colleges = []
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            if row['college'].rstrip() in colleges or row['college'] == "" or row['college'] == None or row['college'] == 'None':
                continue
            else:
                print(idx)
                colleges.append(row['college'].rstrip())
                values = (row['id'], int(float(row['player_height'])))
                cur.execute(query_3, values)

    conn.commit()