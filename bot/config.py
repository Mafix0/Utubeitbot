import os


class Config:

    BOT_TOKEN = "6064905998:AAF3i5AxbRtPVV06cqwzgNYp0zIxrNLZnO8"

    SESSION_NAME = ":memory:"

    API_ID = int(os.environ.get("API_ID"))

    API_HASH = os.environ.get("API_HASH")

    CLIENT_ID = "850143556786-hqlu8c2v871sa0om3u22ritvlahn1o6p.apps.googleusercontent.com"

    CLIENT_SECRET = "4167d8b8779aab33b73810feb3c77021"

    BOT_OWNER = 947945328""

    AUTH_USERS_TEXT = "947945328 932420516"

    AUTH_USERS = [BOT_OWNER, 754495556, 932420516] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
