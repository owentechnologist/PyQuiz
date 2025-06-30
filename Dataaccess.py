import psycopg 
# ^ the database driver for postgres(and cockroach)

# the program is called with the name of a file containing the interesting questions to be used
# Presumably: if usefile is False then the filename is used as a filter when querying a table in a DB
def getlines(usefile, questionTopic):
    if usefile: 
        # Open the file safely using 'with' so it's closed properly, even if there's an error
        questionFilename = questionTopic + '.tsv'
        with open(questionFilename) as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines if line.strip()]
    else: 
        connection = connect_to_db()
        cursor = connection.cursor()
        
        # Query to fetch questions and answers from the Q_and_A table

        # an even more sophisticated impl allow for vector similarity lookup when appropriate
        # so that some answers would not have to be exact token/string matches, but rather semantically equivalant
        cursor.execute("SELECT question, answer FROM Q_and_A join ")
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

'''
DDL and sample queries for a simple DB schema:

create table topic (id UUID PRIMARY KEY DEFAULT gen_random_uuid(), topic string UNIQUE not null);
insert into topic(topic) values('mytest');
create table question_answer (id UUID PRIMARY KEY DEFAULT gen_random_uuid(),topic_id UUID NOT NULL REFERENCES topic (id), question string not null, answer string not null);

with tq AS (select id from topic t where t.topic = 'mytest') insert into question_answer(topic_id,question,answer) SELECT id, 'my testq', 'answer' FROM tq
select question, answer, topic from question_answer qa JOIN topic t ON t.id = qa.topic_id;
 
'''
