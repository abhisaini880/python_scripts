from regex.regex import Regex

def initialize_routes(api):
    api.add_resource(Regex, '/query/<re_type>', methods=['GET'])