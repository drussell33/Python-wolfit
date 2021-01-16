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

def test_1_week_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=7))) == "1 weeks ago"

def test_1_months_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=31))) == "1 months ago"

def test_1_years_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=365))) == "1 years ago"