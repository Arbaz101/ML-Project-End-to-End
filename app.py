from flask import Flask
from markupsafe import escape
#print(__name__)
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "Starting Machine Learning Project"


if __name__=="__main__":
    app.run(debug=True)