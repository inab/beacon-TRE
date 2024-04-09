from typing import Optional
from beacon.request.model import  RequestParams
import json
from beacon.db import BeaconRpcClient

def get_filtering_terms(entry_id: Optional[str], qparams: RequestParams):
    collection = 'filtering_terms'
    messageRabbit = {
        "url":collection,
        "queryPost": ""
    }
    
    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)

    return jsonFile


def get_filtering_term_with_id(entry_id: Optional[str], qparams: RequestParams):
    collection = 'filtering_terms'
    messageRabbit = {
        "url":f'{collection}/{entry_id}',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile
