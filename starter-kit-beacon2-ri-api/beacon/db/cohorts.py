from typing import Optional
from beacon.request.model import  RequestParams
import json
from beacon.db import BeaconRpcClient
from beacon.db.utils import createPOST

def get_cohorts(entry_id: Optional[str], qparams: RequestParams):
    collection = 'cohorts'
    templatePost = createPOST(qparams)
    messageRabbit = {
        "url":collection,
        "queryPost": templatePost
    }
    
    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)

    return jsonFile

def get_cohort_with_id(entry_id: Optional[str], qparams: RequestParams):
    collection = 'cohorts'
    messageRabbit = {
        "url":f'{collection}/{entry_id}',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile


def get_individuals_of_cohort(entry_id: Optional[str], qparams: RequestParams):
    collection = 'cohorts'
    messageRabbit = {
        "url":f'{collection}/{entry_id}/individuals',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile


def get_analyses_of_cohort(entry_id: Optional[str], qparams: RequestParams):
    collection = 'cohorts'
    messageRabbit = {
        "url":f'{collection}/{entry_id}/analyses',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile


def get_variants_of_cohort(entry_id: Optional[str], qparams: RequestParams):
    collection = 'cohorts'
    messageRabbit = {
        "url":f'{collection}/{entry_id}/variants',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile


def get_runs_of_cohort(entry_id: Optional[str], qparams: RequestParams):
    collection = 'cohorts'
    messageRabbit = {

        "url":f'{collection}/{entry_id}/runs',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile


def get_biosamples_of_cohort(entry_id: Optional[str], qparams: RequestParams):
    collection = 'cohorts'
    messageRabbit = {
        "url":f"{collection}/{entry_id}/biosamples",
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile


def get_filtering_terms_of_cohort(entry_id: Optional[str], qparams: RequestParams):
    collection = 'cohorts'
    messageRabbit = {
        "url":f'{collection}/filtering_terms',
        "queryPost": ""
    }

    beacon_rpc = BeaconRpcClient()
    response = beacon_rpc.call(str(messageRabbit))
    jsonFile = json.loads(response)
    return jsonFile
