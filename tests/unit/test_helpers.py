import textwrap
from datetime import timedelta, datetime

import pytest

from sqlalchemy import exc

from app import db
from app.helpers import pretty_date, less_than_day


def test_now():
    assert pretty_date(datetime.utcnow()) == "just now"