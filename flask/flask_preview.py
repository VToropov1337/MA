import psycopg2
from flask import Flask, request



try:
    connect = psycopg2.connect(database='postgres', user='master', host='localhost', password='master')

except Exception as ex:
    print('I am unable to connect to the database', ex)
    raise ex



cursor = connect.cursor()

cursor.execute("SELECT articles.id, articles.article_title, articles.price, geo_objects.title \
    FROM articles \
    JOIN geo_objects \
    ON articles.geo_object_id = geo_objects.id \
    GROUP BY articles.id,geo_objects.title,article_title,articles.price \
    ORDER BY articles.id DESC;")

cursor.execute("SELECT * FROM public.product")

data = cursor.fetchall()


app = Flask(__name__)
app.config.update(
    DEBUG = True
)



@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        try:
            cursor.execute("SELECT articles.id, articles.article_title, articles.price, geo_objects.title \
                FROM articles \
                JOIN geo_objects \
                ON articles.geo_object_id = geo_objects.id \
                GROUP BY articles.id,geo_objects.title,article_title,articles.price \
                ORDER BY articles.id DESC;")


            data = cursor.fetchall()
            return str(data)
        except Exception as x:
            print('++++++++')
            print(x)
            cursor.execute("rollback")
            cursor.execute("SELECT articles.id, articles.article_title, articles.price, geo_objects.title \
                FROM articles \
                JOIN geo_objects \
                ON articles.geo_object_id = geo_objects.id \
                GROUP BY articles.id,geo_objects.title,article_title,articles.price \
                ORDER BY articles.id DESC;")

            data = cursor.fetchall()
            return str(data)


    else:
        try:
            val = connect.cursor()
            t = request.form['title']
            p = request.form['price']
            g = request.form['geo_object']
            print('--------')
            print(request.form['title'],request.form['price'],request.form['geo_object'], sep='\n')
            val.execute(
                """INSERT INTO public.articles(
                    article_title, price, geo_object_id) VALUES (
                    %(title)s,%(price)s,%(geo_object)s)""",

                {'title': t, 'price': p, 'geo_object': g}
            )
            connect.commit()
            print('--------------')
            return "Record was added"
        except Exception as ex:
            print(ex)
            return 'Something wrong', 404



if __name__ == "__main__":
    app.run()