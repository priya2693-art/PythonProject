import pytest
from myproject.lead import Lead, fetch_lead_from_zoho,validate_lead_data


@pytest.fixture()
def lead_data():
    return {
        'crm_id': '12345',
        'name': 'test',
        'phone':'7585748510',
        'email': 'test@gmail.com',
        'from_date':'2025-09-20',
        'nights': 3,
        'from_city': 'delhi',
        'departure_city':'DEL',
        'destination_city':'dubai',
        'assigned_seller':'priya',
        'budget': 5000,
        'travelling_cities':['dubai']
    }
@pytest.fixture
def lead(lead_data):
    return Lead(**lead_data)

def test_create_lead(lead):
    assert lead.crm_id =='12345'
    assert lead.name =='test'
    assert lead.phone == '7585748510'
    assert lead.email == 'test@gmail.com'
    assert lead.from_city =='delhi'
    assert lead.departure_city=='DEL'
    assert lead.destination_city == 'dubai'
    assert lead.budget== 5000
    assert lead.from_date == '2025-09-20'
    assert lead.assigned_seller== 'priya'
    assert lead.travelling_cities== ['dubai']

def test_invalid_lead():
    with pytest.raises(ValueError):
        Lead(crm_id=None, name=None,phone=None,email=None,from_city=None,nights= -1,departure_city=None,destination_city=None,budget=None,assigned_seller=None,travelling_cities=None,from_date=None)



def test_add_city(lead):
    lead.add_city('Paris')
    assert 'Dubai' not in lead.travelling_cities

def test_remove_city(lead):
    lead.remove_city('dubai')
    assert 'dubai' not in lead.travelling_cities

def test_get_lead_summary(lead):
    summary = lead.get_lead_summary()
    assert summary['crm_id'] == '12345'
    assert summary['name'] == 'test'
    assert summary['travelling_cities'] ==['dubai']


def test_fetch_lead_from_zoho():
    crm_id = '12345'
    lead = fetch_lead_from_zoho(crm_id)

    assert lead['crm_id'] == crm_id
    assert lead['name'] == 'Default Name'
    assert lead['phone'] == '0000000000'
    assert lead['email'] == 'default@example.com'
    assert lead['assigned_seller'] == 'priya'
    assert lead['budget'] == 50000
    assert lead['travelling_cities'] == ['Dubai']


def test_validate_lead_data_valid():
    valid_data = {
        'crm_id': '12345',
        'nights': 3
    }
    try:
        validate_lead_data(valid_data)
    except ValueError:
        pytest.fail("validate_lead_data raised ValueError unexpectedly!")


def test_validate_lead_data_invalid():
    invalid_data = {
        'nights': 3
    }
    with pytest.raises(ValueError):
        validate_lead_data(invalid_data)