from flask import Flask, jsonify, request
from pandas import read_excel
import requests
import config
app = Flask(__name__)


@app.route('/v1/process', methods=['POST','GET'])
def process():
    """this is a call bck from KaveNeger, will get sender and massage and
    will check if it is valid, then answers back
    """
    data = request.form
    import pdb; pdb.set_trace()
    sender = data['from']
    message = data['message']
    print(f'received {message} form {sender}')
    send_sms('Hi '+message, sender)
    ret = {"massage": "processed"}
    return jsonify(ret),200

def send_sms(message, receptor):
    """this function will get a MSISDN and message, then
    uses KEveNegar to send sms.
    """
    url = f'https://api.kavenegar.com/v1/{config.API_KEY}/sms/send.json'
    data = {
        "message": message,
        "receptor": receptor,
    }
    res = requests.post(url, data)


# def import_database_from_excel(filepath):
#     """gets and excel file name and imports lookup data (data and failures) from it"""
#     # df contains lookup data in the form of
#     # Row	Reference Number	Description	Start Serial	End Serial	Date
#     df = read_excel(filepath, 0)
#     for index, (line, ref, desc, start_serial, end_serial, date) in df.iterrows():
#         print(line, ref, desc, start_serial, end_serial, date)
#
#     df = read_excel(filepath, 1) # sheet one contains failed serial numbers. only a column
#     for index, failed_serial in df.iterrows():
#         print(failed_serial)



def check_serial():
    pass


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug = False)
    # import_database_from_excel('/data.xlsx')