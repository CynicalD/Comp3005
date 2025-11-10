import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="assignment3",
        user="rayanhassan",
        password="",
    )
    return conn

def getAllStudents():
    # 1. connect
    conn = connect_to_db()
    # 2. makes a cursor
    cur = conn.cursor()
    # 3. run the query
    cur.execute("SELECT student_id, first_name, last_name, email, enrollment_date FROM students;")
    # 4. get all rows
    rows = cur.fetchall()
    # 5. prnit them
    for row in rows:
        print(row)
    # 6. clean up
    cur.close()
    conn.close()

def addStudents(first_name, last_name, email, enrollment_date):
    try:
        with connect_to_db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO students (first_name, last_name, email, enrollment_date)
                    VALUES (%s, %s, %s, %s);
                    """,
                    (first_name, last_name, email, enrollment_date)
                )
                conn.commit()
                print(f"Added student: {first_name}, {last_name}")
    except Exception as e:
        print("Error happened while adding student")
        print(e)
    
def updateStudentEmail(student_id, new_email):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute(
        "UPDATE students SET email = %s WHERE student_id = %s;",
        (new_email, student_id)
    )
    conn.commit()
    print(f"Updated student {student_id}'s email to {new_email}")

    cur.close()
    conn.close()

def deleteStudent(student_id):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM students WHERE student_id = %s;",
        (student_id,)
    )
    conn.commit()
    print(f"Sucessfully deleted student #{student_id}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    #addStudents("Rayan", "Hassan", "rayan.hassan@example.com", "2025-10-7")
    #updateStudentEmail(2, "new.email@example.com")
    deleteStudent(5)
    getAllStudents()