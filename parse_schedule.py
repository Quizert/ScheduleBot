import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Parser:
  def __init__(self) -> None:
    self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    self.SAMPLE_SPREADSHEET_ID = "1vNbxjZmw1ikzqr6Q79yd6FuGN8ha1Qlh5GcDVs-0TiE"
    self.SAMPLE_RANGE_NAME = "1 курс!L:L"
    #SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

    #SAMPLE_SPREADSHEET_ID = "1vNbxjZmw1ikzqr6Q79yd6FuGN8ha1Qlh5GcDVs-0TiE"
    #SAMPLE_RANGE_NAME = "1 курс!L:L"


  def start(self):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    if os.path.exists("token.json"):
      creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", self.SCOPES
        )
        creds = flow.run_local_server(port=0)
      with open("token.json", "w") as token:
        token.write(creds.to_json())

    try:
      service = build("sheets", "v4", credentials=creds)

      sheet = service.spreadsheets()
      result = (
          sheet.values()
          .get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID, range=self.SAMPLE_RANGE_NAME)
          .execute()
      )
      values = result.get("values", [])
      return values
    
      #TODO
    
      if not values:
        print("No data found.")
        return
    except HttpError as err:
      print(err)

