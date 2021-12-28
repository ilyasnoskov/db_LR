import matplotlib.pyplot as plt
import psycopg2

username = 'iliasnoskov'
password = 'admin'
database = 'iliasnoskov_DB'
host = 'localhost'
port = '5432'

query_1_1 = '''
select count(p_height) from height where p_height >= 200 -- more 2 meters
'''
query_1_2 = '''
select count(p_height) from height where p_height < 200
'''

query_2 = '''
Select country, count(country)
	from players
	left join colleges on players.p_college = colleges.college
	group by country
'''

query_3 = '''
select p_college, count(p_college) from players
	group by p_college
'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(con))

with con:

    cur = con.cursor()

    print('1.  ')
    title = ["more 2 meters","less 2 meters"]
    info = []
    cur.execute(query_1_1)
    for row in cur:
        info.append(row[0])
    cur.execute(query_1_2)
    for row in cur:
        info.append(row[0])

    figure, (bar_ax, pie_ax, bar_2_ax) = plt.subplots(1, 3, figsize=(22,12))
    pie_ax.pie(info, labels=title, autopct='%1.1f%%')
    pie_ax.set_title('Кількість гігантських гравців')

    print("\n2. ")
    cur.execute(query_2)
    countryName = []
    counter = []
    for row in cur:
        print(row)
        countryName.append(row[0])
        counter.append(row[1])

    bar_ax.bar(countryName, counter, width=0.5)
    #bar_ax.set_xticklabels(countryName, rotation=35, ha='right')
    bar_ax.set_title('некрасиво бо мало даних в таблицях')
    bar_ax.set_ylabel("кількість гравців певної країни")

    print("\n3. ")
    cur.execute(query_3)

    college = []
    counter = []
    for row in cur:
        print(row)
        college.append(row[0])
        counter.append(row[1])

    bar_2_ax.bar(college, counter, width=0.5)
    bar_2_ax.set_xlabel('name college')
    bar_2_ax.set_ylabel("кількість")

    plt.show()
