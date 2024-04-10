# coding: utf-8

"""
    SEOmonitor API Documentation

    `Introduction`  The SEOmonitor API allows you to programmatically access keyword ranking, traffic, and other SEO data from the SEOmonitor platform. You can use the API to build custom reports, automate workflows, and integrate SEOmonitor data into your own applications. The API enables free and unrestricted access to all your data in the platform, for all Tracked Campaigns. Additionally, it provides access to SEOmonitor's curated UK and US keyword database.   `Main Capabilities`  These are the main data sets you can retrieve with the API 3.0 endpoints:  `Campaign-level data`: Campaign details and campaign-wide keyword data, landing page data, groups data, traffic data, content opportunities data, forecast data, or campaign website research data.  `Keyword-level data`: Data for any and all keywords in the campaign, including ranking data, search data, SERP data, competitor data, SEO Opportunity, keyword-level traffic data, content optimization opportunities' data by keyword and keyword-level forecast projections data.  `Keyword group-level data`: Data for any keyword group in the campaign, including aggregated search and SERP data, website Visibility on specific groups, group SEO Opportunity data.  `Landing page-level data`: Data for specific landing pages that are ranking with the keywords in the campaign, including aggregated search and SERP data, SEO Opportunity, and landing page Visibility.  `Organic traffic data`: Data for the website's organic sessions, conversions, and revenue, including traffic data by segments (brand, non-brand, all traffic, and custom user-created traffic segments), by specific keywords and by specific landing pages.  `Keyword & website research data`: Data for any keyword in SEOmonitor's Research database – any domain-level aggregated search, SERP, and ranking data, and keyword-level and keyword list-level metrics, for the tracked website and for any competitor in top 100.  `Forecast data`: Overview data and details for specific Forecast Scenarios and Objectives, and keyword-level forecast data.  `Website content data`: Data related to content optimization opportunities of the tracked website, including landing page and keyword data for each of the content opportunities categories in SEOmonitor's Content Audit platform (Positive and negative correlations with Visibility, Cannibalization issues, Pages serving too many keywords, Keywords with missing pages, Suboptimal keyword inclusion in the title or H1 or page content, Pages with missing title or H1).   `Getting Started`  Log into your SEOmonitor account and retrieve your unique API Token (Account Settings > Edit Profile).  Check out the `quick start guide` to make your first API call.  Read through the `authentication guide` to learn how to properly authenticate your API requests.   `Libraries and SDKs`  SEOmonitor API uses HTTP protocol, which allows the application of our API to almost all programming languages. All the responses are returned in JSON format by default.  For convenience, we offer client libraries for popular programming languages:  JavaScript PHP Python Java   `Support`  Need help using the API, or have general inquiries? Please contact our support team.  For more information about the SEOmonitor platform, you can visit www.seomonitor.com.   `Changelog`      This is the first version of API 3.0. The Changelog page will be updated as we continue to develop new features and improvements.     `Quick Start Guide`  This guide will walk you through making your first API call.  `Get your API key`  First, you'll need to get an API key:      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Go to Account Settings > Edit Profile     3. Copy the API Token to use in your API requests  Note: Clicking `Regenerate API Token` will overwrite the current key and you will lose access if you or other users are currently using it.   `Make a request`  Next, we'll use cURL to make a request to get Tracked Campaigns details:      curl --request GET \\     --url https://apigw.seomonitor.com/v3//dashboard/v3.0/campaigns/tracked \\     --header 'Accept: application/json' \\     --header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZW9tb25pdG9yLmNvbSIsImlhdCI6MTY1Mjc4NTcwNCwidXNlcl9pZCI6IjY2NTI5In0.2_l9e7ohs9QHbwmr48mIoEF-QxZHNPFiAzJbMk00jcA'  This will retrieve the Tracked Campaigns data for an SEOmonitor account having the following API Token:      'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZW9tb25pdG9yLmNvbSIsImlhdCI6MTY1Mjc4NTcwNCwidXNlcl9pZCI6IjY2NTI5In0.2_l9e7ohs9QHbwmr48mIoEF-QxZHNPFiAzJbMk00jcA'   Let's break down the parts of the request:      - `--request GET` - Make a GET request     - `--url` - The API endpoint URL     - `--header` - Adds the Authorization header with your API key   Handle the response  The API will return a JSON response like this:      {       \"campaign_info\": {         \"id\": \"74516\",         \"name\": \"Asos.com\",          \"company\": \"Asos\",         \"company_id\": \"51256\",         \"domain\": \"www.asos.com\",         \"keyword_count\": 588,          \"date_created\": \"2023-04-25\",         \"location\": \"United Kingdom\",         \"currency\": \"EUR\",         \"mrr\": 3000       },       \"visibility\": {         \"desktop\": {           \"latest\": 0.28,           \"trend_7days\": 0.2,           \"trend_30days\": 0.2         },         \"mobile\": {           \"latest\": 0.27,            \"trend_7days\": 0.2,           \"trend_30days\": 0.2         }       },       \"multiple_locations\": [         {           \"campaign_id\": 12746,           \"location\": \"London, United Kingdom\",           \"visibility\": {             \"desktop\": {               \"latest\": 0.32,               \"trend_7days\": 0.02               \"trend_30days: 0.1               },             \"mobile\": {               \"latest\": 0.33,               \"trend\": 0.03               \"trend_30days\": 0.1                 }             }           }         }       ],       \"health_status\": \"healthy\",       \"objective_status\": {         \"actual_sessions\": 78400,         \"estimated_sessions\": 78400,           \"performance\": 1,         \"status\": \"on_track\",         \"start_month\": \"Jun, 2023\",          \"end_month\": \"Jul, 2024\"       },       \"reporting_status\": \"submitted\",       \"account_manager\": \"Jo Hart\"     }  And that's it! You just made your first API call. Check out the rest of the API reference documentation to see what else you can build.  `Best practices`      - Keep your API key private – do not share your key publicly.     - Do not include your key directly in code that you distribute – use environment variables instead.     - Regenerate your key periodically for improved security.     - Limit API key access to only required endpoints if possible.  `Revoking API keys`  If your API key is compromised, you can revoke it by regenerating the API Token in your SEOmonitor Account Settings. This will immediately invalidate the current key so further requests can't be made.  For any other issues with authentication, contact our support team.   `Retrieve the IDs of the company, campaigns, keywords and keyword groups`  The unique IDs of your company, campaigns, keywords, or keyword groups can be retrieved either from the specific URLs of the platform, or from specific API endpoint responses. Further below you'll find details on these alternatives.   `Company ID`  The company ID can only be retrieved from the platform. Follow these steps:      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Go to Account Settings > Billing     3. In the Billing section, the platform URL contains the company ID.     E.g.: \"app.seomonitor.com/v2/account/company/51244/billing\" – in this example, the company ID is \"51244\"   `Campaign ID`  To retrieve the campaign ID from the platform, follow these steps:       1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign by clicking on its name in the Agency Dashboard.     3. By default, the campaign opens in the Rank Tracker view. The platform URL contains the company ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/0/desktop/keywords?timeframe=2023-09-04%3A2023-10-04\" – in this example, the campaign ID is \"72416\".  To retrieve the campaign ID through the API, make a call through the `Get Tracked Campaigns Details endpoint`. The response will contain the details of the requested Tracked Campaigns, including their IDs, which you can further use in other endpoint requests.   `Keyword ID`  To retrieve the keyword ID from the platform, follow these steps:       1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and click on the required keyword.     3. The platform URL for the keyword view (Keyword Sidebar) contains the keyword ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/0/desktop/keywords?timeframe=2023-09-04%3A2023-10-04&ksid=7063139\" – in this example, the keyword ID is \"7063139\"   To retrieve the keyword ID through the API, make a call through the `Get Keyword Data endpoint`. The response will contain the details of the requested keywords, including their IDs, which you can further use in other endpoint requests.   `Keyword Group ID`      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and click on the required keyword group (Groups side-menu).     3. The platform URL for the keyword group view contains the keyword ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/69976/desktop/keywords?timeframe=2023-09-04%3A2023-10-04\" – in this example, the keyword group ID is \"69976\"  To retrieve the keyword group ID through the API, make a call through the `Get Groups List endpoint`. The response will contain the details of the requested keyword groups, including their IDs, which you can further use in other endpoint requests.   `Forecast ID for Scenarios or Objectives`      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and go to Forecast from the main menu (top).     3. Select a Scenario or the Objective (if set). The platform URL for the specific scenario contains the forecast ID.     E.g.: \"https://app.seomonitor.com/v2/forecast/118794/3788\" – in this example, the forecast ID is \"3788\"   To retrieve the forecast ID through the API, make a call through the`Get Forecast Scenarios endpoint`. The response will contain the details of the requested Scenario or Objective, including their IDs, which you can further use in other endpoint requests.   `SERP Feature Abbreviations`  The returned data for some endpoints will contain SERP feature names in abbreviated form.  The returned values for SERP features are abbreviated as follows:      - \"adt\": Ads Pack Top     - \"def\": Definitions      - \"dir\": Directions      - \"fsn\": Featured Snippet      - \"flt\": Flights      - \"htl\": Hotels      - \"img\": Images Pack      - \"job\": Jobs      - \"kng\": Knowledge Graph      - \"geo\": Local Pack      - \"shp\": Product listing      - \"rcp\": Recipes      - \"qns\": Questions      - \"new\": Top Stories      - \"vid\": Video Carousel      - \"app\": Apps    `Rate Limits`  There are request limits in place to prevent abuse and ensure fair usage.   Exceeding the request limits will lead to HTTP 429 responses. If you need higher limits, contact our support team.   `Limits & Quotas`      -------------------------------------------------------------------------     |Limit                                    |  Number of requests              -------------------------------------------------------------------------     |Maximum requests per second              |  10                              -------------------------------------------------------------------------     |Maximum rows per request (Request Quota) |  1000                            -------------------------------------------------------------------------     |Daily Quota                              |  10 000                          -------------------------------------------------------------------------   `Exceeding Limits`  If you exceed the rate limits, you will receive a 429 Too Many Requests response.  Daily Quota Exceeded      {       \"error\": {         \"message\": \"Daily quota exceeded\",         \"details\": [           \"You have exceeded the allowed daily requests\"          ]       }     }  Details:  This error message indicates that the request exceeds the rate limits for daily requests. Retry the request after some delay.  Rate Limit Exceeded      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }  Details:  This error message indicates that the request exceeds the rate limits for requests per second. Retry the request after some delay.   `Increasing Limits`  The default limits allow most normal API usage patterns. However, if you need higher limits, please contact our support team.    Provide details on:      - Your specific use case      - The endpoints you are using     - The increased limits you are looking for  We will review your request and adjust limits where appropriate   `Need Higher Limits?`  For most use cases, the default limits are sufficient. But if you require higher limits, please contact our support team. We will review your use case and adjust limits where appropriate.   `Errors`  SEOmonitor API uses standard HTTP response codes to indicate the success or failure of API requests.   HTTP Status Codes      ----------------------------------------------------------------------------------     | Code  | Description                                                                 ----------------------------------------------------------------------------------     | 200   | Success                                                                     ----------------------------------------------------------------------------------     | 400   | Bad request - the request was malformed or missing required parameters      ----------------------------------------------------------------------------------      | 401   | Unauthorized - invalid or missing API key                                   ----------------------------------------------------------------------------------     | 403   | Forbidden - API key does not have access to the requested resource          ----------------------------------------------------------------------------------     | 404   | Not found - the requested resource does not exist                           ----------------------------------------------------------------------------------     | 429   | Too many requests - rate or quota limit exceeded                            ----------------------------------------------------------------------------------     | 500   | Internal server error - an unexpected error on the API server               ----------------------------------------------------------------------------------     | 50x   | Errors specific to various endpoints                                        ----------------------------------------------------------------------------------   `Error Response Format`  Error responses will be returned in JSON format:      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }   The error object contains:  - `message` - A general error message   - `details` - More specific details about the error   `Common Errors`  401 Unauthorized      {       \"error\": {         \"message\": \"Invalid authentication\",         \"details\": [           \"The API key provided is invalid\"          ]       }     }   Details:   This error message indicates there is a problem with the API key:  - The API key is missing from the request  - The key is invalid or incorrect  - The key is expired or revoked   Check that you are sending the correct API key in the Authorization header.  403 Forbidden      {       \"error\": {         \"message\": \"Forbidden access\",         \"details\": [           \"Your API key does not have access to the requested data\"          ]       }     }  Details:  This error message indicates that the API key being used does not have access to perform the requested operation. Ensure the key has the required scopes enabled.   404 Not Found      {       \"error\": {         \"message\": \"Data not found\",         \"details\": [           \"The requested data does not exist.\"          ]       }     }   Details:  This error message indicates that the object specified by the request does not exist. For example, requesting a keyword that is not in your SEOmonitor account.   429 Too Many Requests   Daily Quota Exceeded      {       \"error\": {         \"message\": \"Daily quota exceeded\",         \"details\": [           \"You have exceeded the allowed daily requests\"          ]       }     }   Details:  This error message indicates that the request exceeds the rate limits for daily requests. Retry the request after some delay.   Rate Limit Exceeded      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }   Details:  This error message indicates that the request exceeds the rate limits for requests per second. Retry the request after some delay.   500 Internal Server Error       {       \"error\": {         \"message\": \"Internal server error\",         \"details\": [           \"The server encountered an error while processing your requests\"          ]       }     }   Details:  This error message indicates that an unexpected error occurred on the API server. Try the request again later. If the issue persists, contact support.   50X Endpoint-specific errors  You may encounter errors on specific endpoint requests – these are listed and explained under each endpoint page.   Support  If you have any questions about API errors, please contact our support team.   `Changelog`  Version 3.0 (current)   Release Date: ?  This is the first version of the API 3.0.    # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: customer.success@seomonitor.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class KeywordDetail(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'keyword_id': 'int',
        'keyword': 'str',
        'main_keyword_id': 'int',
        'search_intent': 'str',
        'labels': 'str',
        'groups': 'str',
        'serp_data': 'KeywordSerpData',
        'search_data': 'SearchData',
        'ranking_data': 'KeywordRankingData',
        'landing_pages': 'KeywordLandingPages',
        'traffic_data': 'KeywordTrafficData',
        'opportunity': 'Opportunity'
    }

    attribute_map = {
        'keyword_id': 'keyword_id',
        'keyword': 'keyword',
        'main_keyword_id': 'main_keyword_id',
        'search_intent': 'search_intent',
        'labels': 'labels',
        'groups': 'groups',
        'serp_data': 'serp_data',
        'search_data': 'search_data',
        'ranking_data': 'ranking_data',
        'landing_pages': 'landing_pages',
        'traffic_data': 'traffic_data',
        'opportunity': 'opportunity'
    }

    def __init__(self, keyword_id=None, keyword=None, main_keyword_id=None, search_intent=None, labels=None, groups=None, serp_data=None, search_data=None, ranking_data=None, landing_pages=None, traffic_data=None, opportunity=None):  # noqa: E501
        """KeywordDetail - a model defined in Swagger"""  # noqa: E501
        self._keyword_id = None
        self._keyword = None
        self._main_keyword_id = None
        self._search_intent = None
        self._labels = None
        self._groups = None
        self._serp_data = None
        self._search_data = None
        self._ranking_data = None
        self._landing_pages = None
        self._traffic_data = None
        self._opportunity = None
        self.discriminator = None
        if keyword_id is not None:
            self.keyword_id = keyword_id
        if keyword is not None:
            self.keyword = keyword
        if main_keyword_id is not None:
            self.main_keyword_id = main_keyword_id
        if search_intent is not None:
            self.search_intent = search_intent
        if labels is not None:
            self.labels = labels
        if groups is not None:
            self.groups = groups
        if serp_data is not None:
            self.serp_data = serp_data
        if search_data is not None:
            self.search_data = search_data
        if ranking_data is not None:
            self.ranking_data = ranking_data
        if landing_pages is not None:
            self.landing_pages = landing_pages
        if traffic_data is not None:
            self.traffic_data = traffic_data
        if opportunity is not None:
            self.opportunity = opportunity

    @property
    def keyword_id(self):
        """Gets the keyword_id of this KeywordDetail.  # noqa: E501

        The unique ID used to identify and reference the keyword in the system. It can be stored and used in other endpoints for filtering.  # noqa: E501

        :return: The keyword_id of this KeywordDetail.  # noqa: E501
        :rtype: int
        """
        return self._keyword_id

    @keyword_id.setter
    def keyword_id(self, keyword_id):
        """Sets the keyword_id of this KeywordDetail.

        The unique ID used to identify and reference the keyword in the system. It can be stored and used in other endpoints for filtering.  # noqa: E501

        :param keyword_id: The keyword_id of this KeywordDetail.  # noqa: E501
        :type: int
        """

        self._keyword_id = keyword_id

    @property
    def keyword(self):
        """Gets the keyword of this KeywordDetail.  # noqa: E501

        The exact keyword phrase.  # noqa: E501

        :return: The keyword of this KeywordDetail.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this KeywordDetail.

        The exact keyword phrase.  # noqa: E501

        :param keyword: The keyword of this KeywordDetail.  # noqa: E501
        :type: int
        """

        self._keyword = keyword

    @property
    def main_keyword_id(self):
        """Gets the main_keyword_id of this KeywordDetail.  # noqa: E501

        The ID of the main keyword, if the current keyword is aggregated under another keyword as its close variation.  # noqa: E501

        :return: The main_keyword_id of this KeywordDetail.  # noqa: E501
        :rtype: str
        """
        return self._main_keyword_id

    @main_keyword_id.setter
    def main_keyword_id(self, main_keyword_id):
        """Sets the main_keyword_id of this KeywordDetail.

        The ID of the main keyword, if the current keyword is aggregated under another keyword as its close variation.  # noqa: E501

        :param main_keyword_id: The main_keyword_id of this KeywordDetail.  # noqa: E501
        :type: str
        """

        self._main_keyword_id = main_keyword_id

    @property
    def search_intent(self):
        """Gets the search_intent of this KeywordDetail.  # noqa: E501

        The search intent of the keyword.  Possible values: `informational`, `commercial`, or `transactional`.  # noqa: E501

        :return: The search_intent of this KeywordDetail.  # noqa: E501
        :rtype: str
        """
        return self._search_intent

    @search_intent.setter
    def search_intent(self, search_intent):
        """Sets the search_intent of this KeywordDetail.

        The search intent of the keyword.  Possible values: `informational`, `commercial`, or `transactional`.  # noqa: E501

        :param search_intent: The search_intent of this KeywordDetail.  # noqa: E501
        :type: str
        """

        self._search_intent = search_intent

    @property
    def labels(self):
        """Gets the labels of this KeywordDetail.  # noqa: E501

        The label associated with the keyword, either manually or automatically applied, that indicate specific attributes or characteristics of a keyword.  Possible values: automatic labels: `misspelled`, `low relevance`, `brands`, `localized`. for keywords labeled as `seasonal` in the platform, the endpoint will return one of the following possible values: `in_full_season`, `out_of_season`, `season_approaching`. custom labels: User-defined label name.   # noqa: E501

        :return: The labels of this KeywordDetail.  # noqa: E501
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this KeywordDetail.

        The label associated with the keyword, either manually or automatically applied, that indicate specific attributes or characteristics of a keyword.  Possible values: automatic labels: `misspelled`, `low relevance`, `brands`, `localized`. for keywords labeled as `seasonal` in the platform, the endpoint will return one of the following possible values: `in_full_season`, `out_of_season`, `season_approaching`. custom labels: User-defined label name.   # noqa: E501

        :param labels: The labels of this KeywordDetail.  # noqa: E501
        :type: str
        """

        self._labels = labels

    @property
    def groups(self):
        """Gets the groups of this KeywordDetail.  # noqa: E501

        The group_ids of the groups this keyword is included in.  # noqa: E501

        :return: The groups of this KeywordDetail.  # noqa: E501
        :rtype: str
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this KeywordDetail.

        The group_ids of the groups this keyword is included in.  # noqa: E501

        :param groups: The groups of this KeywordDetail.  # noqa: E501
        :type: str
        """

        self._groups = groups

    @property
    def serp_data(self):
        """Gets the serp_data of this KeywordDetail.  # noqa: E501


        :return: The serp_data of this KeywordDetail.  # noqa: E501
        :rtype: KeywordSerpData
        """
        return self._serp_data

    @serp_data.setter
    def serp_data(self, serp_data):
        """Sets the serp_data of this KeywordDetail.


        :param serp_data: The serp_data of this KeywordDetail.  # noqa: E501
        :type: KeywordSerpData
        """

        self._serp_data = serp_data

    @property
    def search_data(self):
        """Gets the search_data of this KeywordDetail.  # noqa: E501


        :return: The search_data of this KeywordDetail.  # noqa: E501
        :rtype: SearchData
        """
        return self._search_data

    @search_data.setter
    def search_data(self, search_data):
        """Sets the search_data of this KeywordDetail.


        :param search_data: The search_data of this KeywordDetail.  # noqa: E501
        :type: SearchData
        """

        self._search_data = search_data

    @property
    def ranking_data(self):
        """Gets the ranking_data of this KeywordDetail.  # noqa: E501


        :return: The ranking_data of this KeywordDetail.  # noqa: E501
        :rtype: KeywordRankingData
        """
        return self._ranking_data

    @ranking_data.setter
    def ranking_data(self, ranking_data):
        """Sets the ranking_data of this KeywordDetail.


        :param ranking_data: The ranking_data of this KeywordDetail.  # noqa: E501
        :type: KeywordRankingData
        """

        self._ranking_data = ranking_data

    @property
    def landing_pages(self):
        """Gets the landing_pages of this KeywordDetail.  # noqa: E501


        :return: The landing_pages of this KeywordDetail.  # noqa: E501
        :rtype: KeywordLandingPages
        """
        return self._landing_pages

    @landing_pages.setter
    def landing_pages(self, landing_pages):
        """Sets the landing_pages of this KeywordDetail.


        :param landing_pages: The landing_pages of this KeywordDetail.  # noqa: E501
        :type: KeywordLandingPages
        """

        self._landing_pages = landing_pages

    @property
    def traffic_data(self):
        """Gets the traffic_data of this KeywordDetail.  # noqa: E501


        :return: The traffic_data of this KeywordDetail.  # noqa: E501
        :rtype: KeywordTrafficData
        """
        return self._traffic_data

    @traffic_data.setter
    def traffic_data(self, traffic_data):
        """Sets the traffic_data of this KeywordDetail.


        :param traffic_data: The traffic_data of this KeywordDetail.  # noqa: E501
        :type: KeywordTrafficData
        """

        self._traffic_data = traffic_data

    @property
    def opportunity(self):
        """Gets the opportunity of this KeywordDetail.  # noqa: E501


        :return: The opportunity of this KeywordDetail.  # noqa: E501
        :rtype: Opportunity
        """
        return self._opportunity

    @opportunity.setter
    def opportunity(self, opportunity):
        """Sets the opportunity of this KeywordDetail.


        :param opportunity: The opportunity of this KeywordDetail.  # noqa: E501
        :type: Opportunity
        """

        self._opportunity = opportunity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(KeywordDetail, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KeywordDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
