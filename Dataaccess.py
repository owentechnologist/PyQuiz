import psycopg 
#the database driver for postgres(and cockroach)
'''else: 
        connection=connect_to_db()
        # Use a hardcoded fallback list of questions
        lines = [
            'Who invented the backwards worm?~Owen',
            'Who was a powerful landscaper?~Drew'
        ]
    return lines'''

def getlines(usefile, questionFilename):
    if usefile: 
        # Open the file safely using 'with' so it's closed properly, even if there's an error
        with open(questionFilename) as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines if line.strip()]


    else: 
        connection = connect_to_db()
        cursor = connection.cursor()
        
        # Query to fetch questions and answers from the Q_and_A table
        cursor.execute("SELECT question, answer FROM Q_and_A")
        rows = cursor.fetchall()
        
        # Create a list of strings in the format "question~answer"
        lines = [f"{row[0]}~{row[1]}" for row in rows]
        
        # Close the connection
        cursor.close()
        connection.close()
    
    return lines


def connect_to_db():
    try:
        '''Adjust these parameters for your setup
        "host=localhost port=5432 dbname=postgres user=postgres sslmode=prefer connect_timeout=10'''
        conn = psycopg.connect(
            dbname="postgres",
            user="postgres",
            password="admin123",
            host="localhost",
            port=5432
        )
        print("✅ Connection successful")
        return conn
    except Exception as e:
        print("❌ Connection failed:", e)
        return None
