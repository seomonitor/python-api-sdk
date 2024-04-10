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


class RankTrackerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def rank_tracker_v30_daily_share_of_clicks_get(self, campaign_id, **kwargs):  # noqa: E501
        """Get Daily Share of Clicks  # noqa: E501

        Retrieves the daily share of clicks of your domain and the top ten ones by visibility, on a specific keyword list, for the selected timeframe.   You can use this endpoint in two ways:  to retrieve the Share of Clicks data of an existing keyword group created in the SEOmonitor campaign, by specifying the `group_id` in the request.  to retrieve the Share of Clicks data of a list of requested keywords, by specifying the list of `keyword_ids` in the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_daily_share_of_clicks_get(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.    Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date start_date: This parameter specifies the start date of the timeframe for which you want to return the data, in YYYY-MM-DD format.
        :param date end_date: This parameter specifies the end date of the timeframe for which you want to return the data in YYYY-MM-DD format.
        :param int group_id: The ID for the group of keywords for which the data must be returned.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign.
        :param str keyword_ids: This parameter allows you to specify the IDs of the keywords for which you want to return Visibility data. `keyword_ids` should be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`).
        :return: DailyShareOfClicks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rank_tracker_v30_daily_share_of_clicks_get_with_http_info(campaign_id, **kwargs)  # noqa: E501
        else:
            (data) = self.rank_tracker_v30_daily_share_of_clicks_get_with_http_info(campaign_id, **kwargs)  # noqa: E501
            return data

    def rank_tracker_v30_daily_share_of_clicks_get_with_http_info(self, campaign_id, **kwargs):  # noqa: E501
        """Get Daily Share of Clicks  # noqa: E501

        Retrieves the daily share of clicks of your domain and the top ten ones by visibility, on a specific keyword list, for the selected timeframe.   You can use this endpoint in two ways:  to retrieve the Share of Clicks data of an existing keyword group created in the SEOmonitor campaign, by specifying the `group_id` in the request.  to retrieve the Share of Clicks data of a list of requested keywords, by specifying the list of `keyword_ids` in the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_daily_share_of_clicks_get_with_http_info(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.    Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date start_date: This parameter specifies the start date of the timeframe for which you want to return the data, in YYYY-MM-DD format.
        :param date end_date: This parameter specifies the end date of the timeframe for which you want to return the data in YYYY-MM-DD format.
        :param int group_id: The ID for the group of keywords for which the data must be returned.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign.
        :param str keyword_ids: This parameter allows you to specify the IDs of the keywords for which you want to return Visibility data. `keyword_ids` should be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`).
        :return: DailyShareOfClicks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'start_date', 'end_date', 'group_id', 'keyword_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rank_tracker_v30_daily_share_of_clicks_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `rank_tracker_v30_daily_share_of_clicks_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'keyword_ids' in params:
            query_params.append(('keyword_ids', params['keyword_ids']))  # noqa: E501

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
            '/rank-tracker/v3.0/daily-share-of-clicks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DailyShareOfClicks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rank_tracker_v30_groups_daily_visibility_get(self, campaign_id, start_date, end_date, **kwargs):  # noqa: E501
        """Get Daily Group Visibility  # noqa: E501

        Retrieves the daily Visibility and average weighted ranks of your website or of any other domain, for a group of keywords, over a specified timeframe.  You can use this endpoint in two ways:   to retrieve the Visibility data of an existing keyword group created in the SEOmonitor campaign, by specifying the `group_id` in the request.  to retrieve the Visibility data of a list of requested keywords, by specifying the list of `keyword_ids` in the request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_groups_daily_visibility_get(campaign_id, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date start_date: This parameter specifies the start date of the timeframe for which you want to return the data, in YYYY-MM-DD format. (required)
        :param date end_date: This parameter specifies the end date of the timeframe for which you want to return the data in YYYY-MM-DD format. (required)
        :param int group_id: The ID for the group of keywords for which the data must be returned.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. 
        :param str keyword_ids: This parameter allows you to specify the IDs of the keywords for which you want to return Visibility data. `keyword_ids` should be a comma-separated list of keyword IDs.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.   If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`).
        :param str domain: The domain name for which the Visibility will be returned.   If no domain is provided, the endpoint will return the data for the campaign's website.
        :param str feature_visibility: This parameter enables you to also retrieve the Visibility for one of the following SERP features: product_listing  `images_pack`  `questions`  `ads_pack`  `knowledge_graph`  `top_stories`  `local_pack`  `featured_snippet`  `recipes`  `news`  If no `feature_visibility` is specified, the endpoint will return an empty array.
        :return: GroupDailyVisibility
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rank_tracker_v30_groups_daily_visibility_get_with_http_info(campaign_id, start_date, end_date, **kwargs)  # noqa: E501
        else:
            (data) = self.rank_tracker_v30_groups_daily_visibility_get_with_http_info(campaign_id, start_date, end_date, **kwargs)  # noqa: E501
            return data

    def rank_tracker_v30_groups_daily_visibility_get_with_http_info(self, campaign_id, start_date, end_date, **kwargs):  # noqa: E501
        """Get Daily Group Visibility  # noqa: E501

        Retrieves the daily Visibility and average weighted ranks of your website or of any other domain, for a group of keywords, over a specified timeframe.  You can use this endpoint in two ways:   to retrieve the Visibility data of an existing keyword group created in the SEOmonitor campaign, by specifying the `group_id` in the request.  to retrieve the Visibility data of a list of requested keywords, by specifying the list of `keyword_ids` in the request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_groups_daily_visibility_get_with_http_info(campaign_id, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date start_date: This parameter specifies the start date of the timeframe for which you want to return the data, in YYYY-MM-DD format. (required)
        :param date end_date: This parameter specifies the end date of the timeframe for which you want to return the data in YYYY-MM-DD format. (required)
        :param int group_id: The ID for the group of keywords for which the data must be returned.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. 
        :param str keyword_ids: This parameter allows you to specify the IDs of the keywords for which you want to return Visibility data. `keyword_ids` should be a comma-separated list of keyword IDs.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.   If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`).
        :param str domain: The domain name for which the Visibility will be returned.   If no domain is provided, the endpoint will return the data for the campaign's website.
        :param str feature_visibility: This parameter enables you to also retrieve the Visibility for one of the following SERP features: product_listing  `images_pack`  `questions`  `ads_pack`  `knowledge_graph`  `top_stories`  `local_pack`  `featured_snippet`  `recipes`  `news`  If no `feature_visibility` is specified, the endpoint will return an empty array.
        :return: GroupDailyVisibility
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'start_date', 'end_date', 'group_id', 'keyword_ids', 'domain', 'feature_visibility']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rank_tracker_v30_groups_daily_visibility_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `rank_tracker_v30_groups_daily_visibility_get`")  # noqa: E501
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params or
                params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `rank_tracker_v30_groups_daily_visibility_get`")  # noqa: E501
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params or
                params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `rank_tracker_v30_groups_daily_visibility_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'keyword_ids' in params:
            query_params.append(('keyword_ids', params['keyword_ids']))  # noqa: E501
        if 'domain' in params:
            query_params.append(('domain', params['domain']))  # noqa: E501
        if 'feature_visibility' in params:
            query_params.append(('feature_visibility', params['feature_visibility']))  # noqa: E501

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
            '/rank-tracker/v3.0/groups/daily-visibility', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupDailyVisibility',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rank_tracker_v30_groups_data_get(self, campaign_id, start_date, end_date, **kwargs):  # noqa: E501
        """Get Groups Data  # noqa: E501

        With this endpoint, you can retrieve overall aggregated search and SERP data along with Visibility metrics and trends for all the keywords of the groups specified through group IDs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_groups_data_get(campaign_id, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date start_date: The start date of the timeframe for which you want to return the data in YYYY-MM-DD format. (required)
        :param date end_date: The end date of the timeframe for which you want to return the data in YYYY-MM-DD format. (required)
        :param str group_ids: The ID(s) of the group(s) for which you want to return data.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is `All Keywords` group, which means data will be returned for all keywords in the campaign.
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :return: list[GroupDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rank_tracker_v30_groups_data_get_with_http_info(campaign_id, start_date, end_date, **kwargs)  # noqa: E501
        else:
            (data) = self.rank_tracker_v30_groups_data_get_with_http_info(campaign_id, start_date, end_date, **kwargs)  # noqa: E501
            return data

    def rank_tracker_v30_groups_data_get_with_http_info(self, campaign_id, start_date, end_date, **kwargs):  # noqa: E501
        """Get Groups Data  # noqa: E501

        With this endpoint, you can retrieve overall aggregated search and SERP data along with Visibility metrics and trends for all the keywords of the groups specified through group IDs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_groups_data_get_with_http_info(campaign_id, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date start_date: The start date of the timeframe for which you want to return the data in YYYY-MM-DD format. (required)
        :param date end_date: The end date of the timeframe for which you want to return the data in YYYY-MM-DD format. (required)
        :param str group_ids: The ID(s) of the group(s) for which you want to return data.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is `All Keywords` group, which means data will be returned for all keywords in the campaign.
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :return: list[GroupDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'start_date', 'end_date', 'group_ids', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rank_tracker_v30_groups_data_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `rank_tracker_v30_groups_data_get`")  # noqa: E501
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params or
                params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `rank_tracker_v30_groups_data_get`")  # noqa: E501
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params or
                params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `rank_tracker_v30_groups_data_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'group_ids' in params:
            query_params.append(('group_ids', params['group_ids']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
            '/rank-tracker/v3.0/groups/data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GroupDetails]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rank_tracker_v30_groups_get(self, campaign_id, **kwargs):  # noqa: E501
        """Get Groups List  # noqa: E501

        This endpoint allows you to retrieve all keyword groups including their structure within folders, for a particular campaign ID. It provides the hierarchical data in a nested JSON structure, with the top-level groups (folders) for the campaign ID at the root level, and any groups nested under them. The response contains details on each group, including its unique ID, name, and type (folder, group, or smart group).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_groups_get(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: The campaign ID for which the group structure will be returned.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :return: list[Group]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rank_tracker_v30_groups_get_with_http_info(campaign_id, **kwargs)  # noqa: E501
        else:
            (data) = self.rank_tracker_v30_groups_get_with_http_info(campaign_id, **kwargs)  # noqa: E501
            return data

    def rank_tracker_v30_groups_get_with_http_info(self, campaign_id, **kwargs):  # noqa: E501
        """Get Groups List  # noqa: E501

        This endpoint allows you to retrieve all keyword groups including their structure within folders, for a particular campaign ID. It provides the hierarchical data in a nested JSON structure, with the top-level groups (folders) for the campaign ID at the root level, and any groups nested under them. The response contains details on each group, including its unique ID, name, and type (folder, group, or smart group).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_groups_get_with_http_info(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: The campaign ID for which the group structure will be returned.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :return: list[Group]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rank_tracker_v30_groups_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `rank_tracker_v30_groups_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501

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
            '/rank-tracker/v3.0/groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Group]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rank_tracker_v30_keywords_competition_get(self, campaign_id, start_date, end_date, device, **kwargs):  # noqa: E501
        """Get Keywords Competition Data  # noqa: E501

        This endpoint returns the specified competitors' ranking data for a campaign.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_competition_get(campaign_id, start_date, end_date, device, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: The ID of the campaign for which keyword competitor ranking data must be returned.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date start_date: The start date of the date range to get ranking data for, in YYYY-MM-DD format. This is the earliest date of rankings to include. (required)
        :param date end_date: The end date of the date range to get ranking data for, in YYYY-MM-DD format. This is the most recent date of rankings to include. (required)
        :param str device: The device type to get ranking data for–either `desktop` or `mobile`.  The default selection is `desktop`. (required)
        :param str search: Allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term.
        :param str keyword_ids: The IDs of the keywords for which you want to get competitor ranking data. `keyword_ids` should be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords in the campaign that meet the other specified criteria (e.g. `group_id`).
        :param int group_id: The ID of a specific group in the campaign to get competitor ranking data for. If not specified, returns data for all of the keywords in the campaign.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. 
        :param str competitors: An optional list of competitor domain names to filter the results by. The ranking data returned will only include the specified competitors. This parameter should be an array of strings containing one or more competitor domains, formatted as follows: `[\"examplecompetitor1.com\", \"examplecompetitor2.net\"]`   If you do not specify the competitors, the endpoint will return data for the competitors configured in the interface for the specified keyword group.
        :param int limit: Determines the maximum number of records to return in a single request. Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: The starting index within the results to begin returning data. Typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str order_by: This parameter enables you to sort the returned data based on the parameter specified. Allowed values:  `keyword`  `rank`  `rank_trend`: Sorts the data based on the trend in keyword ranking.   If you do not specify the `order_by` parameter, the data will be sorted by default by the keyword name (`keyword`).
        :param str order_direction: Determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  Note: The `order_direction` parameter works in conjunction with the `order_by` parameter. Use it to specify the direction of the sort after choosing the field to order by.  If you do not specify an `order_direction`, the default is `asc`.
        :return: KeywordCompetition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rank_tracker_v30_keywords_competition_get_with_http_info(campaign_id, start_date, end_date, device, **kwargs)  # noqa: E501
        else:
            (data) = self.rank_tracker_v30_keywords_competition_get_with_http_info(campaign_id, start_date, end_date, device, **kwargs)  # noqa: E501
            return data

    def rank_tracker_v30_keywords_competition_get_with_http_info(self, campaign_id, start_date, end_date, device, **kwargs):  # noqa: E501
        """Get Keywords Competition Data  # noqa: E501

        This endpoint returns the specified competitors' ranking data for a campaign.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_competition_get_with_http_info(campaign_id, start_date, end_date, device, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: The ID of the campaign for which keyword competitor ranking data must be returned.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date start_date: The start date of the date range to get ranking data for, in YYYY-MM-DD format. This is the earliest date of rankings to include. (required)
        :param date end_date: The end date of the date range to get ranking data for, in YYYY-MM-DD format. This is the most recent date of rankings to include. (required)
        :param str device: The device type to get ranking data for–either `desktop` or `mobile`.  The default selection is `desktop`. (required)
        :param str search: Allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term.
        :param str keyword_ids: The IDs of the keywords for which you want to get competitor ranking data. `keyword_ids` should be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords in the campaign that meet the other specified criteria (e.g. `group_id`).
        :param int group_id: The ID of a specific group in the campaign to get competitor ranking data for. If not specified, returns data for all of the keywords in the campaign.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. 
        :param str competitors: An optional list of competitor domain names to filter the results by. The ranking data returned will only include the specified competitors. This parameter should be an array of strings containing one or more competitor domains, formatted as follows: `[\"examplecompetitor1.com\", \"examplecompetitor2.net\"]`   If you do not specify the competitors, the endpoint will return data for the competitors configured in the interface for the specified keyword group.
        :param int limit: Determines the maximum number of records to return in a single request. Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: The starting index within the results to begin returning data. Typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str order_by: This parameter enables you to sort the returned data based on the parameter specified. Allowed values:  `keyword`  `rank`  `rank_trend`: Sorts the data based on the trend in keyword ranking.   If you do not specify the `order_by` parameter, the data will be sorted by default by the keyword name (`keyword`).
        :param str order_direction: Determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  Note: The `order_direction` parameter works in conjunction with the `order_by` parameter. Use it to specify the direction of the sort after choosing the field to order by.  If you do not specify an `order_direction`, the default is `asc`.
        :return: KeywordCompetition
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'start_date', 'end_date', 'device', 'search', 'keyword_ids', 'group_id', 'competitors', 'limit', 'offset', 'order_by', 'order_direction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rank_tracker_v30_keywords_competition_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `rank_tracker_v30_keywords_competition_get`")  # noqa: E501
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params or
                params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `rank_tracker_v30_keywords_competition_get`")  # noqa: E501
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params or
                params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `rank_tracker_v30_keywords_competition_get`")  # noqa: E501
        # verify the required parameter 'device' is set
        if ('device' not in params or
                params['device'] is None):
            raise ValueError("Missing the required parameter `device` when calling `rank_tracker_v30_keywords_competition_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'device' in params:
            query_params.append(('device', params['device']))  # noqa: E501
        if 'keyword_ids' in params:
            query_params.append(('keyword_ids', params['keyword_ids']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'competitors' in params:
            query_params.append(('competitors', params['competitors']))  # noqa: E501
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
            '/rank-tracker/v3.0/keywords/competition', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='KeywordCompetition',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rank_tracker_v30_keywords_daily_ranks_get(self, campaign_id, start_date, end_date, **kwargs):  # noqa: E501
        """Get Daily Keyword Ranks  # noqa: E501

        This endpoint returns the daily desktop and mobile ranks for your website or any other domain in a specified timeframe for actively tracked or archived keywords.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_daily_ranks_get(campaign_id, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date start_date: The start date of the timeframe for which you want to return the data, in YYYY-MM-DD format. (required)
        :param date end_date: The end date of the timeframe for which you want to return the data, in YYYY-MM-DD format. (required)
        :param str search: The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term.  The search parameter is case-insensitive, allowing partial matches irrespective of casing.
        :param str domain: The domain name for which the ranks will be returned.   If no `domain` is provided, the endpoint will return the data for the campaign's website.
        :param str group_id: The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.   If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. 
        :param str keyword_ids: The IDs of the keywords for which you want to return data. keyword_idsshould be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.   If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`).
        :param bool get_archive: If true, it returns data only for the archived (deleted) keywords that had been active during the requested timeframe.  The default value is `false` and will return the data only for actively tracked keywords.
        :param int limit: Determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: The starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :return: KeywordDailyRanks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rank_tracker_v30_keywords_daily_ranks_get_with_http_info(campaign_id, start_date, end_date, **kwargs)  # noqa: E501
        else:
            (data) = self.rank_tracker_v30_keywords_daily_ranks_get_with_http_info(campaign_id, start_date, end_date, **kwargs)  # noqa: E501
            return data

    def rank_tracker_v30_keywords_daily_ranks_get_with_http_info(self, campaign_id, start_date, end_date, **kwargs):  # noqa: E501
        """Get Daily Keyword Ranks  # noqa: E501

        This endpoint returns the daily desktop and mobile ranks for your website or any other domain in a specified timeframe for actively tracked or archived keywords.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_daily_ranks_get_with_http_info(campaign_id, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date start_date: The start date of the timeframe for which you want to return the data, in YYYY-MM-DD format. (required)
        :param date end_date: The end date of the timeframe for which you want to return the data, in YYYY-MM-DD format. (required)
        :param str search: The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term.  The search parameter is case-insensitive, allowing partial matches irrespective of casing.
        :param str domain: The domain name for which the ranks will be returned.   If no `domain` is provided, the endpoint will return the data for the campaign's website.
        :param str group_id: The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.   If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. 
        :param str keyword_ids: The IDs of the keywords for which you want to return data. keyword_idsshould be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.   If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`).
        :param bool get_archive: If true, it returns data only for the archived (deleted) keywords that had been active during the requested timeframe.  The default value is `false` and will return the data only for actively tracked keywords.
        :param int limit: Determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: The starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :return: KeywordDailyRanks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'start_date', 'end_date', 'search', 'domain', 'group_id', 'keyword_ids', 'get_archive', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rank_tracker_v30_keywords_daily_ranks_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `rank_tracker_v30_keywords_daily_ranks_get`")  # noqa: E501
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params or
                params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `rank_tracker_v30_keywords_daily_ranks_get`")  # noqa: E501
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params or
                params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `rank_tracker_v30_keywords_daily_ranks_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'domain' in params:
            query_params.append(('domain', params['domain']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'keyword_ids' in params:
            query_params.append(('keyword_ids', params['keyword_ids']))  # noqa: E501
        if 'get_archive' in params:
            query_params.append(('get_archive', params['get_archive']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
            '/rank-tracker/v3.0/keywords/daily-ranks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            #response_type='KeywordDailyRanks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rank_tracker_v30_keywords_get(self, campaign_id, end_date, start_date, **kwargs):  # noqa: E501
        """Get Keyword Data  # noqa: E501

        This endpoint retrieves active keywords and their corresponding data within a specified timeframe from the Rank Tracker.   With this endpoint, you can get:  `Campaign-wide Data`: By default, this endpoint returns data for all active keywords in a specified campaign.  `Group-specific Data`: If you supply a `group_id`, the endpoint will return data only for the keywords in the specified group.  `Keyword-specific Data`: You can request data for specific keywords within a campaign by supplying their IDs using the `keyword_ids`  parameter. `keyword_ids` should be a comma-separated list of keyword IDs.   Note: Use other parameters like `limit`, `offset`, `order_by`, `order_direction`, and `search` to further customize the data retrieval as per your needs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_get(campaign_id, end_date, start_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.  (required)
        :param date end_date: This parameter specifies the end date of the timeframe for which you want to return the ranking and traffic data in YYYY-MM-DD format.  If you don't specify an `end_date`, the default is the current day. (required)
        :param date start_date: This parameter specifies the start date of the timeframe for which you want to return the ranking and traffic data in YYYY-MM-DD format.  If you don't specify a `start_date`, the default is 30 days before the `end_date`. (required)
        :param int group_id: The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign.
        :param str keyword_ids: This parameter allows you to specify the IDs of the keywords for which you want to return data. `keyword_ids` should be a comma-separated list of keyword IDs.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`).
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str order_by: This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are: - `keyword` - `search_volume` - `year-over-year` - `rank` - `rank_trend`: Sorts the data based on the trend in keyword ranking. - `rank_trend_impact`: Sorts the data based on the rank trend impact on Visibility. - `opportunity`: Sorts the data based on the keyword Opportunity score. 
        :param str order_direction: This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  Note: The `order_direction` parameter works in conjunction with the `order_by` parameter. Use it to specify the direction of the sort after choosing the field to order by with `order_by`.  If you do not specify an `order_direction`, the default is `asc`.
        :param str search: The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. The search parameter is case-insensitive, allowing partial matches irrespective of casing.
        :return: list[KeywordDetail]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rank_tracker_v30_keywords_get_with_http_info(campaign_id, end_date, start_date, **kwargs)  # noqa: E501
        else:
            (data) = self.rank_tracker_v30_keywords_get_with_http_info(campaign_id, end_date, start_date, **kwargs)  # noqa: E501
            return data

    def rank_tracker_v30_keywords_get_with_http_info(self, campaign_id, end_date, start_date, **kwargs):  # noqa: E501
        """Get Keyword Data  # noqa: E501

        This endpoint retrieves active keywords and their corresponding data within a specified timeframe from the Rank Tracker.   With this endpoint, you can get:  `Campaign-wide Data`: By default, this endpoint returns data for all active keywords in a specified campaign.  `Group-specific Data`: If you supply a `group_id`, the endpoint will return data only for the keywords in the specified group.  `Keyword-specific Data`: You can request data for specific keywords within a campaign by supplying their IDs using the `keyword_ids`  parameter. `keyword_ids` should be a comma-separated list of keyword IDs.   Note: Use other parameters like `limit`, `offset`, `order_by`, `order_direction`, and `search` to further customize the data retrieval as per your needs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_get_with_http_info(campaign_id, end_date, start_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.  (required)
        :param date end_date: This parameter specifies the end date of the timeframe for which you want to return the ranking and traffic data in YYYY-MM-DD format.  If you don't specify an `end_date`, the default is the current day. (required)
        :param date start_date: This parameter specifies the start date of the timeframe for which you want to return the ranking and traffic data in YYYY-MM-DD format.  If you don't specify a `start_date`, the default is 30 days before the `end_date`. (required)
        :param int group_id: The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign.
        :param str keyword_ids: This parameter allows you to specify the IDs of the keywords for which you want to return data. `keyword_ids` should be a comma-separated list of keyword IDs.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`).
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str order_by: This parameter enables you to sort the returned data based on a specified field.  The field names you can use to sort data are: - `keyword` - `search_volume` - `year-over-year` - `rank` - `rank_trend`: Sorts the data based on the trend in keyword ranking. - `rank_trend_impact`: Sorts the data based on the rank trend impact on Visibility. - `opportunity`: Sorts the data based on the keyword Opportunity score. 
        :param str order_direction: This parameter determines the sorting direction of the `order_by` field. You can sort the data in either ascending (`asc`) or descending (`desc`) order.  Note: The `order_direction` parameter works in conjunction with the `order_by` parameter. Use it to specify the direction of the sort after choosing the field to order by with `order_by`.  If you do not specify an `order_direction`, the default is `asc`.
        :param str search: The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. The search parameter is case-insensitive, allowing partial matches irrespective of casing.
        :return: list[KeywordDetail]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'end_date', 'start_date', 'group_id', 'keyword_ids', 'limit', 'offset', 'order_by', 'order_direction', 'search']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rank_tracker_v30_keywords_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `rank_tracker_v30_keywords_get`")  # noqa: E501
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params or
                params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `rank_tracker_v30_keywords_get`")  # noqa: E501
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params or
                params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `rank_tracker_v30_keywords_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'keyword_ids' in params:
            query_params.append(('keyword_ids', params['keyword_ids']))  # noqa: E501
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
            '/rank-tracker/v3.0/keywords', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[KeywordDetail]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rank_tracker_v30_keywords_import_post(self, body, **kwargs):  # noqa: E501
        """Add New Keywords  # noqa: E501

        With this endpoint, you can add a list of keywords to the specified groups of a campaign.   Note: The keywords added through this API endpoint will be charged according to our `pricing policy`. This endpoint cannot be used without setting `spend limits in the Billing section`. Unless you have spend limits set, the endpoint will return an error.  Note: the endpoint can also be used to allocate already tracked keywords to existing groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_import_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KeywordsImportPostBody body: (required)
        :return: AddKeywords
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rank_tracker_v30_keywords_import_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.rank_tracker_v30_keywords_import_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def rank_tracker_v30_keywords_import_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add New Keywords  # noqa: E501

        With this endpoint, you can add a list of keywords to the specified groups of a campaign.   Note: The keywords added through this API endpoint will be charged according to our `pricing policy`. This endpoint cannot be used without setting `spend limits in the Billing section`. Unless you have spend limits set, the endpoint will return an error.  Note: the endpoint can also be used to allocate already tracked keywords to existing groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_import_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KeywordsImportPostBody body: (required)
        :return: AddKeywords
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rank_tracker_v30_keywords_import_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `rank_tracker_v30_keywords_import_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AuthorizationToken']  # noqa: E501

        return self.api_client.call_api(
            '/rank-tracker/v3.0/keywords/import', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddKeywords',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rank_tracker_v30_keywords_import_status_get(self, import_id, campaign_id, **kwargs):  # noqa: E501
        """Get Keywords Import Status  # noqa: E501

        With this endpoint, you can retrieve the current status of a keyword import task using the provided import ID, with information on the number of keywords imported so far and the number remaining.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_import_status_get(import_id, campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int import_id: The import ID of the task.  Please refer to the Add New Keywords endpoint in our API to retrieve the `import_id`. (required)
        :param int campaign_id: The ID of the campaign to which you want to add/import keywords.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.  (required)
        :return: KeywordsImportStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rank_tracker_v30_keywords_import_status_get_with_http_info(import_id, campaign_id, **kwargs)  # noqa: E501
        else:
            (data) = self.rank_tracker_v30_keywords_import_status_get_with_http_info(import_id, campaign_id, **kwargs)  # noqa: E501
            return data

    def rank_tracker_v30_keywords_import_status_get_with_http_info(self, import_id, campaign_id, **kwargs):  # noqa: E501
        """Get Keywords Import Status  # noqa: E501

        With this endpoint, you can retrieve the current status of a keyword import task using the provided import ID, with information on the number of keywords imported so far and the number remaining.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_import_status_get_with_http_info(import_id, campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int import_id: The import ID of the task.  Please refer to the Add New Keywords endpoint in our API to retrieve the `import_id`. (required)
        :param int campaign_id: The ID of the campaign to which you want to add/import keywords.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns.  (required)
        :return: KeywordsImportStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['import_id', 'campaign_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rank_tracker_v30_keywords_import_status_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'import_id' is set
        if ('import_id' not in params or
                params['import_id'] is None):
            raise ValueError("Missing the required parameter `import_id` when calling `rank_tracker_v30_keywords_import_status_get`")  # noqa: E501
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `rank_tracker_v30_keywords_import_status_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'import_id' in params:
            query_params.append(('import_id', params['import_id']))  # noqa: E501
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501

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
            '/rank-tracker/v3.0/keywords/import-status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='KeywordsImportStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rank_tracker_v30_keywords_ranking_pages_get(self, campaign_id, **kwargs):  # noqa: E501
        """Get Ranking Pages  # noqa: E501

        This endpoint returns the ranking pages of the tracked keywords in a campaign.  The response contains an array with ranking pages and their URL, title, description, and associated keyword IDs.  Note: Using the keyword IDs of the ranking keywords for the returned landing pages, you can make API calls through the other endpoints, in order to further process landing page-level search volumes, Visibility, and other metrics.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_ranking_pages_get(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param int group_id: The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign.
        :param int limit: Determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request.  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: The starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the default is `0`, which means the API will start from the first record.
        :param str search: The `search` parameter allows you to filter for landing pages that include the searched term or URL path. The API will return only those records where the landing page matches (fully or partially) the provided search term or URL.
        :return: list[RankingPages]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rank_tracker_v30_keywords_ranking_pages_get_with_http_info(campaign_id, **kwargs)  # noqa: E501
        else:
            (data) = self.rank_tracker_v30_keywords_ranking_pages_get_with_http_info(campaign_id, **kwargs)  # noqa: E501
            return data

    def rank_tracker_v30_keywords_ranking_pages_get_with_http_info(self, campaign_id, **kwargs):  # noqa: E501
        """Get Ranking Pages  # noqa: E501

        This endpoint returns the ranking pages of the tracked keywords in a campaign.  The response contains an array with ranking pages and their URL, title, description, and associated keyword IDs.  Note: Using the keyword IDs of the ranking keywords for the returned landing pages, you can make API calls through the other endpoints, in order to further process landing page-level search volumes, Visibility, and other metrics.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_ranking_pages_get_with_http_info(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param int group_id: The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign.
        :param int limit: Determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request.  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: The starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the default is `0`, which means the API will start from the first record.
        :param str search: The `search` parameter allows you to filter for landing pages that include the searched term or URL path. The API will return only those records where the landing page matches (fully or partially) the provided search term or URL.
        :return: list[RankingPages]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'group_id', 'limit', 'offset', 'search']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rank_tracker_v30_keywords_ranking_pages_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `rank_tracker_v30_keywords_ranking_pages_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
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
            '/rank-tracker/v3.0/keywords/ranking-pages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RankingPages]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rank_tracker_v30_keywords_serp_feature_presence_get(self, campaign_id, start_date, end_date, **kwargs):  # noqa: E501
        """Get Daily SERP Feature Presence  # noqa: E501

        This endpoint returns the historical daily SERP feature data for specified keywords over a specified timeframe.  It provides a comprehensive timeline view of the different SERP features present for each keyword on desktop and mobile searches. This includes detailed tracking of whether the website being monitored is listed in each detected feature per date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_serp_feature_presence_get(campaign_id, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date start_date: This parameter specifies the start date of the timeframe for which you want to return the data in YYYY-MM-DD format. (required)
        :param date end_date: This parameter specifies the end date of the timeframe for which you want to return the data in YYYY-MM-DD format. (required)
        :param int group_id: The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. 
        :param list[int] keyword_ids: This parameter allows you to specify the IDs of the keywords for which you want to return data. `keyword_ids` should be a comma-separated list of keyword IDs.  Please refer to the keyword-related endpoints in our API to retrieve the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`).
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str search: The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. The search parameter is case-insensitive, allowing partial matches irrespective of casing.
        :return: SerpFeaturePresence
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rank_tracker_v30_keywords_serp_feature_presence_get_with_http_info(campaign_id, start_date, end_date, **kwargs)  # noqa: E501
        else:
            (data) = self.rank_tracker_v30_keywords_serp_feature_presence_get_with_http_info(campaign_id, start_date, end_date, **kwargs)  # noqa: E501
            return data

    def rank_tracker_v30_keywords_serp_feature_presence_get_with_http_info(self, campaign_id, start_date, end_date, **kwargs):  # noqa: E501
        """Get Daily SERP Feature Presence  # noqa: E501

        This endpoint returns the historical daily SERP feature data for specified keywords over a specified timeframe.  It provides a comprehensive timeline view of the different SERP features present for each keyword on desktop and mobile searches. This includes detailed tracking of whether the website being monitored is listed in each detected feature per date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_serp_feature_presence_get_with_http_info(campaign_id, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: This parameter specifies the ID of the campaign for which you want to return data.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date start_date: This parameter specifies the start date of the timeframe for which you want to return the data in YYYY-MM-DD format. (required)
        :param date end_date: This parameter specifies the end date of the timeframe for which you want to return the data in YYYY-MM-DD format. (required)
        :param int group_id: The IDs of specific groups in the campaign to get keyword data for.   Please refer to the Quick Start Guide to learn how to retrieve the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. 
        :param list[int] keyword_ids: This parameter allows you to specify the IDs of the keywords for which you want to return data. `keyword_ids` should be a comma-separated list of keyword IDs.  Please refer to the keyword-related endpoints in our API to retrieve the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords that meet the other specified criteria (e.g. `group_id`).
        :param int limit: This parameter determines the maximum number of records to return in a single request.   Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: This parameter specifies the starting point within the collection of resource results. It's typically used with the `limit` parameter to implement pagination.  If you do not specify an `offset`, the API will start from the first record.
        :param str search: The `search` parameter allows you to filter the results based on a keyword search. The API will return only those records where the keyword matches (fully or partially) the provided search term. The search parameter is case-insensitive, allowing partial matches irrespective of casing.
        :return: SerpFeaturePresence
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', 'start_date', 'end_date', 'group_id', 'keyword_ids', 'limit', 'offset', 'search']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rank_tracker_v30_keywords_serp_feature_presence_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `rank_tracker_v30_keywords_serp_feature_presence_get`")  # noqa: E501
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params or
                params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `rank_tracker_v30_keywords_serp_feature_presence_get`")  # noqa: E501
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params or
                params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `rank_tracker_v30_keywords_serp_feature_presence_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'keyword_ids' in params:
            query_params.append(('keyword_ids', params['keyword_ids']))  # noqa: E501
            collection_formats['keyword_ids'] = 'multi'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
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
            '/rank-tracker/v3.0/keywords/serp-feature-presence', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SerpFeaturePresence',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rank_tracker_v30_keywords_top_results_get(self, campaign_id, _date, device, **kwargs):  # noqa: E501
        """Get Top 100 Results  # noqa: E501

        This endpoint returns the top 100 results for the requested keywords on a specified date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_top_results_get(campaign_id, _date, device, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: The ID of the campaign for which keyword competitor ranking data must be returned.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date _date: The date for which the ranking data will be provided, in YYYY-MM-DD format. (required)
        :param str device: The device type to get ranking data for–either `desktop` or `mobile`.  The default selection is `desktop`. (required)
        :param int group_id: The IDs of specific groups in the campaign to get competitor ranking data for. If not specified, returns data for all of the keywords in the campaign.  Please refer to the Quick Start Guide to learn how to identify the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. 
        :param list[int] keyword_ids: The IDs of the keywords for which you want to return the data. `keyword_ids` should be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to identify the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords in the campaign that meet the other specified criteria (e.g. `group_id`).
        :param int limit: Determines the maximum number of records to return in a single request. Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: The starting index within the results to begin returning data. Typically used with the `limit` parameter to implement pagination.  If you do not specify an offset, the default is `0`, which means the API will start from the first record.
        :return: TopResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rank_tracker_v30_keywords_top_results_get_with_http_info(campaign_id, _date, device, **kwargs)  # noqa: E501
        else:
            (data) = self.rank_tracker_v30_keywords_top_results_get_with_http_info(campaign_id, _date, device, **kwargs)  # noqa: E501
            return data

    def rank_tracker_v30_keywords_top_results_get_with_http_info(self, campaign_id, _date, device, **kwargs):  # noqa: E501
        """Get Top 100 Results  # noqa: E501

        This endpoint returns the top 100 results for the requested keywords on a specified date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rank_tracker_v30_keywords_top_results_get_with_http_info(campaign_id, _date, device, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: The ID of the campaign for which keyword competitor ranking data must be returned.  Please refer to the Quick Start Guide to learn how to retrieve the IDs of your campaigns. (required)
        :param date _date: The date for which the ranking data will be provided, in YYYY-MM-DD format. (required)
        :param str device: The device type to get ranking data for–either `desktop` or `mobile`.  The default selection is `desktop`. (required)
        :param int group_id: The IDs of specific groups in the campaign to get competitor ranking data for. If not specified, returns data for all of the keywords in the campaign.  Please refer to the Quick Start Guide to learn how to identify the IDs of your groups.  If you do not specify a `group_id`, the default value is the `All Keywords` group, which means data will be returned for all active keywords in the campaign. 
        :param list[int] keyword_ids: The IDs of the keywords for which you want to return the data. `keyword_ids` should be a comma-separated list of keyword IDs.   Please refer to the Quick Start Guide to learn how to identify the IDs of your keywords.  If you do not specify `keyword_ids`, the API will return data for all keywords in the campaign that meet the other specified criteria (e.g. `group_id`).
        :param int limit: Determines the maximum number of records to return in a single request. Maximum Value: 1000 records per request  If you do not specify a `limit`, the default number of records returned per request will be 100.
        :param int offset: The starting index within the results to begin returning data. Typically used with the `limit` parameter to implement pagination.  If you do not specify an offset, the default is `0`, which means the API will start from the first record.
        :return: TopResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id', '_date', 'device', 'group_id', 'keyword_ids', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rank_tracker_v30_keywords_top_results_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `rank_tracker_v30_keywords_top_results_get`")  # noqa: E501
        # verify the required parameter '_date' is set
        if ('_date' not in params or
                params['_date'] is None):
            raise ValueError("Missing the required parameter `_date` when calling `rank_tracker_v30_keywords_top_results_get`")  # noqa: E501
        # verify the required parameter 'device' is set
        if ('device' not in params or
                params['device'] is None):
            raise ValueError("Missing the required parameter `device` when calling `rank_tracker_v30_keywords_top_results_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if '_date' in params:
            query_params.append(('date', params['_date']))  # noqa: E501
        if 'device' in params:
            query_params.append(('device', params['device']))  # noqa: E501
        if 'group_id' in params:
            query_params.append(('group_id', params['group_id']))  # noqa: E501
        if 'keyword_ids' in params:
            query_params.append(('keyword_ids', params['keyword_ids']))  # noqa: E501
            collection_formats['keyword_ids'] = 'multi'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
            '/rank-tracker/v3.0/keywords/top-results', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TopResults',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
