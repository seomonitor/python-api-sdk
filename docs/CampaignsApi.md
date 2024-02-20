# seomonitor_client.CampaignsApi

All URIs are relative to *https://apigw.seomonitor.com/v3/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboard_v30_campaigns_tracked_get**](CampaignsApi.md#dashboard_v30_campaigns_tracked_get) | **GET** /dashboard/v3.0/campaigns/tracked | Get Tracked Campaigns

# **dashboard_v30_campaigns_tracked_get**
> list[CampaignDetailsRegular] dashboard_v30_campaigns_tracked_get(campaign_ids=campaign_ids, company_id=company_id, limit=limit, offset=offset)

Get Tracked Campaigns

This endpoint returns a list of active Tracked Campaigns with their details, such as campaign_id, name, URL, keyword number, date created, account manager details, and Visibility data.

### Example
```python
from __future__ import print_function
import time
import seomonitor_client
from seomonitor_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationToken
configuration = seomonitor_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = seomonitor_client.CampaignsApi(seomonitor_client.ApiClient(configuration))
campaign_ids = 'campaign_ids_example' # str | The Tracked Campaigns IDs for which you want the data to be returned.  Please refer to the Quick Start Guide to learn how to retrieve your campaign IDs.  If you do not specify `campaign_ids`, the endpoint will return the data for all active Tracked Campaigns you have access to, across all company accounts. (optional)
company_id = 56 # int | The ID of the subscription that contains the Tracked Campaigns for which you want to return data. This is useful for users who have access to multiple company accounts.  Please refer to the Quick Start Guide to learn how to retrieve your company IDs.  If you don't specify a `company_id`, the endpoint will return the data for all Tracked Campaigns you have access to, across all company accounts. (optional)
limit = 56 # int | The maximum number of Tracked Campaigns to return data for.   Maximum Value: 100 records per request  If you do not specify a `limit`, the default number of records returned per request will be 10. (optional)
offset = 56 # int | This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record. (optional)

try:
    # Get Tracked Campaigns
    api_response = api_instance.dashboard_v30_campaigns_tracked_get(campaign_ids=campaign_ids, company_id=company_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->dashboard_v30_campaigns_tracked_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_ids** | **str**| The Tracked Campaigns IDs for which you want the data to be returned.  Please refer to the Quick Start Guide to learn how to retrieve your campaign IDs.  If you do not specify &#x60;campaign_ids&#x60;, the endpoint will return the data for all active Tracked Campaigns you have access to, across all company accounts. | [optional] 
 **company_id** | **int**| The ID of the subscription that contains the Tracked Campaigns for which you want to return data. This is useful for users who have access to multiple company accounts.  Please refer to the Quick Start Guide to learn how to retrieve your company IDs.  If you don&#x27;t specify a &#x60;company_id&#x60;, the endpoint will return the data for all Tracked Campaigns you have access to, across all company accounts. | [optional] 
 **limit** | **int**| The maximum number of Tracked Campaigns to return data for.   Maximum Value: 100 records per request  If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 10. | [optional] 
 **offset** | **int**| This parameter specifies the starting point within the collection of resource results. It&#x27;s typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the API will start from the first record. | [optional] 

### Return type

[**list[CampaignDetailsRegular]**](CampaignDetailsRegular.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

