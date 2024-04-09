from typing import Optional
from beacon.request.model import  RequestParams
import json
from beacon.db import BeaconRpcClient
from beacon.db.utils import createPOST

def get_analyses(entry_id: Optional[str], qparams: RequestParams):
    collection = 'analyses'
    templatePost = createPOST(qparams)
    messageRabbit = {
        "url":collection,
        "queryPost": templatePost
    }
    
    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)

    return jsonFile


def get_analyses_with_id(entry_id: Optional[str], qparams: RequestParams):
    collection = 'analyses'
    messageRabbit = {
        "url":f'{collection}/{entry_id}',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile

def get_variants_of_analyses(entry_id: Optional[str], qparams: RequestParams):
    collection = 'analysis'
    messageRabbit = {
        "url":f'{collection}/{entry_id}/variants',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile

def get_filtering_terms_of_analyses(entry_id: Optional[str], qparams: RequestParams):
    collection = 'analyses'
    messageRabbit = {
        "url":f'{collection}/filtering_terms',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile