from typing import Optional
from beacon.request.model import  RequestParams
import json
from beacon.db import BeaconRpcClient
from beacon.db.utils import createPOST


def get_runs(entry_id: Optional[str], qparams: RequestParams):
    collection = 'runs'
    templatePost = createPOST(qparams)
    messageRabbit = {
        "url":collection,
        "queryPost": templatePost
    }
    
    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)

    return jsonFile

def get_run_with_id(entry_id: Optional[str], qparams: RequestParams):
    collection = 'runs'
    messageRabbit = {
        "url":f'{collection}/{entry_id}',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile


def get_variants_of_run(entry_id: Optional[str], qparams: RequestParams):
    collection = 'runs'
    messageRabbit = {
        "url":f'{collection}/{entry_id}/variants',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile

def get_analyses_of_run(entry_id: Optional[str], qparams: RequestParams):
    collection = 'runs'
    messageRabbit = {
        "url":f'{collection}/{entry_id}/analyses',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile


def get_filtering_terms_of_run(entry_id: Optional[str], qparams: RequestParams):
    collection = 'runs'
    messageRabbit = {
        "url":f'{collection}/filtering_terms',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile