import psycopg2

# Open conenction
conn = psycopg2.connect(database="prod_prelim", user = "prod_prelim", password = "Prod_Prelim", host = "10.29.70.40", port = "5432")
print("Opened database successfully")

# Create Cursor
cur = conn.cursor()

# Select Row
def select_operation():
    cur.execute("SELECT * from prod_prelim.r_eventdata")
    rows = cur.fetchall()
    print(rows)


#Insert Row
def insert_operation():
    insert_stmt = f"INSERT INTO prod_prelim.r_eventdata(\
                gt_createtime, c_piecename, c_msgtype, c_timestamp, gt_sampletime, i_linedir, i_passnum, i_loadonsignal, f_thrdlength, f_linespeed, f_maoffcenval) \
                VALUES(now(), 'TEst001', 'R2DW', 'asdf2345', 'now()', 0, 0, 0, 0, 0, 0)"

    cur.execute(insert_stmt)
    conn.commit()
    print("Records created successfully")

def close_operation():
    conn.close()

if __name__ == '__main__':
    select_operation()
    insert_operation()
    close_operation()