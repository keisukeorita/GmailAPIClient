from bottle import route, run, template, redirect, request,get, static_file
from GmailAPI import GmailAPI


# Static file
@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@route('/main')
def main():
    return template("main")

@route('/run', method=['GET','POST'])
def get_massage(): 
    Gmail = GmailAPI()
    mode= request.forms.get("mode")
    DateFrom= request.forms.get("DateFrom")
    DateTo= request.forms.get("DateTo")
    MessageFrom= request.forms.get("MessageFrom")
    if mode == "modify":
        if Gmail.ModifyUnreadMessageList(DateFrom=DateFrom,DateTo=DateTo,MessageFrom=MessageFrom) == True:
            message = "{} email is modified to read".format(Gmail.MessageIDList['resultSizeEstimate'])
        else:
            return 'error'
    elif mode=="delete":
        if Gmail.DeleteMessageList(DateFrom=DateFrom,DateTo=DateTo,MessageFrom=MessageFrom) == True:
            message = "{} email is deleted".format(Gmail.MessageIDList['resultSizeEstimate'])
        else:
            return 'error'
    else:
        return 'error'

    return message

run(host='localhost', port=8080)