from typing import Optional
from beacon.request.model import  RequestParams
import json
from beacon.db import BeaconRpcClient
from beacon.db.utils import createPOST

def get_biosamples(entry_id: Optional[str], qparams: RequestParams):
    collection = 'biosamples'
    templatePost = createPOST(qparams)
    messageRabbit = {
        "url":collection,
        "queryPost": templatePost
    }
    
    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)

    return jsonFile


def get_biosample_with_id(entry_id: Optional[str], qparams: RequestParams):
    collection = 'biosamples'
    messageRabbit = {
        "url":f'{collection}/{entry_id}',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile

def get_variants_of_biosample(entry_id: Optional[str], qparams: RequestParams):
    collection = 'biosamples'
    messageRabbit = {
        "url":f'{collection}/{entry_id}/variants',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile

def get_analyses_of_biosample(entry_id: Optional[str], qparams: RequestParams):
    collection = 'biosamples'
    messageRabbit = {
        "url":f'{collection}/{entry_id}/analyses',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile

def get_runs_of_biosample(entry_id: Optional[str], qparams: RequestParams):
    collection = 'biosamples'
    messageRabbit = {

        "url":f'{collection}/{entry_id}/runs',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile

def get_filtering_terms_of_biosample(entry_id: Optional[str], qparams: RequestParams):
    collection = 'biosamples'
    messageRabbit = {
        "url":f'{collection}/filtering_terms',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile