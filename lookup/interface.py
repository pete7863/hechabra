import sys
sys.path.insert(0, '/var/www/hechabra')

from database.mysql import client

parts_of_speech = ["adjective", "adverb", "noun", "verb"]

def get_definition_random():
    result = client.perform_read_query("SELECT * FROM definitions ORDER BY RAND() LIMIT 1")

    return def_result_to_dict(result)

def get_definition(def_id):
    result = client.perform_read_query("SELECT * FROM definitions WHERE def_id = " + str(def_id) + " LIMIT 1")

    return def_result_to_dict(result)

def def_result_to_dict(result):
    dict = {}
    dict["def_id"] = result[0][0]
    dict["definition"] = result[0][1]
    dict["part_of_speech"] = parts_of_speech[result[0][2]]
    dict["user_id"] = result[0][3]

    return dict

def add_definition(dataDict):
    user_id = dataDict["user_id"]

    query_str = 'INSERT INTO definitions (`definition`, `part_of_speech`, `user_id`) VALUES ("' + \
                dataDict["definition"] + '" , ' + str(dataDict["part_of_speech"]) + ', ' + str(user_id) + ')'

    client.perform_write_query(query_str)