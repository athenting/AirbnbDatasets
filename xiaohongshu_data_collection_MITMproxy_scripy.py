import sys
sys.path.append('C:/Users/athen/anaconda3/Lib/site-packages')
from mitmproxy import ctx
from jsonpath import jsonpath
import json
import pymysql
import settings

def response(flow):
    global type
    connect = pymysql.connect(
        host=settings.MYSQL_HOST,
        db=settings.MYSQL_DBNAME,
        user=settings.MYSQL_USER,
        passwd=settings.MYSQL_PASSWD,
        use_unicode=True)
    cursor = connect.cursor()

    response = flow.response
    response.encoding = 'utf-8'
    info = ctx.log.info
    info(str(response.status_code))
    info(str(response.headers))

    data = response.text
    jsondata=json.loads(data)
    print(jsondata)
    notes = jsonpath(jsondata, '$..items[*]')
    for note in notes:
        description = jsonpath(note, '$.note.desc')
        id = jsonpath(note, '$.note.id')
        #liked = jsonpath(note, '$.note.liked')[0]
        liked_count = jsonpath(note, '$.note.liked_count')
        title = jsonpath(note, '$.note.title')
        type = jsonpath(note, '$.note.type')
        post_url = 'https://www.xiaohongshu.com/discovery/item/{}'.format(id)
        cursor.execute(
            'insert ignore into test.mgs(id,title,type,liked_count,description,post_url) values (%s,%s,%s,%s,%s,%s)',
            (id,title,type,liked_count,description,post_url))
        connect.commit()




