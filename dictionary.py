import mysql.connector
import itertools
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

word = input("Enter a word: ")

cursor = con.cursor()

cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()



if results:
    for result in results:
        print(result[1])
else:
    cursor.execute("SELECT Expression FROM Dictionary")
    results = [item[0] for item in cursor.fetchall()]
    if len(get_close_matches(word, results)) > 0:
        similar_word = get_close_matches(word, results)[0]
        cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % similar_word)
        results = cursor.fetchall()

        print("If you ment '%s', then here is the definiton." % similar_word)
        for result in results:
            print(result[1])
    else:
        print("Not found!")

