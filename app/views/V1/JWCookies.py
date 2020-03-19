from flask_restful import fields
import json
#输出
class ONoDeal (fields.Raw):
    def format(self, value):
        return value

def INoDeal(value):
    # if value % 2 == 0:
    #     raise ValueError("The parameter '{}' is not odd. You gave us the value: {}".format(name, value))

    return json.loads(value)