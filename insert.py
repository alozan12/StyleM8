import psycopg2

def InsertShirt(shirtList):
    try:
        sql = "INSERT INTO shirt(shi_shirtid, shi_storeid, shi_shirtname, shi_shirtprice, shi_shirtsize, shi_shirtcolor, shi_necktype, shi_sleevetype, shi_shirtstyle, shi_shirtmaterial, shi_shirtrating, shi_description) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cur = conn.cursor()
        cur.execute(sql, shirtList)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Connect to the database
conn = psycopg2.connect(
    database="412Project",
    host='localhost',  
    port='5432'
)

conn.set_session(autocommit=True)

#tableToRead = input("enter table file: ")
#table = open(tableToRead, 'r')

table = open('sampleTables/shirts.tbl', 'r')

# Create a cursor
cur = conn.cursor()
cur.execute("SELECT shi_shirtID FROM shirt ORDER BY shi_shirtID DESC limit 1;")

# Fetch all the rows using a for loop
rows = cur.fetchall()
lastID = 0
for row in rows:
    id = row
    print(f"ID: {id}")
    lastID = id[0]
print(lastID)

shirtList = []
delimiter = '|'
for line in table:
    line = line.split(delimiter)
    line[0] = str(int(line[0]) + lastID + 1)
    line[11] = line[11].strip()
    print(line)
    InsertShirt(line)

# Define the data to be inserted
# data = [(1, 'John Doe'), (2, 'Jane Doe'), (3, 'Jim Doe')]

# Use a for loop to insert each row of data into the table
# for row in data:
#     sql = "INSERT INTO mytable (id, name) VALUES (%s, %s)"
#     cur.execute(sql, row)
 
# Commit the changes to the database
# conn.commit()
# print(f"{data}\nData is successfully inserted")
 
# Close the cursor and the connection
cur.close()
conn.close()