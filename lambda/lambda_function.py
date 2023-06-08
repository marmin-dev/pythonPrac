import sys
import json
import pymysql

rds_host = "database-1.ceeq1u5dvhoi.ap-northeast-2.rds.amazonaws.com"
user_name = "lambda"
user_password = "password"
db_name = "sampledb"

try:
    conn = pymysql.connect(host=rds_host, port=3306, user=user_name, passwd=user_password, db=db_name)
except pymysql.MySQLError as e:
    print("ERROR: Could not connect to DB")
    print(e)
    sys.exit()

print("SUCCESS: Connect to DB")


def lambda_handler(event, context):
    title = event['title']
    contents = event['contents']

    query = f"insert into t_board ( title, contents, created_dt, created_id ) values ( '{title}', '{contents}', now(), 'user' )"

    with conn.cursor() as cur:
        cur.execute(query)
        conn.commit()

    return '%s is run successfully' % (query)