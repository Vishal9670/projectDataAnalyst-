import pyodbc

def get_db_connnection():
    connection_string = (
        'DRIVER = {SQL Server};'
        'SERVER = DESKTOP-MVGO5U1\\SQLEXPRESS;'
        'DATABASE=vishaldb;'
        'UID= vishal;'
        'PWD=Vishal;'
        "Trusted_connection=yes"
    )
    try:
      conx=pyodbc.connect(connection_string)
      print("connection successfull")
      return conx
    except pyodbc.Error as e:
        print("Error: ", e)
        return None


