import textwrap
from datetime import timedelta, datetime

import pytest

from sqlalchemy import exc

from app import db
from app.helpers import pretty_date, less_than_day


def test_now():
    assert pretty_date(datetime.utcnow()) == "just now"

def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days=1))) == "Yesterday"

def test_2_days_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=2))) == "2 days ago"