from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    f=open("util/trendopinions.txt","r")
    data=f.read().split()
    topics={}
    for i in range(0,len(data),2):
        print(i)
        topics[data[i]]=((1-abs(float(data[i+1])))*255)*(float(data[i+1])/float(data[i+1]))
    return render_template("home.html",topics=topics)

if __name__ == "__main__":
    app.debug = True
    app.run()