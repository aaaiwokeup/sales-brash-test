import pytest

from datetime import datetime

from run import aggregate_data

def test_aggregate_data():
    fb_spend = [
        {
            "date": "2025-06-04",
            "campaign_id": "CAMP-123",
            "spend": 37.5
            },
        {
            "date": "2025-06-04",
            "campaign_id": "CAMP-456",
            "spend": 19.9
            },
        {
            "date": "2025-06-05",
            "campaign_id": "CAMP-123",
            "spend": 42.1
            },
        {
            "date": "2025-06-05",
            "campaign_id": "CAMP-789",
            "spend": 11
            }
    ]

    network_conv = [
        {
            "date": "2025-06-04",
            "campaign_id": "CAMP-123",
            "conversions": 14
            },
        {
            "date": "2025-06-04",
            "campaign_id": "CAMP-456",
            "conversions": 3
            },
        {
            "date": "2025-06-05",
            "campaign_id": "CAMP-123",
            "conversions": 10
            },
        {
            "date": "2025-06-05",
            "campaign_id": "CAMP-456",
            "conversions": 5
            }
    ]

    start_date = datetime.strptime('2025-06-04', '%Y-%m-%d').date().isoformat()
    end_date = datetime.strptime('2025-06-04', '%Y-%m-%d').date().isoformat()

    result = [('2025-06-04', 'CAMP-123', 37.5, 14, 2.68), ('2025-06-04', 'CAMP-456', 19.9, 3, 6.63)]

    assert aggregate_data(fb_spend, network_conv, start_date, end_date) == result


def test_zero_division():
    fb_spend = [
        {
            "date": "2025-06-04",
            "campaign_id": "CAMP-123",
            "spend": 37.5
            }
    ]

    network_conv = [
        {
            "date": "2025-06-04",
            "campaign_id": "CAMP-123",
            "conversions": 0
            }
    ]

    start_date = datetime.strptime('2025-06-04', '%Y-%m-%d').date().isoformat()
    end_date = datetime.strptime('2025-06-04', '%Y-%m-%d').date().isoformat()

    result = [('2025-06-04', 'CAMP-123', 37.5, 0, None)]

    assert aggregate_data(fb_spend, network_conv, start_date, end_date) == result
