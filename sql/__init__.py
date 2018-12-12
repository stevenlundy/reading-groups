import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="48hr-W2018-mysql.dezydev.com",
        user="abelincoln",
        passwd="cherrytree",
        database="reading_groups"
    )