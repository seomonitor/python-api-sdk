# seomonitor_client.ForecastApi

All URIs are relative to *https://apigw.seomonitor.com/v3/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_v30_keywords_get**](ForecastApi.md#forecast_v30_keywords_get) | **GET** /forecast/v3.0/keywords | Get Forecast keywords
[**forecast_v30_objective_get**](ForecastApi.md#forecast_v30_objective_get) | **GET** /forecast/v3.0/objective | Get Forecast objective Data
[**forecast_v30_scenario_get**](ForecastApi.md#forecast_v30_scenario_get) | **GET** /forecast/v3.0/scenario | Get Forecast scenario Data
[**forecast_v30_scenarios_get**](ForecastApi.md#forecast_v30_scenarios_get) | **GET** /forecast/v3.0/scenarios | Get Forecast scenarios

# **forecast_v30_keywords_get**
> list[ForecastKeywords] forecast_v30_keywords_get(campaign_id, forecast_id, limit=limit, offset=offset)

Get Forecast keywords

This endpoint returns the forecast data for the keywords included in the Forecast Scenario or Objective, including keyword data, target rank data, and additional traffic data, for the forecast timeframe.

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
api_instance = seomonitor_client.ForecastApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
forecast_id = 56 # int | This parameter specifies the ID of the Forecast scenario set as an Objective for which you want to return data.   Please refer to the 'Quick Start Guide'  to retrieve the ID of your scenarios. 
limit = 56 # int | This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request   If you do not specify a `limit`, the default number of records returned per request will be 100. (optional)
offset = 56 # int | This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record. (optional)

try:
    # Get Forecast keywords
    api_response = api_instance.forecast_v30_keywords_get(campaign_id, forecast_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForecastApi->forecast_v30_keywords_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **forecast_id** | **int**| This parameter specifies the ID of the Forecast scenario set as an Objective for which you want to return data.   Please refer to the &#x27;Quick Start Guide&#x27;  to retrieve the ID of your scenarios.  | 
 **limit** | **int**| This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request   If you do not specify a &#x60;limit&#x60;, the default number of records returned per request will be 100. | [optional] 
 **offset** | **int**| This parameter specifies the starting point within the collection of resource results. It&#x27;s typically used with the &#x60;limit&#x60; parameter to implement pagination.  If you do not specify an &#x60;offset&#x60;, the API will start from the first record. | [optional] 

### Return type

[**list[ForecastKeywords]**](ForecastKeywords.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_v30_objective_get**
> ForecastObjectiveData forecast_v30_objective_get(campaign_id, forecast_id)

Get Forecast objective Data

This endpoint returns the data of Forecast Scenarios set as Objectives, including the SEO goal and configuration parameters, the forecast results overview data, and the monthly actual and estimated results for the forecast timeframe.

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
api_instance = seomonitor_client.ForecastApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
forecast_id = 56 # int | This parameter specifies the ID of the Forecast scenario for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your Forecast scenarios. 

try:
    # Get Forecast objective Data
    api_response = api_instance.forecast_v30_objective_get(campaign_id, forecast_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForecastApi->forecast_v30_objective_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **forecast_id** | **int**| This parameter specifies the ID of the Forecast scenario for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your Forecast scenarios.  | 

### Return type

[**ForecastObjectiveData**](ForecastObjectiveData.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_v30_scenario_get**
> ForecastScenarioData forecast_v30_scenario_get(campaign_id, forecast_id)

Get Forecast scenario Data

This endpoint returns the data of Forecast Scenarios created in a specified campaign, including the scenario details, the SEO goal and configuration parameters, the forecast results overview data, and the monthly estimated results for the forecast timeframe.

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
api_instance = seomonitor_client.ForecastApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.
forecast_id = 56 # int | This parameter specifies the ID of the Forecast scenario for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your Forecast scenarios.  To get data for the Campaign Objective, use the 'Get Forecast Objective Data'. 

try:
    # Get Forecast scenario Data
    api_response = api_instance.forecast_v30_scenario_get(campaign_id, forecast_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForecastApi->forecast_v30_scenario_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 
 **forecast_id** | **int**| This parameter specifies the ID of the Forecast scenario for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your Forecast scenarios.  To get data for the Campaign Objective, use the &#x27;Get Forecast Objective Data&#x27;.  | 

### Return type

[**ForecastScenarioData**](ForecastScenarioData.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_v30_scenarios_get**
> Scenarios forecast_v30_scenarios_get(campaign_id)

Get Forecast scenarios

This endpoint returns a list of Scenarios created in a specified campaign, including the Objective if one is set, and their details.

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
api_instance = seomonitor_client.ForecastApi(seomonitor_client.ApiClient(configuration))
campaign_id = 56 # int | This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.

try:
    # Get Forecast scenarios
    api_response = api_instance.forecast_v30_scenarios_get(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForecastApi->forecast_v30_scenarios_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. | 

### Return type

[**Scenarios**](Scenarios.md)

### Authorization

[AuthorizationToken](../README.md#AuthorizationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

