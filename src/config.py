#   -   -   -   -   -   -   -   -   #
from os import getenv as env
from dotenv import load_dotenv
#   -   -   -   -   -   -   -   -   #
load_dotenv()
#   -   -   -   -   -   -   -   -   #
CONFIG = dict(
    host=env('HOST'),
    port=env('PORT'),
    debug=True,
)
TOKEN_NAME = 'tkn'
MASTER_PASSWORD = env('MASTER_PASSWORD')
#   -   -   -   -   -   -   -   -   #