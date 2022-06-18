from flask import Flask
from markupsafe import escape
from Housing.exception import HousingException
from Housing.logger import logging
import sys

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception('We are not getting details')
    except Exception as e:
        housing = HousingException(e, sys)  
        errormsg = housing.get_detailed_error_message(e, sys)
        #print(housing)    
    return errormsg


if __name__=="__main__":
    app.run(debug=True)