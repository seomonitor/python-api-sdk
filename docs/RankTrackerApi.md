# seomonitor_client.RankTrackerApi

All URIs are relative to *https://apigw.seomonitor.com/v3/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rank_tracker_v30_daily_share_of_clicks_get**](RankTrackerApi.md#rank_tracker_v30_daily_share_of_clicks_get) | **GET** /rank-tracker/v3.0/daily-share-of-clicks | Get Daily Share of Clicks
[**rank_tracker_v30_groups_daily_visibility_get**](RankTrackerApi.md#rank_tracker_v30_groups_daily_visibility_get) | **GET** /rank-tracker/v3.0/groups/daily-visibility | Get Daily Group Visibility
[**rank_tracker_v30_groups_data_get**](RankTrackerApi.md#rank_tracker_v30_groups_data_get) | **GET** /rank-tracker/v3.0/groups/data | Get Groups Data
[**rank_tracker_v30_groups_get**](RankTrackerApi.md#rank_tracker_v30_groups_get) | **GET** /rank-tracker/v3.0/groups | Get Groups List
[**rank_tracker_v30_keywords_competition_get**](RankTrackerApi.md#rank_tracker_v30_keywords_competition_get) | **GET** /rank-tracker/v3.0/keywords/competition | Get Keywords Competition Data
[**rank_tracker_v30_keywords_daily_ranks_get**](RankTrackerApi.md#rank_tracker_v30_keywords_daily_ranks_get) | **GET** /rank-tracker/v3.0/keywords/daily-ranks | Get Daily Keyword Ranks
[**rank_tracker_v30_keywords_get**](RankTrackerApi.md#rank_tracker_v30_keywords_get) | **GET** /rank-tracker/v3.0/keywords | Get Keyword Data
[**rank_tracker_v30_keywords_import_post**](RankTrackerApi.md#rank_tracker_v30_keywords_import_post) | **POST** /rank-tracker/v3.0/keywords/import | Add New Keywords
[**rank_tracker_v30_keywords_import_status_get**](RankTrackerApi.md#rank_tracker_v30_keywords_import_status_get) | **GET** /rank-tracker/v3.0/keywords/import-status | Get Keywords Import Status
[**rank_tracker_v30_keywords_ranking_pages_get**](RankTrackerApi.md#rank_tracker_v30_keywords_ranking_pages_get) | **GET** /rank-tracker/v3.0/keywords/ranking-pages | Get Ranking Pages
[**rank_tracker_v30_keywords_serp_feature_presence_get**](RankTrackerApi.md#rank_tracker_v30_keywords_serp_feature_presence_get) | **GET** /rank-tracker/v3.0/keywords/serp-feature-presence | Get Daily SERP Feature Presence
[**rank_tracker_v30_keywords_top_results_get**](RankTrackerApi.md#rank_tracker_v30_keywords_top_results_get) | **GET** /rank-tracker/v3.0/keywords/top-results | Get Top 100 Results

# **rank_tracker_v30_daily_share_of_clicks_get**
> DailyShareOfClicks rank_tracker_v30_daily_share_of_clicks_get(campaign_id, start_date=start_date, end_date=end_date, group_id=group_id, keyword_ids=keyword_ids)

Get Daily Share of Clicks

Retrieves the daily share of clicks of your domain and the top ten ones by visibility, on a specific keyword list, for the selected timeframe.   You can use this endpoint in two ways:  to retrieve the Share of Clicks data of an existing keyword group created in the SEOmonitor campaign, by specifying the `group_id` in the request.  to retrieve the Share of Clicks data of a list of requested keywords, by specifying the list of `keyword_ids` in the request.

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
api_instance = seomonitor_client.RankTrackerApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.    Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
start_date = '2013-10-20' # date | This parameter specifies the start date of the timeframe for which you want to return the data, in YYYY-MM-DD format. (optional)
end_date = '2013-10-20' # date | This parameter specifies the end date of the timeframe for which you want to return the data in YYYY-MM-DD format. (optional)
group_id = 56 # int | The ID for the group of keywords for which the data must be returned.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. (optional)
keyword_ids = 'keyword_ids_example' # str | This parameter allows you to specify the IDs of the keywords for which you want to return Visibility data. `keyword_ids` should be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`). (optional)

try:
    # Get Daily Share of Clicks
    api_response = api_instance.rank_tracker_v30_daily_share_of_clicks_get(campaign_id, start_date=start_date, end_date=end_date, group_id=group_id, keyword_ids=keyword_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerApi->rank_tracker_v30_daily_share_of_clicks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.    Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **start_date** | **date**| This parameter specifies the start date of the timeframe for which you want to return the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| This parameter specifies the end date of the timeframe for which you want to return the data in YYYY-MM-DD format. | [optional] 
 **group_id** | **int**| The ID for the group of keywords for which the data must be returned.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a &#x60;group_id&#x60;, the default value is the &#x60;All Keywords&#x60; group, which means data will be returned for all active keywords in the campaign. | [optional] 
 **keyword_ids** | **str**| This parameter allows you to specify the IDs of the keywords for which you want to return Visibility data. &#x60;keyword_ids&#x60; should be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.  If you do not specify &#x60;keyword_ids&#x60;, the API will return data for all keywords that meet the other specified criteria (e.g. &#x60;group_id&#x60;). | [optional] 

### Return type

[**DailyShareOfClicks**](DailyShareOfClicks.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rank_tracker_v30_groups_daily_visibility_get**
> GroupDailyVisibility rank_tracker_v30_groups_daily_visibility_get(campaign_id, start_date, end_date, group_id=group_id, keyword_ids=keyword_ids, domain=domain, feature_visibility=feature_visibility)

Get Daily Group Visibility

Retrieves the daily Visibility and average weighted ranks of your website or of any other domain, for a group of keywords, over a specified timeframe.  You can use this endpoint in two ways:   to retrieve the Visibility data of an existing keyword group created in the SEOmonitor campaign, by specifying the `group_id` in the request.  to retrieve the Visibility data of a list of requested keywords, by specifying the list of `keyword_ids` in the request. 

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
api_instance = seomonitor_client.RankTrackerApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
start_date = '2013-10-20' # date | This parameter specifies the start date of the timeframe for which you want to return the data, in YYYY-MM-DD format.
end_date = '2013-10-20' # date | This parameter specifies the end date of the timeframe for which you want to return the data in YYYY-MM-DD format.
group_id = 56 # int | The ID for the group of keywords for which the data must be returned.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign.  (optional)
keyword_ids = 'keyword_ids_example' # str | This parameter allows you to specify the IDs of the keywords for which you want to return Visibility data. `keyword_ids` should be a comma-separated list of keyword IDs.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.   If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`). (optional)
domain = 'domain_example' # str | The domain name for which the Visibility will be returned.   If no domain is provided, the endpoint will return the data for the campaign's website. (optional)
feature_visibility = 'feature_visibility_example' # str | This parameter enables you to also retrieve the Visibility for one of the following SERP features: product_listing  `images_pack`  `questions`  `ads_pack`  `knowledge_graph`  `top_stories`  `local_pack`  `featured_snippet`  `recipes`  `news`  If no `feature_visibility` is specified, the endpoint will return an empty array. (optional)

try:
    # Get Daily Group Visibility
    api_response = api_instance.rank_tracker_v30_groups_daily_visibility_get(campaign_id, start_date, end_date, group_id=group_id, keyword_ids=keyword_ids, domain=domain, feature_visibility=feature_visibility)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerApi->rank_tracker_v30_groups_daily_visibility_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **start_date** | **date**| This parameter specifies the start date of the timeframe for which you want to return the data, in YYYY-MM-DD format. | 
 **end_date** | **date**| This parameter specifies the end date of the timeframe for which you want to return the data in YYYY-MM-DD format. | 
 **group_id** | **int**| The ID for the group of keywords for which the data must be returned.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a &#x60;group_id&#x60;, the default value is the &#x60;All Keywords&#x60; group, which means data will be returned for all active keywords in the campaign.  | [optional] 
 **keyword_ids** | **str**| This parameter allows you to specify the IDs of the keywords for which you want to return Visibility data. &#x60;keyword_ids&#x60; should be a comma-separated list of keyword IDs.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.   If you do not specify &#x60;keyword_ids&#x60;, the API will return data for all keywords that meet the other specified criteria (e.g. &#x60;group_id&#x60;). | [optional] 
 **domain** | **str**| The domain name for which the Visibility will be returned.   If no domain is provided, the endpoint will return the data for the campaign&#x27;s website. | [optional] 
 **feature_visibility** | **str**| This parameter enables you to also retrieve the Visibility for one of the following SERP features: product_listing  &#x60;images_pack&#x60;  &#x60;questions&#x60;  &#x60;ads_pack&#x60;  &#x60;knowledge_graph&#x60;  &#x60;top_stories&#x60;  &#x60;local_pack&#x60;  &#x60;featured_snippet&#x60;  &#x60;recipes&#x60;  &#x60;news&#x60;  If no &#x60;feature_visibility&#x60; is specified, the endpoint will return an empty array. | [optional] 

### Return type

[**GroupDailyVisibility**](GroupDailyVisibility.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rank_tracker_v30_groups_data_get**
> list[GroupDetails] rank_tracker_v30_groups_data_get(campaign_id, start_date, end_date, group_ids=group_ids, limit=limit, offset=offset)

Get Groups Data

With this endpoint, you can retrieve overall aggregated search and SERP data along with Visibility metrics and trends for all the keywords of the groups specified through group IDs.

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
api_instance = seomonitor_client.RankTrackerApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
start_date = '2013-10-20' # date | The start date of the timeframe for which you want to return the data in YYYY-MM-DD format.
end_date = '2013-10-20' # date | The end date of the timeframe for which you want to return the data in YYYY-MM-DD format.
group_ids = 'group_ids_example' # str | The ID(s) of the group(s) for which you want to return data.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is `All Keywords` group, which means data will be returned for all keywords in the campaign. (optional)
limit = 56 # int | This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record. (optional)

try:
    # Get Groups Data
    api_response = api_instance.rank_tracker_v30_groups_data_get(campaign_id, start_date, end_date, group_ids=group_ids, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerApi->rank_tracker_v30_groups_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **start_date** | **date**| The start date of the timeframe for which you want to return the data in YYYY-MM-DD format. | 
 **end_date** | **date**| The end date of the timeframe for which you want to return the data in YYYY-MM-DD format. | 
 **group_ids** | **str**| The ID(s) of the group(s) for which you want to return data.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a &#x60;group_id&#x60;, the default value is &#x60;All Keywords&#x60; group, which means data will be returned for all keywords in the campaign. | [optional] 
 **limit** | **int**| This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| This parameter specifies the starting point within the collection of resource results. It&#x27;s typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the API will start from the first record. | [optional] 

### Return type

[**list[GroupDetails]**](GroupDetails.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rank_tracker_v30_groups_get**
> list[Group] rank_tracker_v30_groups_get(campaign_id)

Get Groups List

This endpoint allows you to retrieve all keyword groups including their structure within folders, for a particular campaign ID. It provides the hierarchical data in a nested JSON structure, with the top-level groups (folders) for the campaign ID at the root level, and any groups nested under them. The response contains details on each group, including its unique ID, name, and type (folder, group, or smart group).

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
api_instance = seomonitor_client.RankTrackerApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | The campaign ID for which the group structure will be returned.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.

try:
    # Get Groups List
    api_response = api_instance.rank_tracker_v30_groups_get(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerApi->rank_tracker_v30_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The campaign ID for which the group structure will be returned.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 

### Return type

[**list[Group]**](Group.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rank_tracker_v30_keywords_competition_get**
> KeywordCompetition rank_tracker_v30_keywords_competition_get(campaign_id, start_date, end_date, device, search=search, keyword_ids=keyword_ids, group_id=group_id, competitors=competitors, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction)

Get Keywords Competition Data

This endpoint returns the specified competitors' ranking data for a campaign.

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
api_instance = seomonitor_client.RankTrackerApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | The ID of the campaign for which keyword competitor ranking data must be returned.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
start_date = '2013-10-20' # date | The start date of the date range to get ranking data for, in YYYY-MM-DD format. This is the earliest date of rankings to include.
end_date = '2013-10-20' # date | The end date of the date range to get ranking data for, in YYYY-MM-DD format. This is the most recent date of rankings to include.
device = 'device_example' # str | The device type to get ranking data for–either `desktop` or `mobile`.  The default selection is `desktop`.
search = 'search_example' # str | Allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. (optional)
keyword_ids = 'keyword_ids_example' # str | The IDs of the keywords for which you want to get competitor ranking data. `keyword_ids` should be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords in the campaign that meet the other specified criteria (e.g. `group_id`). (optional)
group_id = 56 # int | The ID of a specific group in the campaign to get competitor ranking data for. If not specified, returns data for all of the keywords in the campaign.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign.  (optional)
competitors = 'competitors_example' # str | An optional list of competitor domain names to filter the results by. The ranking data returned will only include the specified competitors. This parameter should be an array of strings containing one or more competitor domains, formatted as follows: `[\"examplecompetitor1.com\", \"examplecompetitor2.net\"]`   If you do not specify the competitors, the endpoint will return data for the competitors configured in the interface for the specified keyword group. (optional)
limit = 56 # int | Determines the maximum number of records to return in a single request. Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | The starting index within the results to begin returning data. Typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record. (optional)
order_by = 'order_by_example' # str | This parameter enables you to sort the returned data based on the parameter specified. Allowed values:  `keyword`  `rank`  `rank_trend`: Sorts the data based on the trend in keyword ranking.   If you do not specify the `order_by` parameter, the data will be sorted by default by the keyword name (`keyword`). (optional)
order_direction = 'order_direction_example' # str | Determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  Note: The `order_direction` parameter works in conjunction with the `order_by` parameter. Use it to specify the direction of the sort after choosing the field to order by.  If you do not specify an `order_direction`, the default is `asc`. (optional)

try:
    # Get Keywords Competition Data
    api_response = api_instance.rank_tracker_v30_keywords_competition_get(campaign_id, start_date, end_date, device, search=search, keyword_ids=keyword_ids, group_id=group_id, competitors=competitors, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerApi->rank_tracker_v30_keywords_competition_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The ID of the campaign for which keyword competitor ranking data must be returned.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **start_date** | **date**| The start date of the date range to get ranking data for, in YYYY-MM-DD format. This is the earliest date of rankings to include. | 
 **end_date** | **date**| The end date of the date range to get ranking data for, in YYYY-MM-DD format. This is the most recent date of rankings to include. | 
 **device** | **str**| The device type to get ranking data for–either &#x60;desktop&#x60; or &#x60;mobile&#x60;.  The default selection is &#x60;desktop&#x60;. | 
 **search** | **str**| Allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. | [optional] 
 **keyword_ids** | **str**| The IDs of the keywords for which you want to get competitor ranking data. &#x60;keyword_ids&#x60; should be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.  If you do not specify &#x60;keyword_ids&#x60;, the API will return data for all keywords in the campaign that meet the other specified criteria (e.g. &#x60;group_id&#x60;). | [optional] 
 **group_id** | **int**| The ID of a specific group in the campaign to get competitor ranking data for. If not specified, returns data for all of the keywords in the campaign.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a &#x60;group_id&#x60;, the default value is the &#x60;All Keywords&#x60; group, which means data will be returned for all active keywords in the campaign.  | [optional] 
 **competitors** | **str**| An optional list of competitor domain names to filter the results by. The ranking data returned will only include the specified competitors. This parameter should be an array of strings containing one or more competitor domains, formatted as follows: &#x60;[\&quot;examplecompetitor1.com\&quot;, \&quot;examplecompetitor2.net\&quot;]&#x60;   If you do not specify the competitors, the endpoint will return data for the competitors configured in the interface for the specified keyword group. | [optional] 
 **limit** | **int**| Determines the maximum number of records to return in a single request. Maximum Value: 1000 records per request  If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| The starting index within the results to begin returning data. Typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the API will start from the first record. | [optional] 
 **order_by** | **str**| This parameter enables you to sort the returned data based on the parameter specified. Allowed values:  &#x60;keyword&#x60;  &#x60;rank&#x60;  &#x60;rank_trend&#x60;: Sorts the data based on the trend in keyword ranking.   If you do not specify the &#x60;order_by&#x60; parameter, the data will be sorted by default by the keyword name (&#x60;keyword&#x60;). | [optional] 
 **order_direction** | **str**| Determines the sorting direction of the &#x60;order_by&#x60; field. You can sort the data in either ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;) order.  Note: The &#x60;order_direction&#x60; parameter works in conjunction with the &#x60;order_by&#x60; parameter. Use it to specify the direction of the sort after choosing the field to order by.  If you do not specify an &#x60;order_direction&#x60;, the default is &#x60;asc&#x60;. | [optional] 

### Return type

[**KeywordCompetition**](KeywordCompetition.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rank_tracker_v30_keywords_daily_ranks_get**
> KeywordDailyRanks rank_tracker_v30_keywords_daily_ranks_get(campaign_id, start_date, end_date, search=search, domain=domain, group_id=group_id, keyword_ids=keyword_ids, get_archive=get_archive, limit=limit, offset=offset)

Get Daily Keyword Ranks

This endpoint returns the daily desktop and mobile ranks for your website or any other domain in a specified timeframe for actively tracked or archived keywords.

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
api_instance = seomonitor_client.RankTrackerApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
start_date = '2013-10-20' # date | The start date of the timeframe for which you want to return the data, in YYYY-MM-DD format.
end_date = '2013-10-20' # date | The end date of the timeframe for which you want to return the data, in YYYY-MM-DD format.
search = 'search_example' # str | The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term.  The search parameter is case-insensitive, allowing partial matches irrespective of casing. (optional)
domain = 'domain_example' # str | The domain name for which the ranks will be returned.   If no `domain` is provided, the endpoint will return the data for the campaign's website. (optional)
group_id = 'group_id_example' # str | The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.   If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign.  (optional)
keyword_ids = 'keyword_ids_example' # str | The IDs of the keywords for which you want to return data. keyword_idsshould be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.   If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`). (optional)
get_archive = true # bool | If true, it returns data only for the archived (deleted) keywords that had been active during the requested timeframe.  The default value is `false` and will return the data only for actively tracked keywords. (optional)
limit = 56 # int | Determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | The starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record. (optional)

try:
    # Get Daily Keyword Ranks
    api_response = api_instance.rank_tracker_v30_keywords_daily_ranks_get(campaign_id, start_date, end_date, search=search, domain=domain, group_id=group_id, keyword_ids=keyword_ids, get_archive=get_archive, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerApi->rank_tracker_v30_keywords_daily_ranks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **start_date** | **date**| The start date of the timeframe for which you want to return the data, in YYYY-MM-DD format. | 
 **end_date** | **date**| The end date of the timeframe for which you want to return the data, in YYYY-MM-DD format. | 
 **search** | **str**| The &#x60;search&#x60; parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term.  The search parameter is case-insensitive, allowing partial matches irrespective of casing. | [optional] 
 **domain** | **str**| The domain name for which the ranks will be returned.   If no &#x60;domain&#x60; is provided, the endpoint will return the data for the campaign&#x27;s website. | [optional] 
 **group_id** | **str**| The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.   If you do not specify a &#x60;group_id&#x60;, the default value is the &#x60;All Keywords&#x60; group, which means data will be returned for all active keywords in the campaign.  | [optional] 
 **keyword_ids** | **str**| The IDs of the keywords for which you want to return data. keyword_idsshould be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.   If you do not specify &#x60;keyword_ids&#x60;, the API will return data for all keywords that meet the other specified criteria (e.g. &#x60;group_id&#x60;). | [optional] 
 **get_archive** | **bool**| If true, it returns data only for the archived (deleted) keywords that had been active during the requested timeframe.  The default value is &#x60;false&#x60; and will return the data only for actively tracked keywords. | [optional] 
 **limit** | **int**| Determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| The starting point within the collection of resource results. It&#x27;s typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the API will start from the first record. | [optional] 

### Return type

[**KeywordDailyRanks**](KeywordDailyRanks.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rank_tracker_v30_keywords_get**
> list[KeywordDetail] rank_tracker_v30_keywords_get(campaign_id, end_date, start_date, group_id=group_id, keyword_ids=keyword_ids, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction, search=search)

Get Keyword Data

This endpoint retrieves active keywords and their corresponding data within a specified timeframe from the Rank Tracker.   With this endpoint, you can get:  `Campaign-wide Data`: By default, this endpoint returns data for all active keywords in a specified campaign.  `Group-specific Data`: If you supply a `group_id`, the endpoint will return data only for the keywords in the specified group.  `Keyword-specific Data`: You can request data for specific keywords within a campaign by supplying their IDs using the `keyword_ids`  parameter. `keyword_ids` should be a comma-separated list of keyword IDs.   Note: Use other parameters like `limit`, `offset`, `order_by`, `order_direction`, and `search` to further customize the data retrieval as per your needs.

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
api_instance = seomonitor_client.RankTrackerApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. 
end_date = '2013-10-20' # date | This parameter specifies the end date of the timeframe for which you want to return the ranking and traffic data in YYYY-MM-DD format.  If you don't specify an `end_date`, the default is the current day.
start_date = '2013-10-20' # date | This parameter specifies the start date of the timeframe for which you want to return the ranking and traffic data in YYYY-MM-DD format.  If you don't specify a `start_date`, the default is 30 days before the `end_date`.
group_id = 56 # int | The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. (optional)
keyword_ids = 'keyword_ids_example' # str | This parameter allows you to specify the IDs of the keywords for which you want to return data. `keyword_ids` should be a comma-separated list of keyword IDs.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`). (optional)
limit = 56 # int | This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record. (optional)
order_by = 'order_by_example' # str | This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are: - `keyword` - `search_volume` - `year-over-year` - `rank` - `rank_trend`: Sorts the data based on the trend in keyword ranking. - `rank_trend_impact`: Sorts the data based on the rank trend impact on Visibility. - `opportunity`: Sorts the data based on the keyword Opportunity score.  (optional)
order_direction = 'order_direction_example' # str | This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  Note: The `order_direction` parameter works in conjunction with the `order_by` parameter. Use it to specify the direction of the sort after choosing the field to order by with `order_by`.  If you do not specify an `order_direction`, the default is `asc`. (optional)
search = 'search_example' # str | The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. The search parameter is case-insensitive, allowing partial matches irrespective of casing. (optional)

try:
    # Get Keyword Data
    api_response = api_instance.rank_tracker_v30_keywords_get(campaign_id, end_date, start_date, group_id=group_id, keyword_ids=keyword_ids, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerApi->rank_tracker_v30_keywords_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.  | 
 **end_date** | **date**| This parameter specifies the end date of the timeframe for which you want to return the ranking and traffic data in YYYY-MM-DD format.  If you don&#x27;t specify an &#x60;end_date&#x60;, the default is the current day. | 
 **start_date** | **date**| This parameter specifies the start date of the timeframe for which you want to return the ranking and traffic data in YYYY-MM-DD format.  If you don&#x27;t specify a &#x60;start_date&#x60;, the default is 30 days before the &#x60;end_date&#x60;. | 
 **group_id** | **int**| The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a &#x60;group_id&#x60;, the default value is the &#x60;All Keywords&#x60; group, which means data will be returned for all active keywords in the campaign. | [optional] 
 **keyword_ids** | **str**| This parameter allows you to specify the IDs of the keywords for which you want to return data. &#x60;keyword_ids&#x60; should be a comma-separated list of keyword IDs.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.  If you do not specify &#x60;keyword_ids&#x60;, the API will return data for all keywords that meet the other specified criteria (e.g. &#x60;group_id&#x60;). | [optional] 
 **limit** | **int**| This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| This parameter specifies the starting point within the collection of resource results. It&#x27;s typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the API will start from the first record. | [optional] 
 **order_by** | **str**| This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are: - &#x60;keyword&#x60; - &#x60;search_volume&#x60; - &#x60;year-over-year&#x60; - &#x60;rank&#x60; - &#x60;rank_trend&#x60;: Sorts the data based on the trend in keyword ranking. - &#x60;rank_trend_impact&#x60;: Sorts the data based on the rank trend impact on Visibility. - &#x60;opportunity&#x60;: Sorts the data based on the keyword Opportunity score.  | [optional] 
 **order_direction** | **str**| This parameter determines the sorting direction of the &#x60;order_by&#x60; field. You can sort the data in either ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;) order.  Note: The &#x60;order_direction&#x60; parameter works in conjunction with the &#x60;order_by&#x60; parameter. Use it to specify the direction of the sort after choosing the field to order by with &#x60;order_by&#x60;.  If you do not specify an &#x60;order_direction&#x60;, the default is &#x60;asc&#x60;. | [optional] 
 **search** | **str**| The &#x60;search&#x60; parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. The search parameter is case-insensitive, allowing partial matches irrespective of casing. | [optional] 

### Return type

[**list[KeywordDetail]**](KeywordDetail.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rank_tracker_v30_keywords_import_post**
> AddKeywords rank_tracker_v30_keywords_import_post(body)

Add New Keywords

With this endpoint, you can add a list of keywords to the specified groups of a campaign.   Note: The keywords added through this API endpoint will be charged according to our `pricing policy`. This endpoint cannot be used without setting `spend limits in the Billing section`. Unless you have spend limits set, the endpoint will return an error.  Note: the endpoint can also be used to allocate already tracked keywords to existing groups.

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
api_instance = seomonitor_client.RankTrackerApi(seomonitor_client.ApiClient(configuration))
body = seomonitor_client.KeywordsImportPostBody() # KeywordsImportPostBody | 

try:
    # Add New Keywords
    api_response = api_instance.rank_tracker_v30_keywords_import_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerApi->rank_tracker_v30_keywords_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KeywordsImportPostBody**](KeywordsImportPostBody.md)|  | 

### Return type

[**AddKeywords**](AddKeywords.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rank_tracker_v30_keywords_import_status_get**
> KeywordsImportStatus rank_tracker_v30_keywords_import_status_get(import_id, campaign_id)

Get Keywords Import Status

With this endpoint, you can retrieve the current status of a keyword import task using the provided import ID, with information on the number of keywords imported so far and the number remaining. 

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
api_instance = seomonitor_client.RankTrackerApi(seomonitor_client.ApiClient(configuration))
import_id = 56 # int | The import ID of the task.  Please refer to the Add New Keywords endpoint in our API to retrieve the `import_id`.
campaign_id = 56 # int | The ID of the campaign to which you want to add/import keywords.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. 

try:
    # Get Keywords Import Status
    api_response = api_instance.rank_tracker_v30_keywords_import_status_get(import_id, campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerApi->rank_tracker_v30_keywords_import_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **int**| The import ID of the task.  Please refer to the Add New Keywords endpoint in our API to retrieve the &#x60;import_id&#x60;. | 
 **campaign_id** | **int**| The ID of the campaign to which you want to add/import keywords.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.  | 

### Return type

[**KeywordsImportStatus**](KeywordsImportStatus.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rank_tracker_v30_keywords_ranking_pages_get**
> list[RankingPages] rank_tracker_v30_keywords_ranking_pages_get(campaign_id, group_id=group_id, limit=limit, offset=offset, search=search)

Get Ranking Pages

This endpoint returns the ranking pages of the tracked keywords in a campaign.  The response contains an array with ranking pages and their URL, title, description, and associated keyword IDs.  Note: Using the keyword IDs of the ranking keywords for the returned landing pages, you can make API calls through the other endpoints, in order to further process landing page-level search volumes, Visibility, and other metrics.

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
api_instance = seomonitor_client.RankTrackerApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
group_id = 56 # int | The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. (optional)
limit = 56 # int | Determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request.  If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | The starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the default is `0`, which means the API will start from the first record. (optional)
search = 'search_example' # str | The `search` parameter allows you to filter for landing pages that include the searched term or URL path. The API will return only those records where the landing page matches (fully or partially) the provided search term or URL. (optional)

try:
    # Get Ranking Pages
    api_response = api_instance.rank_tracker_v30_keywords_ranking_pages_get(campaign_id, group_id=group_id, limit=limit, offset=offset, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerApi->rank_tracker_v30_keywords_ranking_pages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **group_id** | **int**| The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a &#x60;group_id&#x60;, the default value is the &#x60;All Keywords&#x60; group, which means data will be returned for all active keywords in the campaign. | [optional] 
 **limit** | **int**| Determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request.  If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| The starting point within the collection of resource results. It&#x27;s typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the default is &#x60;0&#x60;, which means the API will start from the first record. | [optional] 
 **search** | **str**| The &#x60;search&#x60; parameter allows you to filter for landing pages that include the searched term or URL path. The API will return only those records where the landing page matches (fully or partially) the provided search term or URL. | [optional] 

### Return type

[**list[RankingPages]**](RankingPages.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rank_tracker_v30_keywords_serp_feature_presence_get**
> SerpFeaturePresence rank_tracker_v30_keywords_serp_feature_presence_get(campaign_id, start_date, end_date, group_id=group_id, keyword_ids=keyword_ids, limit=limit, offset=offset, search=search)

Get Daily SERP Feature Presence

This endpoint returns the historical daily SERP feature data for specified keywords over a specified timeframe.  It provides a comprehensive timeline view of the different SERP features present for each keyword on desktop and mobile searches. This includes detailed tracking of whether the website being monitored is listed in each detected feature per date.

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
api_instance = seomonitor_client.RankTrackerApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
start_date = '2013-10-20' # date | This parameter specifies the start date of the timeframe for which you want to return the data in YYYY-MM-DD format.
end_date = '2013-10-20' # date | This parameter specifies the end date of the timeframe for which you want to return the data in YYYY-MM-DD format.
group_id = 56 # int | The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign.  (optional)
keyword_ids = [56] # list[int] | This parameter allows you to specify the IDs of the keywords for which you want to return data. `keyword_ids` should be a comma-separated list of keyword IDs.  Please refer to the keyword-related endpoints in our API to retrieve the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`). (optional)
limit = 56 # int | This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record. (optional)
search = 'search_example' # str | The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. The search parameter is case-insensitive, allowing partial matches irrespective of casing. (optional)

try:
    # Get Daily SERP Feature Presence
    api_response = api_instance.rank_tracker_v30_keywords_serp_feature_presence_get(campaign_id, start_date, end_date, group_id=group_id, keyword_ids=keyword_ids, limit=limit, offset=offset, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerApi->rank_tracker_v30_keywords_serp_feature_presence_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **start_date** | **date**| This parameter specifies the start date of the timeframe for which you want to return the data in YYYY-MM-DD format. | 
 **end_date** | **date**| This parameter specifies the end date of the timeframe for which you want to return the data in YYYY-MM-DD format. | 
 **group_id** | **int**| The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a &#x60;group_id&#x60;, the default value is the &#x60;All Keywords&#x60; group, which means data will be returned for all active keywords in the campaign.  | [optional] 
 **keyword_ids** | [**list[int]**](int.md)| This parameter allows you to specify the IDs of the keywords for which you want to return data. &#x60;keyword_ids&#x60; should be a comma-separated list of keyword IDs.  Please refer to the keyword-related endpoints in our API to retrieve the IDs of your keywords.  If you do not specify &#x60;keyword_ids&#x60;, the API will return data for all keywords that meet the other specified criteria (e.g. &#x60;group_id&#x60;). | [optional] 
 **limit** | **int**| This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| This parameter specifies the starting point within the collection of resource results. It&#x27;s typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the API will start from the first record. | [optional] 
 **search** | **str**| The &#x60;search&#x60; parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. The search parameter is case-insensitive, allowing partial matches irrespective of casing. | [optional] 

### Return type

[**SerpFeaturePresence**](SerpFeaturePresence.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rank_tracker_v30_keywords_top_results_get**
> TopResults rank_tracker_v30_keywords_top_results_get(campaign_id, _date, device, group_id=group_id, keyword_ids=keyword_ids, limit=limit, offset=offset)

Get Top 100 Results

This endpoint returns the top 100 results for the requested keywords on a specified date.

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
api_instance = seomonitor_client.RankTrackerApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | The ID of the campaign for which keyword competitor ranking data must be returned.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
_date = '2013-10-20' # date | The date for which the ranking data will be provided, in YYYY-MM-DD format.
device = 'device_example' # str | The device type to get ranking data for–either `desktop` or `mobile`.  The default selection is `desktop`.
group_id = 56 # int | The IDs of specific groups in the campaign to get competitor ranking data for. If not specified, returns data for all of the keywords in the campaign.  Please refer to the Quick Start Guide to learn how to identify the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign.  (optional)
keyword_ids = [56] # list[int] | The IDs of the keywords for which you want to return the data. `keyword_ids` should be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to identify the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords in the campaign that meet the other specified criteria (e.g. `group_id`). (optional)
limit = 56 # int | Determines the maximum number of records to return in a single request. Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | The starting index within the results to begin returning data. Typically used with the `limit` parameter to implement pagination.  If you do not specify an offset, the default is `0`, which means the API will start from the first record. (optional)

try:
    # Get Top 100 Results
    api_response = api_instance.rank_tracker_v30_keywords_top_results_get(campaign_id, _date, device, group_id=group_id, keyword_ids=keyword_ids, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerApi->rank_tracker_v30_keywords_top_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The ID of the campaign for which keyword competitor ranking data must be returned.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **_date** | **date**| The date for which the ranking data will be provided, in YYYY-MM-DD format. | 
 **device** | **str**| The device type to get ranking data for–either &#x60;desktop&#x60; or &#x60;mobile&#x60;.  The default selection is &#x60;desktop&#x60;. | 
 **group_id** | **int**| The IDs of specific groups in the campaign to get competitor ranking data for. If not specified, returns data for all of the keywords in the campaign.  Please refer to the Quick Start Guide to learn how to identify the IDs of your groups.  If you do not specify a &#x60;group_id&#x60;, the default value is the &#x60;All Keywords&#x60; group, which means data will be returned for all active keywords in the campaign.  | [optional] 
 **keyword_ids** | [**list[int]**](int.md)| The IDs of the keywords for which you want to return the data. &#x60;keyword_ids&#x60; should be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to identify the IDs of your keywords.  If you do not specify &#x60;keyword_ids&#x60;, the API will return data for all keywords in the campaign that meet the other specified criteria (e.g. &#x60;group_id&#x60;). | [optional] 
 **limit** | **int**| Determines the maximum number of records to return in a single request. Maximum Value: 1000 records per request  If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| The starting index within the results to begin returning data. Typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an offset, the default is &#x60;0&#x60;, which means the API will start from the first record. | [optional] 

### Return type

[**TopResults**](TopResults.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

