from bottle import route, run, template, redirect, request
from GmailAPI import GmailAPI

@route('/main')
def main():
    MessageList = []
    return template("search", MessageList=MessageList)

@route('/get', method=['GET','POST'])
def get_massage(): 
    Gmail = GmailAPI()
    DateFrom= request.forms.get("DateFrom")
    DateTo= request.forms.get("DateTo")
    MessageFrom= request.forms.get("From")
    if Gmail.GetMessageList(DateFrom=DateFrom,DateTo=DateTo,MessageFrom=None) == False:
        return 'error'
    return template("result", MessageList=Gmail.MessageList)

@route('/delete', method=['GET','POST'])
def delete():

    Gmail = GmailAPI()
    MessageList = request.body
    num = Gmail.DeleteMessageList(MessageList=MessageList)
    return template("delete", result=num)

run(host='localhost', port=8080)