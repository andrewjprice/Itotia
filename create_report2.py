#!/usr/bin/env python3
import sys
from datetime import datetime
from dbconfig import read_db_config
from mysql.connector import Error, MySQLConnection


def connect():
    """
    Connect to SQL DB with connect file.
    """
    db_config = read_db_config()
    try:
        print("Connecting to MySQL Database...")
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            print("Connection Successful.")
        else:
            print("Connection Failed.")
    except Error as error:
        print(error)


def getInput(begTest, endTest):
    while True:
        try:
            #begTest = sys.argv[1]
            #endTest = sys.argv[2]
            #begTest = datetime.strptime(begTest, '%Y%m%d')
            #endTest = datetime.strptime(endTest,'%Y%m%d')
            dateFormat(begTest,endTest)
            return False
        except ValueError:
            print('Invalid date!')
            exit(-1)
            break

def dateFormat(begDate,endDate):
    beg_date = datetime.strptime(begDate,'%Y%m%d').strftime('%Y-%m-%d 00:00')
    end_date = datetime.strptime(endDate,'%Y%m%d').strftime('%Y-%m-%d 23:59')
    print("Beginning date: {}".format(beg_date))
    print("Ending date: {}".format(end_date))
       
def main():
    connect()
    begTest = "20150816"
    endTest = "20150916"
    getInput(begTest, endTest)

if __name__ == '__main__':
    #call main
    main() 

    exit(0)
