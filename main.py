import bs4
import re
import sqlite3
import urllib.request
import urllib.error
import time
import json


def main():
    dbpath = "广东.db"
    try:
        init_db(dbpath)
    except sqlite3.OperationalError:
        print('数据库已存在')
    getDate(dbpath)


findFuJian = re.compile(r'href="(.*?)"')


def getDate(dbpath):
    for id in range(42, 50):
        datalist = []
        url = "https://www.gd.gov.cn/gkmlpt/api/all/5?page=" + str(id) + "&sid=2"
        print(url)
        html = askurl(url)
        # print(html)
        # soup = bs4.BeautifulSoup(url, "html.parser")
        # 请求数据
        data1 = json.loads(html)

        # 提取文章信息
        articles = data1.get('articles', [])
        # print(articles)
        for a in range(len(articles)):
            data = []
            identifier = articles[a]['identifier']
            publisher = articles[a]['publisher']
            created_at = articles[a]['created_at']
            title = articles[a]['title']
            post_url = articles[a]['post_url']
            htmlC = askurl(post_url)
            # print(htmlC)
            # print("+" * 20)
            soup = bs4.BeautifulSoup(htmlC, "html.parser")  # 解析器，在内存形成树形结构的对象
            # print(soup)
            # print("_"*20)

            zhengwen = soup.find_all("div", class_="content")  # 查找符合要求的字符串，形成列表
            if not zhengwen:                          # 个别post_url无法获取到数据，转为使用url
                htmlC = askurl(articles[a]['url'])
                soup = bs4.BeautifulSoup(htmlC, "html.parser")
                zhengwen = soup.find_all("div", class_="content")     # content conten
            # print(zhengwen)
            # print("+" * 50)

            item2 = soup.find_all("img", class_="nfw-cms-img")
            if len(item2) == 0:
                item2 = soup.find_all('a', class_="nfw-cms-attachment")
            item2 = str(item2)
            fujian = re.findall(findFuJian, item2)

            # print(identifier, publisher, created_at, title, zhengwen, fujian)
            print(identifier, publisher, created_at, title, fujian)
            # print(type(identifier), type(publisher), type(created_at), type(title), type(zhengwen[0]), type(fujian))

            data.append(identifier)
            data.append(publisher)
            data.append(created_at)
            data.append(title)
            data.append(str(zhengwen[0]).replace("'", ""))
            if len(fujian) != 0:
                datafujian = ",".join(fujian)

                data.append(datafujian)

            print(str(id) + '共' + str(len(articles)) + '条,已爬' + str(a + 1) + '条。')
            # print(data)
            # for c in range(len(data)):
            #     print(data[c])
            datalist.append(data)

            savedatadb(datalist, dbpath)
            datalist = []
            time.sleep(3)

        # savedatadb(datalist, dbpath)

        time.sleep(5)


# 保存数据到数据库
def savedatadb(datalist, dbpath):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):  # 非数字插入数据库时需要有双引号或单引号
            data[index] = "'" + data[index] + "'"  # 格式化字符串 f'"{item}"' 在 item 两侧添加双引号。
        if len(data) == 5:
            sql = '''
                    insert into guangdong(
                    identifier,publisher,created_at,title,zhengwen)
                    values(%s)
                ''' % ",".join(data)
        else:
            sql = '''
                    insert into guangdong(
                    identifier,publisher,created_at,title,zhengwen,fujian)
                    values(%s)
                ''' % ",".join(data)
        # print(sql)
        cur.execute(sql)  # 执行
        conn.commit()  # 提交
    cur.close()
    conn.close()


# 初始化数据库
def init_db(dbpath):
    sql = '''
        create table guangdong 
        (
        id integer primary key autoincrement,
        identifier varchar,
        publisher varchar,
        created_at text,
        title varchar,
        zhengwen text,
        fujian text
        )

    '''  # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()  # 游标
    cursor.execute(sql)
    conn.commit()  # 提交
    conn.close()


# 得到指定一个URL的网页内容
def askurl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")          # unicode_escape
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)  # 把e中的错误类型打印
        if hasattr(e, "reason"):
            print(e.reason)  # e.code是错权误代码，e.reason获取的是错误的原因

    return html


if __name__ == "__main__":
    main()
    print("爬取完毕")
