# coding: utf-8

"""
    SEOmonitor API Documentation

    `Introduction`  The SEOmonitor API allows you to programmatically access keyword ranking, traffic, and other SEO data from the SEOmonitor platform. You can use the API to build custom reports, automate workflows, and integrate SEOmonitor data into your own applications. The API enables free and unrestricted access to all your data in the platform, for all Tracked Campaigns. Additionally, it provides access to SEOmonitor's curated UK and US keyword database.   `Main Capabilities`  These are the main data sets you can retrieve with the API 3.0 endpoints:  `Campaign-level data`: Campaign details and campaign-wide keyword data, landing page data, groups data, traffic data, content opportunities data, forecast data, or campaign website research data.  `Keyword-level data`: Data for any and all keywords in the campaign, including ranking data, search data, SERP data, competitor data, SEO Opportunity, keyword-level traffic data, content optimization opportunities' data by keyword and keyword-level forecast projections data.  `Keyword group-level data`: Data for any keyword group in the campaign, including aggregated search and SERP data, website Visibility on specific groups, group SEO Opportunity data.  `Landing page-level data`: Data for specific landing pages that are ranking with the keywords in the campaign, including aggregated search and SERP data, SEO Opportunity, and landing page Visibility.  `Organic traffic data`: Data for the website's organic sessions, conversions, and revenue, including traffic data by segments (brand, non-brand, all traffic, and custom user-created traffic segments), by specific keywords and by specific landing pages.  `Keyword & website research data`: Data for any keyword in SEOmonitor's Research database – any domain-level aggregated search, SERP, and ranking data, and keyword-level and keyword list-level metrics, for the tracked website and for any competitor in top 100.  `Forecast data`: Overview data and details for specific Forecast Scenarios and Objectives, and keyword-level forecast data.  `Website content data`: Data related to content optimization opportunities of the tracked website, including landing page and keyword data for each of the content opportunities categories in SEOmonitor's Content Audit platform (Positive and negative correlations with Visibility, Cannibalization issues, Pages serving too many keywords, Keywords with missing pages, Suboptimal keyword inclusion in the title or H1 or page content, Pages with missing title or H1).   `Getting Started`  Log into your SEOmonitor account and retrieve your unique API Token (Account Settings > Edit Profile).  Check out the `quick start guide` to make your first API call.  Read through the `authentication guide` to learn how to properly authenticate your API requests.   `Libraries and SDKs`  SEOmonitor API uses HTTP protocol, which allows the application of our API to almost all programming languages. All the responses are returned in JSON format by default.  For convenience, we offer client libraries for popular programming languages:  JavaScript PHP Python Java   `Support`  Need help using the API, or have general inquiries? Please contact our support team.  For more information about the SEOmonitor platform, you can visit www.seomonitor.com.   `Changelog`      This is the first version of API 3.0. The Changelog page will be updated as we continue to develop new features and improvements.     `Quick Start Guide`  This guide will walk you through making your first API call.  `Get your API key`  First, you'll need to get an API key:      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Go to Account Settings > Edit Profile     3. Copy the API Token to use in your API requests  Note: Clicking `Regenerate API Token` will overwrite the current key and you will lose access if you or other users are currently using it.   `Make a request`  Next, we'll use cURL to make a request to get Tracked Campaigns details:      curl --request GET \\     --url https://apigw.seomonitor.com/v3//dashboard/v3.0/campaigns/tracked \\     --header 'Accept: application/json' \\     --header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZW9tb25pdG9yLmNvbSIsImlhdCI6MTY1Mjc4NTcwNCwidXNlcl9pZCI6IjY2NTI5In0.2_l9e7ohs9QHbwmr48mIoEF-QxZHNPFiAzJbMk00jcA'  This will retrieve the Tracked Campaigns data for an SEOmonitor account having the following API Token:      'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZW9tb25pdG9yLmNvbSIsImlhdCI6MTY1Mjc4NTcwNCwidXNlcl9pZCI6IjY2NTI5In0.2_l9e7ohs9QHbwmr48mIoEF-QxZHNPFiAzJbMk00jcA'   Let's break down the parts of the request:      - `--request GET` - Make a GET request     - `--url` - The API endpoint URL     - `--header` - Adds the Authorization header with your API key   Handle the response  The API will return a JSON response like this:      {       \"campaign_info\": {         \"id\": \"74516\",         \"name\": \"Asos.com\",          \"company\": \"Asos\",         \"company_id\": \"51256\",         \"domain\": \"www.asos.com\",         \"keyword_count\": 588,          \"date_created\": \"2023-04-25\",         \"location\": \"United Kingdom\",         \"currency\": \"EUR\",         \"mrr\": 3000       },       \"visibility\": {         \"desktop\": {           \"latest\": 0.28,           \"trend_7days\": 0.2,           \"trend_30days\": 0.2         },         \"mobile\": {           \"latest\": 0.27,            \"trend_7days\": 0.2,           \"trend_30days\": 0.2         }       },       \"multiple_locations\": [         {           \"campaign_id\": 12746,           \"location\": \"London, United Kingdom\",           \"visibility\": {             \"desktop\": {               \"latest\": 0.32,               \"trend_7days\": 0.02               \"trend_30days: 0.1               },             \"mobile\": {               \"latest\": 0.33,               \"trend\": 0.03               \"trend_30days\": 0.1                 }             }           }         }       ],       \"health_status\": \"healthy\",       \"objective_status\": {         \"actual_sessions\": 78400,         \"estimated_sessions\": 78400,           \"performance\": 1,         \"status\": \"on_track\",         \"start_month\": \"Jun, 2023\",          \"end_month\": \"Jul, 2024\"       },       \"reporting_status\": \"submitted\",       \"account_manager\": \"Jo Hart\"     }  And that's it! You just made your first API call. Check out the rest of the API reference documentation to see what else you can build.  `Best practices`      - Keep your API key private – do not share your key publicly.     - Do not include your key directly in code that you distribute – use environment variables instead.     - Regenerate your key periodically for improved security.     - Limit API key access to only required endpoints if possible.  `Revoking API keys`  If your API key is compromised, you can revoke it by regenerating the API Token in your SEOmonitor Account Settings. This will immediately invalidate the current key so further requests can't be made.  For any other issues with authentication, contact our support team.   `Retrieve the IDs of the company, campaigns, keywords and keyword groups`  The unique IDs of your company, campaigns, keywords, or keyword groups can be retrieved either from the specific URLs of the platform, or from specific API endpoint responses. Further below you'll find details on these alternatives.   `Company ID`  The company ID can only be retrieved from the platform. Follow these steps:      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Go to Account Settings > Billing     3. In the Billing section, the platform URL contains the company ID.     E.g.: \"app.seomonitor.com/v2/account/company/51244/billing\" – in this example, the company ID is \"51244\"   `Campaign ID`  To retrieve the campaign ID from the platform, follow these steps:       1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign by clicking on its name in the Agency Dashboard.     3. By default, the campaign opens in the Rank Tracker view. The platform URL contains the company ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/0/desktop/keywords?timeframe=2023-09-04%3A2023-10-04\" – in this example, the campaign ID is \"72416\".  To retrieve the campaign ID through the API, make a call through the `Get Tracked Campaigns Details endpoint`. The response will contain the details of the requested Tracked Campaigns, including their IDs, which you can further use in other endpoint requests.   `Keyword ID`  To retrieve the keyword ID from the platform, follow these steps:       1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and click on the required keyword.     3. The platform URL for the keyword view (Keyword Sidebar) contains the keyword ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/0/desktop/keywords?timeframe=2023-09-04%3A2023-10-04&ksid=7063139\" – in this example, the keyword ID is \"7063139\"   To retrieve the keyword ID through the API, make a call through the `Get Keyword Data endpoint`. The response will contain the details of the requested keywords, including their IDs, which you can further use in other endpoint requests.   `Keyword Group ID`      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and click on the required keyword group (Groups side-menu).     3. The platform URL for the keyword group view contains the keyword ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/69976/desktop/keywords?timeframe=2023-09-04%3A2023-10-04\" – in this example, the keyword group ID is \"69976\"  To retrieve the keyword group ID through the API, make a call through the `Get Groups List endpoint`. The response will contain the details of the requested keyword groups, including their IDs, which you can further use in other endpoint requests.   `Forecast ID for Scenarios or Objectives`      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and go to Forecast from the main menu (top).     3. Select a Scenario or the Objective (if set). The platform URL for the specific scenario contains the forecast ID.     E.g.: \"https://app.seomonitor.com/v2/forecast/118794/3788\" – in this example, the forecast ID is \"3788\"   To retrieve the forecast ID through the API, make a call through the`Get Forecast Scenarios endpoint`. The response will contain the details of the requested Scenario or Objective, including their IDs, which you can further use in other endpoint requests.   `SERP Feature Abbreviations`  The returned data for some endpoints will contain SERP feature names in abbreviated form.  The returned values for SERP features are abbreviated as follows:      - \"adt\": Ads Pack Top     - \"def\": Definitions      - \"dir\": Directions      - \"fsn\": Featured Snippet      - \"flt\": Flights      - \"htl\": Hotels      - \"img\": Images Pack      - \"job\": Jobs      - \"kng\": Knowledge Graph      - \"geo\": Local Pack      - \"shp\": Product listing      - \"rcp\": Recipes      - \"qns\": Questions      - \"new\": Top Stories      - \"vid\": Video Carousel      - \"app\": Apps    `Rate Limits`  There are request limits in place to prevent abuse and ensure fair usage.   Exceeding the request limits will lead to HTTP 429 responses. If you need higher limits, contact our support team.   `Limits & Quotas`      -------------------------------------------------------------------------     |Limit                                    |  Number of requests              -------------------------------------------------------------------------     |Maximum requests per second              |  10                              -------------------------------------------------------------------------     |Maximum rows per request (Request Quota) |  1000                            -------------------------------------------------------------------------     |Daily Quota                              |  10 000                          -------------------------------------------------------------------------   `Exceeding Limits`  If you exceed the rate limits, you will receive a 429 Too Many Requests response.  Daily Quota Exceeded      {       \"error\": {         \"message\": \"Daily quota exceeded\",         \"details\": [           \"You have exceeded the allowed daily requests\"          ]       }     }  Details:  This error message indicates that the request exceeds the rate limits for daily requests. Retry the request after some delay.  Rate Limit Exceeded      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }  Details:  This error message indicates that the request exceeds the rate limits for requests per second. Retry the request after some delay.   `Increasing Limits`  The default limits allow most normal API usage patterns. However, if you need higher limits, please contact our support team.    Provide details on:      - Your specific use case      - The endpoints you are using     - The increased limits you are looking for  We will review your request and adjust limits where appropriate   `Need Higher Limits?`  For most use cases, the default limits are sufficient. But if you require higher limits, please contact our support team. We will review your use case and adjust limits where appropriate.   `Errors`  SEOmonitor API uses standard HTTP response codes to indicate the success or failure of API requests.   HTTP Status Codes      ----------------------------------------------------------------------------------     | Code  | Description                                                                 ----------------------------------------------------------------------------------     | 200   | Success                                                                     ----------------------------------------------------------------------------------     | 400   | Bad request - the request was malformed or missing required parameters      ----------------------------------------------------------------------------------      | 401   | Unauthorized - invalid or missing API key                                   ----------------------------------------------------------------------------------     | 403   | Forbidden - API key does not have access to the requested resource          ----------------------------------------------------------------------------------     | 404   | Not found - the requested resource does not exist                           ----------------------------------------------------------------------------------     | 429   | Too many requests - rate or quota limit exceeded                            ----------------------------------------------------------------------------------     | 500   | Internal server error - an unexpected error on the API server               ----------------------------------------------------------------------------------     | 50x   | Errors specific to various endpoints                                        ----------------------------------------------------------------------------------   `Error Response Format`  Error responses will be returned in JSON format:      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }   The error object contains:  - `message` - A general error message   - `details` - More specific details about the error   `Common Errors`  401 Unauthorized      {       \"error\": {         \"message\": \"Invalid authentication\",         \"details\": [           \"The API key provided is invalid\"          ]       }     }   Details:   This error message indicates there is a problem with the API key:  - The API key is missing from the request  - The key is invalid or incorrect  - The key is expired or revoked   Check that you are sending the correct API key in the Authorization header.  403 Forbidden      {       \"error\": {         \"message\": \"Forbidden access\",         \"details\": [           \"Your API key does not have access to the requested data\"          ]       }     }  Details:  This error message indicates that the API key being used does not have access to perform the requested operation. Ensure the key has the required scopes enabled.   404 Not Found      {       \"error\": {         \"message\": \"Data not found\",         \"details\": [           \"The requested data does not exist.\"          ]       }     }   Details:  This error message indicates that the object specified by the request does not exist. For example, requesting a keyword that is not in your SEOmonitor account.   429 Too Many Requests   Daily Quota Exceeded      {       \"error\": {         \"message\": \"Daily quota exceeded\",         \"details\": [           \"You have exceeded the allowed daily requests\"          ]       }     }   Details:  This error message indicates that the request exceeds the rate limits for daily requests. Retry the request after some delay.   Rate Limit Exceeded      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }   Details:  This error message indicates that the request exceeds the rate limits for requests per second. Retry the request after some delay.   500 Internal Server Error       {       \"error\": {         \"message\": \"Internal server error\",         \"details\": [           \"The server encountered an error while processing your requests\"          ]       }     }   Details:  This error message indicates that an unexpected error occurred on the API server. Try the request again later. If the issue persists, contact support.   50X Endpoint-specific errors  You may encounter errors on specific endpoint requests – these are listed and explained under each endpoint page.   Support  If you have any questions about API errors, please contact our support team.   `Changelog`  Version 3.0 (current)   Release Date: ?  This is the first version of the API 3.0.    # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: customer.success@seomonitor.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from seomonitor_client.api_client import ApiClient


class KeywordResearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def research_v30_domain_overview_get(self, campaign_id, url, **kwargs):  # noqa: E501
        """Get URL/Domain Overview  # noqa: E501

        This endpoint returns the overall aggregated search, SERP, and Visibility data for all the ranking keywords of a specified domain or URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.research_v30_domain_overview_get(campaign_id, url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param str url: This parameter specifies the domain or URL path for which you want to return the data.   If you request a domain, the endpoint will return the data for the entire domain.   If you request a URL, the endpoint will return the data only for the specified URL path.  (required)
        :param str gap_analysis: The type of keywords you want to return data for. Allowed values are `overlapping`, `non-overlapping`, or `all-keywords`.  If the `keyword_gap_type` is not specified, data for `all-keywords` is returned.
        :return: ResearchDomainOverview
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.research_v30_domain_overview_get_with_http_info(campaign_id, url, **kwargs)  # noqa: E501
        else:
            (data) = self.research_v30_domain_overview_get_with_http_info(campaign_id, url, **kwargs)  # noqa: E501
            return data

    def research_v30_domain_overview_get_with_http_info(self, campaign_id, url, **kwargs):  # noqa: E501
        """Get URL/Domain Overview  # noqa: E501

        This endpoint returns the overall aggregated search, SERP, and Visibility data for all the ranking keywords of a specified domain or URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.research_v30_domain_overview_get_with_http_info(campaign_id, url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param str url: This parameter specifies the domain or URL path for which you want to return the data.   If you request a domain, the endpoint will return the data for the entire domain.   If you request a URL, the endpoint will return the data only for the specified URL path.  (required)
        :param str gap_analysis: The type of keywords you want to return data for. Allowed values are `overlapping`, `non-overlapping`, or `all-keywords`.  If the `keyword_gap_type` is not specified, data for `all-keywords` is returned.
        :return: ResearchDomainOverview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'url', 'gap_analysis']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method research_v30_domain_overview_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `research_v30_domain_overview_get`")  # noqa: E501
        # verify the required parameter 'url' is set
        if ('url' not in params or
                params['url'] is None):
            raise ValueError("Missing the required parameter `url` when calling `research_v30_domain_overview_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501
        if 'gap_analysis' in params:
            query_params.append(('gap_analysis', params['gap_analysis']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationToken']  # noqa: E501

        return self.api_client.call_api(
            '/research/v3.0/domain-overview', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResearchDomainOverview',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def research_v30_domain_ranking_keywords_get(self, campaign_id, url, **kwargs):  # noqa: E501
        """Get Ranking Keywords  # noqa: E501

        This endpoint returns the keywords on which the specified domain or URL ranks in top 100. For each keyword, it will return SERP, search and two sets of ranking data for your campaign domain, and for the requested one.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.research_v30_domain_ranking_keywords_get(campaign_id, url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param str url: This parameter specifies the domain or URL path for which you want to return the keywords ranking in top 100.  If you request a domain, the endpoint will return the data for the entire domain.   If you request a URL, the endpoint will return the data only for the specified URL path. (required)
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str order_by: This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `search_volume`  `year-over-year`  `rank`: Sorts the data based on the keyword rank for the requested domain or URL.  `rank_trend`: Sorts the data based on the trend in keyword ranking for the requested domain or URL.  `my_rank`: Sorts the data based on the keyword rank for the tracked website.  `my_rank_trend`: Sorts the data based on the trend in keyword ranking for the tracked website.  `percentage_clicks`: Sorts the data based on the percentage of clicks that end up on organic results after discounting the impact of the top 10 SERP features present on the keyword. 
        :param str order_direction: This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`.
        :param str gap_analysis: The type of keywords you want to return data for. Allowed values are `overlapping`, `non-overlapping`, or `all-keywords`.   If the `keyword_gap_type` is not specified, data for `all-keywords` is returned.
        :param str search: The `search` parameter allows you to filter the results based on a keyword name search. The API will return only those records where the keyword matches (fully or partially) the provided search term.  The search parameter is case-insensitive, allowing partial matches irrespective of casing. 
        :return: DomainRankingsData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.research_v30_domain_ranking_keywords_get_with_http_info(campaign_id, url, **kwargs)  # noqa: E501
        else:
            (data) = self.research_v30_domain_ranking_keywords_get_with_http_info(campaign_id, url, **kwargs)  # noqa: E501
            return data

    def research_v30_domain_ranking_keywords_get_with_http_info(self, campaign_id, url, **kwargs):  # noqa: E501
        """Get Ranking Keywords  # noqa: E501

        This endpoint returns the keywords on which the specified domain or URL ranks in top 100. For each keyword, it will return SERP, search and two sets of ranking data for your campaign domain, and for the requested one.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.research_v30_domain_ranking_keywords_get_with_http_info(campaign_id, url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param str url: This parameter specifies the domain or URL path for which you want to return the keywords ranking in top 100.  If you request a domain, the endpoint will return the data for the entire domain.   If you request a URL, the endpoint will return the data only for the specified URL path. (required)
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str order_by: This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `search_volume`  `year-over-year`  `rank`: Sorts the data based on the keyword rank for the requested domain or URL.  `rank_trend`: Sorts the data based on the trend in keyword ranking for the requested domain or URL.  `my_rank`: Sorts the data based on the keyword rank for the tracked website.  `my_rank_trend`: Sorts the data based on the trend in keyword ranking for the tracked website.  `percentage_clicks`: Sorts the data based on the percentage of clicks that end up on organic results after discounting the impact of the top 10 SERP features present on the keyword. 
        :param str order_direction: This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`.
        :param str gap_analysis: The type of keywords you want to return data for. Allowed values are `overlapping`, `non-overlapping`, or `all-keywords`.   If the `keyword_gap_type` is not specified, data for `all-keywords` is returned.
        :param str search: The `search` parameter allows you to filter the results based on a keyword name search. The API will return only those records where the keyword matches (fully or partially) the provided search term.  The search parameter is case-insensitive, allowing partial matches irrespective of casing. 
        :return: DomainRankingsData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'url', 'limit', 'offset', 'order_by', 'order_direction', 'gap_analysis', 'search']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method research_v30_domain_ranking_keywords_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `research_v30_domain_ranking_keywords_get`")  # noqa: E501
        # verify the required parameter 'url' is set
        if ('url' not in params or
                params['url'] is None):
            raise ValueError("Missing the required parameter `url` when calling `research_v30_domain_ranking_keywords_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'order_direction' in params:
            query_params.append(('order_direction', params['order_direction']))  # noqa: E501
        if 'gap_analysis' in params:
            query_params.append(('gap_analysis', params['gap_analysis']))  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationToken']  # noqa: E501

        return self.api_client.call_api(
            '/research/v3.0/domain-ranking-keywords', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainRankingsData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def research_v30_keywords_get(self, campaign_id, keywords, **kwargs):  # noqa: E501
        """Get Keyword Data  # noqa: E501

        This endpoint returns the SERP, search and your ranking data for the keywords specified in the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.research_v30_keywords_get(campaign_id, keywords, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.  (required)
        :param str keywords: Comma-separated list of keyword phrases that you want to return data for.  (required)
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str order_by: This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `search_volume`  `year-over-year`  `rank`  `rank_trend`  `percentage_clicks`
        :param str order_direction: This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`.
        :return: list[ResearchKeywords]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.research_v30_keywords_get_with_http_info(campaign_id, keywords, **kwargs)  # noqa: E501
        else:
            (data) = self.research_v30_keywords_get_with_http_info(campaign_id, keywords, **kwargs)  # noqa: E501
            return data

    def research_v30_keywords_get_with_http_info(self, campaign_id, keywords, **kwargs):  # noqa: E501
        """Get Keyword Data  # noqa: E501

        This endpoint returns the SERP, search and your ranking data for the keywords specified in the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.research_v30_keywords_get_with_http_info(campaign_id, keywords, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.  (required)
        :param str keywords: Comma-separated list of keyword phrases that you want to return data for.  (required)
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str order_by: This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `search_volume`  `year-over-year`  `rank`  `rank_trend`  `percentage_clicks`
        :param str order_direction: This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`.
        :return: list[ResearchKeywords]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'keywords', 'limit', 'offset', 'order_by', 'order_direction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method research_v30_keywords_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `research_v30_keywords_get`")  # noqa: E501
        # verify the required parameter 'keywords' is set
        if ('keywords' not in params or
                params['keywords'] is None):
            raise ValueError("Missing the required parameter `keywords` when calling `research_v30_keywords_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'keywords' in params:
            query_params.append(('keywords', params['keywords']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'order_direction' in params:
            query_params.append(('order_direction', params['order_direction']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationToken']  # noqa: E501

        return self.api_client.call_api(
            '/research/v3.0/keywords', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ResearchKeywords]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def research_v30_ranking_data_get(self, campaign_id, keywords, domains, **kwargs):  # noqa: E501
        """Get Ranking Data  # noqa: E501

        This endpoint returns the SERP, search, and ranking data for the keywords specified in the request, for both your campaign website and the specified domains or URLs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.research_v30_ranking_data_get(campaign_id, keywords, domains, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.  (required)
        :param list[str] keywords: A comma-separated list of keyword phrases that you want to return data for. (required)
        :param str domains: A comma-separated list of domains for which you want to return the ranking data. The maximum number of domains allowed is 10. (required)
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request   If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str order_by: This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `rank`  `rank_trend`  If you do not specify an `order_by`parameter, the API will sort the data by `rank` by default.
        :param str order_direction: This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`.
        :return: list[KeywordResearchRankingData]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.research_v30_ranking_data_get_with_http_info(campaign_id, keywords, domains, **kwargs)  # noqa: E501
        else:
            (data) = self.research_v30_ranking_data_get_with_http_info(campaign_id, keywords, domains, **kwargs)  # noqa: E501
            return data

    def research_v30_ranking_data_get_with_http_info(self, campaign_id, keywords, domains, **kwargs):  # noqa: E501
        """Get Ranking Data  # noqa: E501

        This endpoint returns the SERP, search, and ranking data for the keywords specified in the request, for both your campaign website and the specified domains or URLs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.research_v30_ranking_data_get_with_http_info(campaign_id, keywords, domains, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.  (required)
        :param list[str] keywords: A comma-separated list of keyword phrases that you want to return data for. (required)
        :param str domains: A comma-separated list of domains for which you want to return the ranking data. The maximum number of domains allowed is 10. (required)
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request   If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str order_by: This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `rank`  `rank_trend`  If you do not specify an `order_by`parameter, the API will sort the data by `rank` by default.
        :param str order_direction: This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`.
        :return: list[KeywordResearchRankingData]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'keywords', 'domains', 'limit', 'offset', 'order_by', 'order_direction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method research_v30_ranking_data_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `research_v30_ranking_data_get`")  # noqa: E501
        # verify the required parameter 'keywords' is set
        if ('keywords' not in params or
                params['keywords'] is None):
            raise ValueError("Missing the required parameter `keywords` when calling `research_v30_ranking_data_get`")  # noqa: E501
        # verify the required parameter 'domains' is set
        if ('domains' not in params or
                params['domains'] is None):
            raise ValueError("Missing the required parameter `domains` when calling `research_v30_ranking_data_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'keywords' in params:
            query_params.append(('keywords', params['keywords']))  # noqa: E501
            collection_formats['keywords'] = 'multi'  # noqa: E501
        if 'domains' in params:
            query_params.append(('domains', params['domains']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'order_direction' in params:
            query_params.append(('order_direction', params['order_direction']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationToken']  # noqa: E501

        return self.api_client.call_api(
            '/research/v3.0/ranking-data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[KeywordResearchRankingData]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def research_v30_related_keywords_get(self, campaign_id, keyword, **kwargs):  # noqa: E501
        """Get Related Keywords  # noqa: E501

        This endpoint returns the SERP, search, and your ranking data of the related keywords for a specified keyword (topic).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.research_v30_related_keywords_get(campaign_id, keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param str keyword: The topic for which you want to return related keywords' data. (required)
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str order_by: This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `connection_strength`  `search_volume`  `year-over-year`  `rank`  `rank_trend`  `percentage_clicks`  If not otherwise specified, the returned data will be sorted by `connection_strength` by default.
        :param str order_direction: This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`.
        :param str search: The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. The search parameter is case-insensitive, allowing partial matches irrespective of casing. 
        :return: list[TopicKeywordDetail]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.research_v30_related_keywords_get_with_http_info(campaign_id, keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.research_v30_related_keywords_get_with_http_info(campaign_id, keyword, **kwargs)  # noqa: E501
            return data

    def research_v30_related_keywords_get_with_http_info(self, campaign_id, keyword, **kwargs):  # noqa: E501
        """Get Related Keywords  # noqa: E501

        This endpoint returns the SERP, search, and your ranking data of the related keywords for a specified keyword (topic).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.research_v30_related_keywords_get_with_http_info(campaign_id, keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param str keyword: The topic for which you want to return related keywords' data. (required)
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str order_by: This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are:  `connection_strength`  `search_volume`  `year-over-year`  `rank`  `rank_trend`  `percentage_clicks`  If not otherwise specified, the returned data will be sorted by `connection_strength` by default.
        :param str order_direction: This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  If you do not specify an `order_direction`, the default is `asc`.
        :param str search: The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. The search parameter is case-insensitive, allowing partial matches irrespective of casing. 
        :return: list[TopicKeywordDetail]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'keyword', 'limit', 'offset', 'order_by', 'order_direction', 'search']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method research_v30_related_keywords_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `research_v30_related_keywords_get`")  # noqa: E501
        # verify the required parameter 'keyword' is set
        if ('keyword' not in params or
                params['keyword'] is None):
            raise ValueError("Missing the required parameter `keyword` when calling `research_v30_related_keywords_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'order_direction' in params:
            query_params.append(('order_direction', params['order_direction']))  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationToken']  # noqa: E501

        return self.api_client.call_api(
            '/research/v3.0/related-keywords', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TopicKeywordDetail]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def research_v30_topic_overview_get(self, campaign_id, keyword, **kwargs):  # noqa: E501
        """Get Topic Overview  # noqa: E501

        This endpoint returns the overall aggregated search, SERP, and your website's Visibility data for all the related keywords of a specified keyword (topic).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.research_v30_topic_overview_get(campaign_id, keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param str keyword: The topic for which you want to return related keywords' data. (required)
        :return: TopicsOverview
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.research_v30_topic_overview_get_with_http_info(campaign_id, keyword, **kwargs)  # noqa: E501
        else:
            (data) = self.research_v30_topic_overview_get_with_http_info(campaign_id, keyword, **kwargs)  # noqa: E501
            return data

    def research_v30_topic_overview_get_with_http_info(self, campaign_id, keyword, **kwargs):  # noqa: E501
        """Get Topic Overview  # noqa: E501

        This endpoint returns the overall aggregated search, SERP, and your website's Visibility data for all the related keywords of a specified keyword (topic).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.research_v30_topic_overview_get_with_http_info(campaign_id, keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param str keyword: The topic for which you want to return related keywords' data. (required)
        :return: TopicsOverview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'keyword']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method research_v30_topic_overview_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `research_v30_topic_overview_get`")  # noqa: E501
        # verify the required parameter 'keyword' is set
        if ('keyword' not in params or
                params['keyword'] is None):
            raise ValueError("Missing the required parameter `keyword` when calling `research_v30_topic_overview_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationToken']  # noqa: E501

        return self.api_client.call_api(
            '/research/v3.0/topic-overview', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TopicsOverview',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
