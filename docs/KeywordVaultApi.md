# swagger_client.KeywordVaultApi

All URIs are relative to *https://apix.seomonitor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keyword_vault_v30_get_keyword_data_by_list_get**](KeywordVaultApi.md#keyword_vault_v30_get_keyword_data_by_list_get) | **GET** /keyword-vault/v3.0/get-keyword-data-by-list | Get Keyword Data by List
[**keyword_vault_v30_get_overview_data_get**](KeywordVaultApi.md#keyword_vault_v30_get_overview_data_get) | **GET** /keyword-vault/v3.0/get-overview-data | Get Overview Data

# **keyword_vault_v30_get_keyword_data_by_list_get**
> KeywordVaultGetKeywordDataByList keyword_vault_v30_get_keyword_data_by_list_get(campaign_id, list, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction, search=search)

Get Keyword Data by List

This endpoint returns the SERP, search and ranking data for the keywords in a specified list within the Keyword Vault of a specified campaign. The ranking data is for both the website tracked in the specified SEOmonitor campaign and for the specified competitor websites.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.KeywordVaultApi(swagger_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
list = 'list_example' # str | The name of the list created in the Keyword Vault for which you want to return keyword data.
limit = 56 # int | This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record. (optional)
order_by = 'order_by_example' # str | This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `search_volume`  `year-over-year`  `rank`  `rank_trend`  `percentage_clicks`  If not otherwise specified, the returned data will be sorted by `connection_strength` by default. (optional)
order_direction = 'order_direction_example' # str | This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`. (optional)
search = 'search_example' # str | The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term.  The search parameter is case-insensitive, allowing partial matches irrespective of casing.  (optional)

try:
    # Get Keyword Data by List
    api_response = api_instance.keyword_vault_v30_get_keyword_data_by_list_get(campaign_id, list, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeywordVaultApi->keyword_vault_v30_get_keyword_data_by_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **list** | **str**| The name of the list created in the Keyword Vault for which you want to return keyword data. | 
 **limit** | **int**| This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| This parameter specifies the starting point within the collection of resource results. It&#x27;s typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the API will start from the first record. | [optional] 
 **order_by** | **str**| This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  &#x60;search_volume&#x60;  &#x60;year-over-year&#x60;  &#x60;rank&#x60;  &#x60;rank_trend&#x60;  &#x60;percentage_clicks&#x60;  If not otherwise specified, the returned data will be sorted by &#x60;connection_strength&#x60; by default. | [optional] 
 **order_direction** | **str**| This parameter determines the sorting direction of the &#x60;order_by&#x60; field. You can sort the data in either ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;) order.  If you do not specify an &#x60;order_direction&#x60;, the default is &#x60;asc&#x60;. | [optional] 
 **search** | **str**| The &#x60;search&#x60; parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term.  The search parameter is case-insensitive, allowing partial matches irrespective of casing.  | [optional] 

### Return type

[**KeywordVaultGetKeywordDataByList**](KeywordVaultGetKeywordDataByList.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keyword_vault_v30_get_overview_data_get**
> KeywordVaultGetOverviewData keyword_vault_v30_get_overview_data_get(campaign_id, list)

Get Overview Data

This endpoint returns the overall aggregated search, SERP, and Visibility data for all the keywords of a specified list in the Keyword Vault.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthorizationToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.KeywordVaultApi(swagger_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
list = 'list_example' # str | The name of the list created in the Keyword Vault for which you want to return keyword data.

try:
    # Get Overview Data
    api_response = api_instance.keyword_vault_v30_get_overview_data_get(campaign_id, list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeywordVaultApi->keyword_vault_v30_get_overview_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **list** | **str**| The name of the list created in the Keyword Vault for which you want to return keyword data. | 

### Return type

[**KeywordVaultGetOverviewData**](KeywordVaultGetOverviewData.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

