# app.py
from flask import Flask
from flask_restful import Api, Resource, reqparse
import joblib
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re


APP = Flask(__name__)
API = Api(APP)


class Match_perc():    
    def cal_match_perc(str1, str2):
        str1 = str1.lower()
        str1 = str1.replace('mr', '')
        str1 = str1.replace('mrs', '')
        str1 = str1.strip()
        str1 = re.sub(r'[^\w\s]', '', str1)
    
        str2 = str2.lower()
        str2 = str2.replace('mr', '')
        str2 = str2.replace('mrs', '')
        str2 = str2.strip()
        str2 = re.sub(r'[^\w\s]', '', str2)
    
        results = fuzz.token_set_ratio(str1, str2)
    
        return(results)
        
        
class get_match_perc(Resource):

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('first_string')
        parser.add_argument('second_string')

        args = parser.parse_args()  # creates dict

        out = Match_perc.cal_match_perc(args['first_string'], args['second_string'])

        return out, 200


API.add_resource(get_match_perc, '/get_match_perc')

if __name__ == '__main__':
    APP.run(debug=True, port='1080')