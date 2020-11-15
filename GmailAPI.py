from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time

class GmailAPI:

    def __init__(self):
        # If modifying these scopes, delete the file token.json.
        self._SCOPES = 'https://mail.google.com/'
        self.MessageIDList = []

    def ConnectGmail(self):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', self._SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('gmail', 'v1', http=creds.authorize(Http()))
        
        return service

    def DeleteMessageList(self,DateFrom,DateTo,MessageFrom):
        try:

            #Connect to Gmail API
            service = self.ConnectGmail()
            self.MessageIDList = []
            
            query = ''
            # Set query parameter
            if DateFrom != None and DateFrom !="":
                query += 'after:' + DateFrom + ' '
            if DateTo != None  and DateTo !="":
                query += 'before:' + DateTo + ' '
            if MessageFrom != None and MessageFrom !="":
                query += 'From:' + MessageFrom + ' '

            # Get MessageIDList from API
            self.MessageIDList = service.users().messages().list(userId='me',maxResults=500,q=query).execute()
            if self.MessageIDList['resultSizeEstimate'] == 0: 
                print("Message is not found")
                return False

            # Set reqponsebody for batch delete
            ids = {
                'ids': []
            }
            ids['ids'].extend([str(d['id']) for d in self.MessageIDList['messages']])
            
            #Run batchDelete
            service.users().messages().batchDelete(userId='me',body=ids).execute()

            return True
    
        except Exception as e:
            return False

    def ModifyUnreadMessageList(self,DateFrom,DateTo,MessageFrom):
        try:

            #Connect to Gmail API
            service = self.ConnectGmail()
            self.MessageIDList = []
            
            query = ''
            # Set query parameter
            query += 'is:unread ' #未読のみ
            if DateFrom != None and DateFrom !="":
                query += 'after:' + DateFrom + ' '
            if DateTo != None  and DateTo !="":
                query += 'before:' + DateTo + ' '
            if MessageFrom != None and MessageFrom !="":
                query += 'From:' + MessageFrom + ' '

            # Get MessageIDList from API
            self.MessageIDList = service.users().messages().list(userId='me',maxResults=500,q=query).execute()
            if self.MessageIDList['resultSizeEstimate'] == 0: 
                print("Message is not found")
                return False

            # Set reqponsebody for batch delete
            ids = {
                'ids': [],
                "removeLabelIds": [
                "UNREAD"
                ]
            }
            ids['ids'].extend([str(d['id']) for d in self.MessageIDList['messages']])
            
            # Run batchModify
            service.users().messages().batchModify(userId='me',body=ids).execute()

            return True
    
        except Exception as e:
            return False
