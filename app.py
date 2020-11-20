from flask import Flask,render_template,request
import datetime
import sqlite3

app = Flask(__name__)


@app.route('/')
def result():
    return render_template("mo.html")



@app.route('/mo')
def result1():
    return render_template("mo.html")



@app.route('/movies')
def result2():

    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()


    return render_template("movies.html",movies = datalist)



@app.route('/grand')
def result3():
    score = []  #评分
    num = []   #每个评分所统计出的电影数据
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0]))
        num.append(item[1])

    cur.close()
    con.close()
    return render_template("grand.html",score = score,num = num)



@app.route('/world')
def result4():
    return render_template("world.html")



@app.route('/team')
def result5():
    return render_template("team.html")

if __name__ == '__main__':
    app.run(debug=True)

    