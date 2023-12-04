import psycopg2



def MyCloset(memberID):
    try: 
        conn = psycopg2.connect(
        database="412Project",
        host='localhost',  
        port='5432'
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM outfit, closet WHERE o_closetid = c_closetid AND c_memberid = %(memberID)s", {"memberID": memberID})
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def FindYourOutfit():
    # returns as list of 12 items
    try:
        conn = psycopg2.connect(
        database="412Project",
        host='localhost',  
        port='5432'
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM shirt LIMIT 4")
        rows = cur.fetchall()
        cur.execute("SELECT * FROM pants LIMIT 4")
        rows = rows + cur.fetchall()
        cur.execute("SELECT * FROM shoes LIMIT 4")
        rows = rows + cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def GetAllShirts():
    try:
        conn = psycopg2.connect(
            database="412Project",
            host='localhost',  
            port='5432'
            )
        cur = conn.cursor()
        cur.execute("SELECT * FROM shirt LIMIT 100")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def GetAllPants():
    try:
        conn = psycopg2.connect(
            database="412Project",
            host='localhost',  
            port='5432'
            )
        cur = conn.cursor()
        cur.execute("SELECT * FROM pants LIMIT 100")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def GetAllShoes():
    try:
        conn = psycopg2.connect(
            database="412Project",
            host='localhost',  
            port='5432'
            )
        cur = conn.cursor()
        cur.execute("SELECT * FROM shoes LIMIT 100")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def GetShirt(shirtID):
    try:
        conn = psycopg2.connect(
            database="412Project",
            host='localhost',  
            port='5432'
            )
        cur = conn.cursor()
        cur.execute("SELECT * FROM shirt, store WHERE shi_shirtid = %(shirtID)s AND s_storeid = shi_storeid", {"shirtID": shirtID})
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def GetPants(pantsID):
    try:
        conn = psycopg2.connect(
            database="412Project",
            host='localhost',  
            port='5432'
            )
        cur = conn.cursor()
        cur.execute("SELECT * FROM pants, store WHERE p_pantsid = %(pantsID)s AND s_storeid = p_storeid", {"pantsID": pantsID})
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def GetShoes(shoesID):
    try:
        conn = psycopg2.connect(
            database="412Project",
            host='localhost',  
            port='5432'
            )
        cur = conn.cursor()
        cur.execute("SELECT * FROM shoes, store WHERE sho_shoesid = %(shoesID)s AND s_storeid = sho_storeid", {"shoesID": shoesID})
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def CreateAccount(username):
    try:
        conn = psycopg2.connect(
            database="412Project",
            host='localhost',  
            port='5432'
            )
        cur = conn.cursor()
        cur.execute("INSERT INTO member VALUES(1000, %(username)s, 1, 0)")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

rows = CreateAccount("TEST")
for row in rows:
    print(row)
