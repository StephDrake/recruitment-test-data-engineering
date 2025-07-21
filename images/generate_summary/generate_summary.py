import mysql.connector
import json 

# creates live connection to server (database)
conn=mysql.connector.connect(
    host='database',
    user='codetest',
    password='swordfish',
    database='codetest'
)

# used to run SQL queries
cursor = conn.cursor()
cursor.execute("SELECT places.country, COUNT(*) as count FROM people JOIN places ON people.place_id = places.id GROUP BY places.country")

rows  = cursor.fetchall()
summary = [{country : count} for country, count in rows]

with open('/data/summary_output', 'w', encoding ='utf-8') as f:
    json.dump(summary, f)

cursor.close()
conn.close()