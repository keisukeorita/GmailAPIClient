from bottle import route, run, template, redirect, request
from GmailAPI import GmailAPI

@route('/main')
def main():
    return template("search")

@route('/run', method=['GET','POST'])
def get_massage(): 
    Gmail = GmailAPI()
    mode= request.forms.get("mode")
    DateFrom= request.forms.get("DateFrom")
    DateTo= request.forms.get("DateTo")
    MessageFrom= request.forms.get("From")
    if mode == "modify":
        print(mode)
        print(DateFrom)
        print(DateTo)
        print(MessageFrom)
        # if Gmail.ModifyUnreadMessageList(DateFrom=DateFrom,DateTo=DateTo,MessageFrom=MessageFrom) == False:
        #    return 'error'
    else:
        print(mode)
        print(DateFrom)
        print(DateTo)
        print(MessageFrom)
        # if Gmail.DeleteMessageList(DateFrom=DateFrom,DateTo=DateTo,MessageFrom=MessageFrom) == False:
        #    return 'error'
    return template("result")

run(host='localhost', port=8080)