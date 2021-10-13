# -*- coding: utf-8 -*-
import json
import pymysql

db_settings = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '********',
    'db': 'stock',
    'charset': 'utf8'
}

# 連線
conn = pymysql.connect(**db_settings)
db = conn.cursor()

'''
# 刪除表
sql0 = 'DROP TABLE test;'
db.execute(sql0)
conn.commit()
'''
# 新增表
sql = 'CREATE TABLE test(ID  CHAR(20), price  CHAR(20), EPS CHAR(20));'
db.execute(sql)
conn.commit()

# 表內新增column
sql2 = 'ALTER TABLE test ADD COLUMN name CHAR(20);'
db.execute(sql2)
conn.commit()

# 表內刪除column
sql3 = 'ALTER TABLE test DROP COLUMN EPS;'
db.execute(sql3)
conn.commit()

# 表內新增單一資料
sql4 = 'INSERT INTO test(ID, price, name)VALUES(%s, %s, %s)'
db.execute(sql4, ('0050', '105.70', 'N'))
conn.commit()

db.execute(sql4, ('0051', '39.41', 'N'))
conn.commit()

# 表內刪除單一資料
sql5 = 'DELETE FROM test WHERE ID = %s'
db.execute(sql5, ('0051'))
conn.commit()

# 灌入多筆資料
with open('.\demo13\stock_test2.json', 'r', encoding='utf-8') as f: #讀取json檔案
    log = json.load(f)
    
col = tuple(log[0].keys())
data = tuple(log[0].values())
# 新增表
sql = 'CREATE TABLE import_json('
for c in col:
    sql = sql + c +' CHAR(20),'    
sql = sql[:-1] + ');'
db.execute(sql)
conn.commit()
# 灌入資料庫
sql2 = 'INSERT INTO import_json('
for c in col:
    sql2 = sql2 + c + ','
sql2 = sql2[:-1] + ') VALUES ('
for i in range(len(col)):
    sql2 = sql2 + '%s,'
sql2 = sql2[:-1] + ');'
for i in range(len(log)):
    db.execute(sql2, tuple(log[i].values()))
conn.commit()

# 擷取表內資料
command = 'SELECT * FROM test;'
db.execute(command)
result = db.fetchall()

command2 = 'SELECT * FROM stock.import_json;'
db.execute(command2)
result2 = db.fetchall()

#斷線
db.close()
conn.close()
