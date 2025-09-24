// sampel python code.

from fastapi import APIRouter, HTTPException, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
import requests
import time
import pytz
import logging
from datetime import datetime, timedelta
from models.access_token_response import AccessTokenResponse
from app.database import db, tokens_collection
from app.crypto import encrypt_text

# Set up logging
logger = logging.getLogger(__name__)

router = APIRouter()


security = HTTPBearer()

def verify_jwt(credentials: HTTPAuthorizationCredentials = Security(security)):
  """
  Verify the JWT token in the request.

  Args:
    credentials (HTTPAuthorizationCredentials): The credentials containing the JWT token.

  Returns:
    dict: The decoded payload of the JWT token.

  Raises:
    HTTPException: If the token is invalid, expired, or has an invalid payload.
  """
  try:
    token = credentials.credentials
    payload = jwt.decode(token, GITHUB_JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
    if "sub" not in payload:
      raise HTTPException(status_code=400, detail="Invalid token payload")
    return payload
  except jwt.ExpiredSignatureError:
    raise HTTPException(status_code=401, detail="Token has expired")
  except jwt.InvalidTokenError:
    raise HTTPException(status_code=401, detail="Invalid token")


