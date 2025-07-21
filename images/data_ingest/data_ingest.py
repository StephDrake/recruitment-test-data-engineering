import csv
import mysql.connector

# creates live connection to server (database)
conn=mysql.connector.connect(
    host='database',
    user='codetest',
    password='swordfish',
    database='codetest'
)

# used to run SQL queries
cursor = conn.cursor()

with open('/data/places.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute(
            'INSERT INTO places (city, county, country) VALUES (%s, %s, %s)',
            (row['city'], row['county'], row['country'])
        )

# commit the queries or wont execute
conn.commit()

with open('/data/people.csv', encoding='utf-8') as f:
    reader=csv.DictReader(f)
    for row in reader:
        cursor.execute('SELECT id FROM places WHERE city = %s', (row['place_of_birth'], ))

        # gets next row of query result, returns tuple (eg. (1,))
        result = cursor.fetchone()
        if result:
            place_id = result[0]
            cursor.execute(
                'INSERT INTO people (given_name, family_name, date_of_birth, place_id) VALUES (%s, %s, %s, %s)',
                (row['given_name'], row['family_name'], row['date_of_birth'], place_id)
            )
        else:
            print(f"City: {row['place_of_birth']} not found in places")
            
# commit changes to database and close cursor and connection engine
conn.commit()
cursor.close()
conn.close()

#winpty docker exec -it recruitment-test-data-engineering-database-1 mysql -u codetest -p
# to run sql in gitbash - find docker ps and the name of mysql container
