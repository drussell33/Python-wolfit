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

def test_10_seconds_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=10))) == "10 seconds ago"

def test_a_minute_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=60))) == "a minute ago"

def test_5_minutes_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=301))) == "5 minutes ago"

def test_an_hour_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=3600))) == "an hour ago"

def test_3_hours_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=10800))) == "3 hours ago"

# def test_epoch_int_input_for_jan15():
#     assert (pretty_date(1610712001) == "Yesterday")

def test_epoch_int_input_for_jan152020():
    assert (pretty_date(1579089601) == "1 years ago")

def test_bad_input():
    assert (pretty_date(datetime.utcnow() - timedelta(days=-1))) == "just about now"