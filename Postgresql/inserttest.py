import psycopg2

try:
   connection = psycopg2.connect(user="postgres",
                                  password="post123",
                                  host="157.230.105.22",
                                  port="5432",
                                  database="SehirRehberi")
   cursor = connection.cursor()

   postgres_insert_query = """ INSERT INTO Users (PasswordHash, PasswordSalt, UserName) VALUES (%s,%s,%s) """
   record_to_insert = ('0xAEFBBEB75376340394AC18177DF775549CB2CD74D5A26FEAF2C910772AF675617D1A1D5CD50DE914AEAAA7AE07033CEEC30F6AE7BF1E9191207AE475A91706BA',
   '0x1CCBEA721E21B0A5C35999FAB68447FEA14EDA5728104AA5968661A2348D8CCFFA49853DB1DDD5A463F702505220A643F8C3FAA53AB798ABDE3C024B818AFEEBD1A6189DF70611A3C3CA0A9C186C4B395F10A9101EB95F52204645BD87EFF0752A688956409D305460A4C5B4AEF52BBEA89EB918CD06DC58136C4658D2BC64F2',
   'yagmur')
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")