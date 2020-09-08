from flask_restful import Resource
from flask import request, jsonify
import re_engine

class Regex(Resource):
    def get(self, re_type):
        '''
        Function to process the get request.
        parameter : re_type
        description : re_type value can be find or replace as per requirement of user.
        '''
        req_data = request.get_json() 
        try:
            pattern = req_data['pattern']
            sequence = req_data['sequence']
        except:
            message="Required index pattern or sequence not found"
            return {"message":message},422

        result = re_engine.find(pattern=pattern, sequence=sequence)
        if result == []:
            message = "No match found"
            return {"message":message},404
        else:
            if(re_type=='find'):
                return {"message":"success","data":result}
            elif(re_type=='replace'):
                try:
                    replace = req_data['replace']
                except:
                    message="Required index replace not found"
                    return {"message":message},422
                result = re_engine.replace(pattern=pattern, repl=replace, sequence=sequence)
                return {"message":"success","data":result}