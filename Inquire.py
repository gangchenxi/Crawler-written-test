import re
import sqlite3
import json


def main():
    dbpath = "广东.db"

    intime = input("请输入要查询的时间范围：例：(20220101-20230601)")
    time1 = intime[0:4] + "-" + intime[4:6] + "-" + intime[6:8] + " 00:00:00"
    time2 = intime[9:13] + "-" + intime[13:15] + "-" + intime[15:17] + " 00:00:00"
    print(time1, time2)
    data = inquiredb(time1, time2, dbpath)
    a = int(input("输入选择是否显示正文：1：不显示。2：显示"))
    if a == 1:
        for row in data:
            column1_value = row[1]  # 第一个列的值
            column2_value = row[2]  # 第二个列的值
            column3_value = row[3]
            column4_value = row[4]
            column6_value = row[6]
            print(column1_value, column2_value, column3_value, column4_value, column6_value)
    else:
        for row in data:
            column1_value = row[1]  # 第一个列的值
            column2_value = row[2]  # 第二个列的值
            column3_value = row[3]
            column4_value = row[4]
            column5_value = row[5]
            column6_value = row[6]
            print(column1_value, column2_value, column3_value, column4_value,column5_value, column6_value)



def inquiredb(time1, time2, dbpath):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    sql = '''
        SELECT *
        FROM guangdong
        WHERE created_at BETWEEN ? AND ?;
    '''
    cur.execute(sql, (time1, time2))  # 执行
    data = cur.fetchall()
    conn.close()
    return data


if __name__ == "__main__":
    main()
    print("查询完毕")
