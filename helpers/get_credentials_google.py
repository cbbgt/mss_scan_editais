import os
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials


def get_credentials_google():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'credentials.json', scope)
    # print(f"ENVIROMENT: {os.environ.get('ENVIROMENT')}")
    # if os.environ.get('ENVIROMENT') == 'DEV':
    #     scope = ['https://spreadsheets.google.com/feeds']
    #     credentials = ServiceAccountCredentials.from_json_keyfile_name(
    #         'credentials.json', scope)
    # else:
    #     scope = ['https://spreadsheets.google.com/feeds']
    #     credentials = Credentials.from_service_account_info(
    #         {
    #             'type': os.environ['GOOGLE_TYPE'],
    #             'project_id': os.environ['GOOGLE_PROJECT_ID'],
    #             'private_key_id': os.environ['GOOGLE_PRIVATE_KEY_ID'],
    #             'private_key': os.environ['GOOGLE_PRIVATE_KEY'].replace('\\n', '\n'),
    #             'client_email': os.environ['GOOGLE_CLIENT_EMAIL'],
    #             'client_id': os.environ['GOOGLE_CLIENT_ID'],
    #             'auth_uri': os.environ['GOOGLE_AUTH_URI'],
    #             'token_uri': os.environ['GOOGLE_TOKEN_URI'],
    #             'auth_provider_x509_cert_url': os.environ['GOOGLE_AUTH_PROVIDER_X509_CERT_URL'],
    #             'client_x509_cert_url': os.environ['GOOGLE_CLIENT_X509_CERT_URL'],
    #         },
    #         scopes=scope
    #     )
    return credentials
