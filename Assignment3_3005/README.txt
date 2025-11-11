Name: Rayan Hassan Student_ID: 101310730
#COMP 3005 Assignment 3

##Prerequisites
- Python3
- PostgreSQL
- Git 

STEP 1: Clone the repo
    GitHub Repository:
        run: git clone https://github.com/CynicalD/Comp3005
    then cd into assignment3_3005

STEP 2: Create and populate db
    Create the databse callign it assignment3 and table called student and populate it with data from spec

STEP 3: Create & activate VENV and install requirements
    run: 
    MAC OS : python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
    WINDOWS: python -m venv .venv; .\.venv\Scripts\activate; pip install -r requirements.txt
    Note: this will also install dependency pyscopg2 used to talk to db

STEP 4: Run app.py 
    Make sure PostgreSQL is running.
    Now run: python3 app.py and it should perform CRUD opeartions as shown in video.


Youtube link video: https://youtu.be/EtIMZ0PSduE
    