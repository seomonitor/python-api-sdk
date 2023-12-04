# swagger_client.KeywordResearchApi

All URIs are relative to *https://apix.seomonitor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**research_v30_domain_overview_get**](KeywordResearchApi.md#research_v30_domain_overview_get) | **GET** /research/v3.0/domain-overview | Get URL/Domain Overview
[**research_v30_domain_ranking_keywords_get**](KeywordResearchApi.md#research_v30_domain_ranking_keywords_get) | **GET** /research/v3.0/domain-ranking-keywords | Get Ranking Keywords
[**research_v30_keywords_get**](KeywordResearchApi.md#research_v30_keywords_get) | **GET** /research/v3.0/keywords | Get Keyword Data
[**research_v30_ranking_data_get**](KeywordResearchApi.md#research_v30_ranking_data_get) | **GET** /research/v3.0/ranking-data | Get Ranking Data
[**research_v30_related_keywords_get**](KeywordResearchApi.md#research_v30_related_keywords_get) | **GET** /research/v3.0/related-keywords | Get Related Keywords
[**research_v30_topic_overview_get**](KeywordResearchApi.md#research_v30_topic_overview_get) | **GET** /research/v3.0/topic-overview | Get Topic Overview

# **research_v30_domain_overview_get**
> ResearchDomainOverview research_v30_domain_overview_get(campaign_id, url, gap_analysis=gap_analysis)

Get URL/Domain Overview

This endpoint returns the overall aggregated search, SERP, and Visibility data for all the ranking keywords of a specified domain or URL.

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
api_instance = swagger_client.KeywordResearchApi(swagger_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
url = 'url_example' # str | This parameter specifies the domain or URL path for which you want to return the data.   If you request a domain, the endpoint will return the data for the entire domain.   If you request a URL, the endpoint will return the data only for the specified URL path. 
gap_analysis = 'gap_analysis_example' # str | The type of keywords you want to return data for. Allowed values are `overlapping`, `non-overlapping`, or `all-keywords`.  If the `keyword_gap_type` is not specified, data for `all-keywords` is returned. (optional)

try:
    # Get URL/Domain Overview
    api_response = api_instance.research_v30_domain_overview_get(campaign_id, url, gap_analysis=gap_analysis)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeywordResearchApi->research_v30_domain_overview_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **url** | **str**| This parameter specifies the domain or URL path for which you want to return the data.   If you request a domain, the endpoint will return the data for the entire domain.   If you request a URL, the endpoint will return the data only for the specified URL path.  | 
 **gap_analysis** | **str**| The type of keywords you want to return data for. Allowed values are &#x60;overlapping&#x60;, &#x60;non-overlapping&#x60;, or &#x60;all-keywords&#x60;.  If the &#x60;keyword_gap_type&#x60; is not specified, data for &#x60;all-keywords&#x60; is returned. | [optional] 

### Return type

[**ResearchDomainOverview**](ResearchDomainOverview.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_v30_domain_ranking_keywords_get**
> DomainRankingsData research_v30_domain_ranking_keywords_get(campaign_id, url, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction, gap_analysis=gap_analysis, search=search)

Get Ranking Keywords

This endpoint returns the keywords on which the specified domain or URL ranks in top 100. For each keyword, it will return SERP, search and two sets of ranking data for your campaign domain, and for the requested one.

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
api_instance = swagger_client.KeywordResearchApi(swagger_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
url = 'url_example' # str | This parameter specifies the domain or URL path for which you want to return the keywords ranking in top 100.  If you request a domain, the endpoint will return the data for the entire domain.   If you request a URL, the endpoint will return the data only for the specified URL path.
limit = 56 # int | This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record. (optional)
order_by = 'order_by_example' # str | This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `search_volume`  `year-over-year`  `rank`: Sorts the data based on the keyword rank for the requested domain or URL.  `rank_trend`: Sorts the data based on the trend in keyword ranking for the requested domain or URL.  `my_rank`: Sorts the data based on the keyword rank for the tracked website.  `my_rank_trend`: Sorts the data based on the trend in keyword ranking for the tracked website.  `percentage_clicks`: Sorts the data based on the percentage of clicks that end up on organic results after discounting the impact of the top 10 SERP features present on the keyword.  (optional)
order_direction = 'order_direction_example' # str | This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`. (optional)
gap_analysis = 'gap_analysis_example' # str | The type of keywords you want to return data for. Allowed values are `overlapping`, `non-overlapping`, or `all-keywords`.   If the `keyword_gap_type` is not specified, data for `all-keywords` is returned. (optional)
search = 'search_example' # str | The `search` parameter allows you to filter the results based on a keyword name search. The API will return only those records where the keyword matches (fully or partially) the provided search term.  The search parameter is case-insensitive, allowing partial matches irrespective of casing.  (optional)

try:
    # Get Ranking Keywords
    api_response = api_instance.research_v30_domain_ranking_keywords_get(campaign_id, url, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction, gap_analysis=gap_analysis, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeywordResearchApi->research_v30_domain_ranking_keywords_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **url** | **str**| This parameter specifies the domain or URL path for which you want to return the keywords ranking in top 100.  If you request a domain, the endpoint will return the data for the entire domain.   If you request a URL, the endpoint will return the data only for the specified URL path. | 
 **limit** | **int**| This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| This parameter specifies the starting point within the collection of resource results. It&#x27;s typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the API will start from the first record. | [optional] 
 **order_by** | **str**| This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  &#x60;search_volume&#x60;  &#x60;year-over-year&#x60;  &#x60;rank&#x60;: Sorts the data based on the keyword rank for the requested domain or URL.  &#x60;rank_trend&#x60;: Sorts the data based on the trend in keyword ranking for the requested domain or URL.  &#x60;my_rank&#x60;: Sorts the data based on the keyword rank for the tracked website.  &#x60;my_rank_trend&#x60;: Sorts the data based on the trend in keyword ranking for the tracked website.  &#x60;percentage_clicks&#x60;: Sorts the data based on the percentage of clicks that end up on organic results after discounting the impact of the top 10 SERP features present on the keyword.  | [optional] 
 **order_direction** | **str**| This parameter determines the sorting direction of the &#x60;order_by&#x60; field. You can sort the data in either ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;) order.  If you do not specify an &#x60;order_direction&#x60;, the default is &#x60;asc&#x60;. | [optional] 
 **gap_analysis** | **str**| The type of keywords you want to return data for. Allowed values are &#x60;overlapping&#x60;, &#x60;non-overlapping&#x60;, or &#x60;all-keywords&#x60;.   If the &#x60;keyword_gap_type&#x60; is not specified, data for &#x60;all-keywords&#x60; is returned. | [optional] 
 **search** | **str**| The &#x60;search&#x60; parameter allows you to filter the results based on a keyword name search. The API will return only those records where the keyword matches (fully or partially) the provided search term.  The search parameter is case-insensitive, allowing partial matches irrespective of casing.  | [optional] 

### Return type

[**DomainRankingsData**](DomainRankingsData.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_v30_keywords_get**
> list[ResearchKeywords] research_v30_keywords_get(campaign_id, keywords, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction)

Get Keyword Data

This endpoint returns the SERP, search and your ranking data for the keywords specified in the request.

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
api_instance = swagger_client.KeywordResearchApi(swagger_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. 
keywords = 'keywords_example' # str | Comma-separated list of keyword phrases that you want to return data for. 
limit = 56 # int | This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record. (optional)
order_by = 'order_by_example' # str | This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `search_volume`  `year-over-year`  `rank`  `rank_trend`  `percentage_clicks` (optional)
order_direction = 'order_direction_example' # str | This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`. (optional)

try:
    # Get Keyword Data
    api_response = api_instance.research_v30_keywords_get(campaign_id, keywords, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeywordResearchApi->research_v30_keywords_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.  | 
 **keywords** | **str**| Comma-separated list of keyword phrases that you want to return data for.  | 
 **limit** | **int**| This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| This parameter specifies the starting point within the collection of resource results. It&#x27;s typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the API will start from the first record. | [optional] 
 **order_by** | **str**| This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  &#x60;search_volume&#x60;  &#x60;year-over-year&#x60;  &#x60;rank&#x60;  &#x60;rank_trend&#x60;  &#x60;percentage_clicks&#x60; | [optional] 
 **order_direction** | **str**| This parameter determines the sorting direction of the &#x60;order_by&#x60; field. You can sort the data in either ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;) order.  If you do not specify an &#x60;order_direction&#x60;, the default is &#x60;asc&#x60;. | [optional] 

### Return type

[**list[ResearchKeywords]**](ResearchKeywords.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_v30_ranking_data_get**
> list[KeywordResearchRankingData] research_v30_ranking_data_get(campaign_id, keywords, domains, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction)

Get Ranking Data

This endpoint returns the SERP, search, and ranking data for the keywords specified in the request, for both your campaign website and the specified domains or URLs.

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
api_instance = swagger_client.KeywordResearchApi(swagger_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. 
keywords = ['keywords_example'] # list[str] | A comma-separated list of keyword phrases that you want to return data for.
domains = 'domains_example' # str | A comma-separated list of domains for which you want to return the ranking data. The maximum number of domains allowed is 10.
limit = 56 # int | This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request   If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record. (optional)
order_by = 'order_by_example' # str | This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `rank`  `rank_trend`  If you do not specify an `order_by`parameter, the API will sort the data by `rank` by default. (optional)
order_direction = 'order_direction_example' # str | This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`. (optional)

try:
    # Get Ranking Data
    api_response = api_instance.research_v30_ranking_data_get(campaign_id, keywords, domains, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeywordResearchApi->research_v30_ranking_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.  | 
 **keywords** | [**list[str]**](str.md)| A comma-separated list of keyword phrases that you want to return data for. | 
 **domains** | **str**| A comma-separated list of domains for which you want to return the ranking data. The maximum number of domains allowed is 10. | 
 **limit** | **int**| This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request   If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| This parameter specifies the starting point within the collection of resource results. It&#x27;s typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the API will start from the first record. | [optional] 
 **order_by** | **str**| This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  &#x60;rank&#x60;  &#x60;rank_trend&#x60;  If you do not specify an &#x60;order_by&#x60;parameter, the API will sort the data by &#x60;rank&#x60; by default. | [optional] 
 **order_direction** | **str**| This parameter determines the sorting direction of the &#x60;order_by&#x60; field. You can sort the data in either ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;) order.  If you do not specify an &#x60;order_direction&#x60;, the default is &#x60;asc&#x60;. | [optional] 

### Return type

[**list[KeywordResearchRankingData]**](KeywordResearchRankingData.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_v30_related_keywords_get**
> list[TopicKeywordDetail] research_v30_related_keywords_get(campaign_id, keyword, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction, search=search)

Get Related Keywords

This endpoint returns the SERP, search, and your ranking data of the related keywords for a specified keyword (topic).

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
api_instance = swagger_client.KeywordResearchApi(swagger_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
keyword = 'keyword_example' # str | The topic for which you want to return related keywords' data.
limit = 56 # int | This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record. (optional)
order_by = 'order_by_example' # str | This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `connection_strength`  `search_volume`  `year-over-year`  `rank`  `rank_trend`  `percentage_clicks`  If not otherwise specified, the returned data will be sorted by `connection_strength` by default. (optional)
order_direction = 'order_direction_example' # str | This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`. (optional)
search = 'search_example' # str | The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. The search parameter is case-insensitive, allowing partial matches irrespective of casing.  (optional)

try:
    # Get Related Keywords
    api_response = api_instance.research_v30_related_keywords_get(campaign_id, keyword, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeywordResearchApi->research_v30_related_keywords_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **keyword** | **str**| The topic for which you want to return related keywords&#x27; data. | 
 **limit** | **int**| This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| This parameter specifies the starting point within the collection of resource results. It&#x27;s typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the API will start from the first record. | [optional] 
 **order_by** | **str**| This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  &#x60;connection_strength&#x60;  &#x60;search_volume&#x60;  &#x60;year-over-year&#x60;  &#x60;rank&#x60;  &#x60;rank_trend&#x60;  &#x60;percentage_clicks&#x60;  If not otherwise specified, the returned data will be sorted by &#x60;connection_strength&#x60; by default. | [optional] 
 **order_direction** | **str**| This parameter determines the sorting direction of the &#x60;order_by&#x60; field. You can sort the data in either ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;) order.  If you do not specify an &#x60;order_direction&#x60;, the default is &#x60;asc&#x60;. | [optional] 
 **search** | **str**| The &#x60;search&#x60; parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. The search parameter is case-insensitive, allowing partial matches irrespective of casing.  | [optional] 

### Return type

[**list[TopicKeywordDetail]**](TopicKeywordDetail.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_v30_topic_overview_get**
> TopicsOverview research_v30_topic_overview_get(campaign_id, keyword)

Get Topic Overview

This endpoint returns the overall aggregated search, SERP, and your website's Visibility data for all the related keywords of a specified keyword (topic). 

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
api_instance = swagger_client.KeywordResearchApi(swagger_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
keyword = 'keyword_example' # str | The topic for which you want to return related keywords' data.

try:
    # Get Topic Overview
    api_response = api_instance.research_v30_topic_overview_get(campaign_id, keyword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeywordResearchApi->research_v30_topic_overview_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **keyword** | **str**| The topic for which you want to return related keywords&#x27; data. | 

### Return type

[**TopicsOverview**](TopicsOverview.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

