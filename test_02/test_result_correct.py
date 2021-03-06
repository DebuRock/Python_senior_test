import os
from bson import ObjectId
test_db_name = "test_%s" % ObjectId()
os.environ['DB_NAME'] = test_db_name
from app import api
from pymongo import MongoClient
import pytest
from bson.json_util import loads
import hashlib


def make_test_mongo():
    client = MongoClient(port=27017)
    return client[test_db_name]


@pytest.fixture(scope="session", autouse=True)
def set_up_test_mongo_and_tear_down(request):
    mongo = make_test_mongo()
    fixture_dir = os.path.join(os.path.dirname(__file__), 'fixture_data')
    fnames = os.listdir(os.path.join(os.path.dirname(__file__), 'fixture_data'))
    for fname in fnames:
        fpath = os.path.join(fixture_dir, fname)
        with open(fpath, 'r') as f:
            entries = loads(f.read())
            coll = fname.split(".")[0]
            mongo[coll].insert_many(entries)

    def tear_down():
        mongo.client.drop_database(test_db_name)

    request.addfinalizer(tear_down)


@pytest.fixture
def client():
    with api.test_client() as client:
        yield client


def test_call_view_function(client):
    result = client.get('list_client_user/58884ff19c5d396319ef9c09')
    assert hashlib.sha224(result.data).hexdigest() == "7203ebd74df5402adf4a28cdb59410e25f5754c5864217b995ede1e7"
