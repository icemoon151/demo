import psycopg2

conn = psycopg2.connect(host='localhost', database="hw04", user="dbo", password="123456")

cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS hw_a;
CREATE TABLE IF NOT EXISTS hw_a(
    sn    INTEGER,
    name  VARCHAR,
    PRIMARY KEY(sn)
);

''')

ins_sql = 'INSERT INTO hw_a (sn, name) VALUES (%s, %s)'
for i in range(10,60,10):
    sn=i
    name='A%d' % sn
    cur.execute(ins_sql, (sn, name) )

ass = conn.cursor()
ass.execute('''
DROP TABLE IF EXISTS hw_b;
CREATE TABLE IF NOT EXISTS hw_b(
    sn    INTEGER,
    name  VARCHAR,
    PRIMARY KEY(sn)
);

''')

ins_sql = 'INSERT INTO hw_b (sn, name) VALUES (%s, %s)'
for j in range(40,80,10):
    sn=j
    name='B%d' % sn
    cur.execute(ins_sql, (sn, name) )

conn.commit()
