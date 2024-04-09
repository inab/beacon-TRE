
def createPOST(qparams):

    listFilters = []
    for filter in qparams.query.filters:
        filter["includeDescendantTerms"] = True
        listFilters.append(filter)
    include_resultset_responses = qparams.query.include_resultset_responses.name
    pagination = {
        "skip": qparams.query.pagination.skip,
        "limit": qparams.query.pagination.limit
    }
    testMode = qparams.query.test_mode
    requestedGranularity = qparams.query.requested_granularity.name.lower()
    
    templatePOST = {
        "meta": {
            "apiVersion": qparams.meta.api_version
        },
        "query": {
            "filters": listFilters,
            "includeResultsetResponses": include_resultset_responses,
            "pagination": pagination,
            "testMode": testMode,
            "requestedGranularity": requestedGranularity
        }
    }

    return templatePOST