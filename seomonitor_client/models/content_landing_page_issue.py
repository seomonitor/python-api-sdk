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

class ContentLandingPageIssue(object):
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
        'issue_id': 'int',
        'url': 'str',
        'type': 'str',
        'keywords': 'list[int]',
        'average_ctr': 'float',
        'search_volume': 'int',
        'year_over_year': 'float',
        'visibility_score': 'int',
        'visibility_score_change': 'int',
        'difficulty': 'DifficultyValue',
        'opportunity_score': 'int'
    }

    attribute_map = {
        'issue_id': 'issue_id',
        'url': 'url',
        'type': 'type',
        'keywords': 'keywords',
        'average_ctr': 'average_ctr',
        'search_volume': 'search_volume',
        'year_over_year': 'year_over_year',
        'visibility_score': 'visibility_score',
        'visibility_score_change': 'visibility_score_change',
        'difficulty': 'difficulty',
        'opportunity_score': 'opportunity_score'
    }

    def __init__(self, issue_id=None, url=None, type=None, keywords=None, average_ctr=None, search_volume=None, year_over_year=None, visibility_score=None, visibility_score_change=None, difficulty=None, opportunity_score=None):  # noqa: E501
        """ContentLandingPageIssue - a model defined in Swagger"""  # noqa: E501
        self._issue_id = None
        self._url = None
        self._type = None
        self._keywords = None
        self._average_ctr = None
        self._search_volume = None
        self._year_over_year = None
        self._visibility_score = None
        self._visibility_score_change = None
        self._difficulty = None
        self._opportunity_score = None
        self.discriminator = None
        if issue_id is not None:
            self.issue_id = issue_id
        if url is not None:
            self.url = url
        if type is not None:
            self.type = type
        if keywords is not None:
            self.keywords = keywords
        if average_ctr is not None:
            self.average_ctr = average_ctr
        if search_volume is not None:
            self.search_volume = search_volume
        if year_over_year is not None:
            self.year_over_year = year_over_year
        if visibility_score is not None:
            self.visibility_score = visibility_score
        if visibility_score_change is not None:
            self.visibility_score_change = visibility_score_change
        if difficulty is not None:
            self.difficulty = difficulty
        if opportunity_score is not None:
            self.opportunity_score = opportunity_score

    @property
    def issue_id(self):
        """Gets the issue_id of this ContentLandingPageIssue.  # noqa: E501

        Internal ID for this issue.  # noqa: E501

        :return: The issue_id of this ContentLandingPageIssue.  # noqa: E501
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this ContentLandingPageIssue.

        Internal ID for this issue.  # noqa: E501

        :param issue_id: The issue_id of this ContentLandingPageIssue.  # noqa: E501
        :type: int
        """

        self._issue_id = issue_id

    @property
    def url(self):
        """Gets the url of this ContentLandingPageIssue.  # noqa: E501

        URL of the landing page  # noqa: E501

        :return: The url of this ContentLandingPageIssue.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ContentLandingPageIssue.

        URL of the landing page  # noqa: E501

        :param url: The url of this ContentLandingPageIssue.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def type(self):
        """Gets the type of this ContentLandingPageIssue.  # noqa: E501

        The type of the issue reported. Available values are: missing_title => Pages with missing title or h1; suboptimal_title_inclusion => Pages with suboptimal keyword inclusion in the title or h1; suboptimal_content_inclusion => Pages with suboptimal keyword inclusion in the content; pages_with_many_keywords => Pages considered to be serving too many keywords; visibility_increase => Pages with an increase in the visibility metric that can be correlated with a content change; visibility_drop => Pages with a drop in the visibility metric that can be correlated with a content change;  # noqa: E501

        :return: The type of this ContentLandingPageIssue.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ContentLandingPageIssue.

        The type of the issue reported. Available values are: missing_title => Pages with missing title or h1; suboptimal_title_inclusion => Pages with suboptimal keyword inclusion in the title or h1; suboptimal_content_inclusion => Pages with suboptimal keyword inclusion in the content; pages_with_many_keywords => Pages considered to be serving too many keywords; visibility_increase => Pages with an increase in the visibility metric that can be correlated with a content change; visibility_drop => Pages with a drop in the visibility metric that can be correlated with a content change;  # noqa: E501

        :param type: The type of this ContentLandingPageIssue.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def keywords(self):
        """Gets the keywords of this ContentLandingPageIssue.  # noqa: E501

        Array of keyword IDs of the keywords which rank for this landing page.  # noqa: E501

        :return: The keywords of this ContentLandingPageIssue.  # noqa: E501
        :rtype: list[int]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this ContentLandingPageIssue.

        Array of keyword IDs of the keywords which rank for this landing page.  # noqa: E501

        :param keywords: The keywords of this ContentLandingPageIssue.  # noqa: E501
        :type: list[int]
        """

        self._keywords = keywords

    @property
    def average_ctr(self):
        """Gets the average_ctr of this ContentLandingPageIssue.  # noqa: E501

        The percentage of the search volume that ends up by clicking on the organic results. This is calculated for every keyword for their unique mix of SERP features. For a landing page, this is calculated by taking into account the CTR of every keyword it ranks for and the potential search volume of that particular keyword.  # noqa: E501

        :return: The average_ctr of this ContentLandingPageIssue.  # noqa: E501
        :rtype: float
        """
        return self._average_ctr

    @average_ctr.setter
    def average_ctr(self, average_ctr):
        """Sets the average_ctr of this ContentLandingPageIssue.

        The percentage of the search volume that ends up by clicking on the organic results. This is calculated for every keyword for their unique mix of SERP features. For a landing page, this is calculated by taking into account the CTR of every keyword it ranks for and the potential search volume of that particular keyword.  # noqa: E501

        :param average_ctr: The average_ctr of this ContentLandingPageIssue.  # noqa: E501
        :type: float
        """

        self._average_ctr = average_ctr

    @property
    def search_volume(self):
        """Gets the search_volume of this ContentLandingPageIssue.  # noqa: E501

        The sum of the average search volume as an integer as provided by Google Ads for the keywords ranking for this landing page.  # noqa: E501

        :return: The search_volume of this ContentLandingPageIssue.  # noqa: E501
        :rtype: int
        """
        return self._search_volume

    @search_volume.setter
    def search_volume(self, search_volume):
        """Sets the search_volume of this ContentLandingPageIssue.

        The sum of the average search volume as an integer as provided by Google Ads for the keywords ranking for this landing page.  # noqa: E501

        :param search_volume: The search_volume of this ContentLandingPageIssue.  # noqa: E501
        :type: int
        """

        self._search_volume = search_volume

    @property
    def year_over_year(self):
        """Gets the year_over_year of this ContentLandingPageIssue.  # noqa: E501

        The Year-over-Year search trend as a positive or negative percentage calculated as last month Search Volume compared to one year ago, as provided by Google Ads.  # noqa: E501

        :return: The year_over_year of this ContentLandingPageIssue.  # noqa: E501
        :rtype: float
        """
        return self._year_over_year

    @year_over_year.setter
    def year_over_year(self, year_over_year):
        """Sets the year_over_year of this ContentLandingPageIssue.

        The Year-over-Year search trend as a positive or negative percentage calculated as last month Search Volume compared to one year ago, as provided by Google Ads.  # noqa: E501

        :param year_over_year: The year_over_year of this ContentLandingPageIssue.  # noqa: E501
        :type: float
        """

        self._year_over_year = year_over_year

    @property
    def visibility_score(self):
        """Gets the visibility_score of this ContentLandingPageIssue.  # noqa: E501

        The visibility score of the landing page as a percentage calculated by taking into account the ranks and the search volumes of the keywords the landing page ranks for. For more detalils on visibility metric: https://help.seomonitor.com/en/articles/6344566-reliable-visibility-metric  # noqa: E501

        :return: The visibility_score of this ContentLandingPageIssue.  # noqa: E501
        :rtype: int
        """
        return self._visibility_score

    @visibility_score.setter
    def visibility_score(self, visibility_score):
        """Sets the visibility_score of this ContentLandingPageIssue.

        The visibility score of the landing page as a percentage calculated by taking into account the ranks and the search volumes of the keywords the landing page ranks for. For more detalils on visibility metric: https://help.seomonitor.com/en/articles/6344566-reliable-visibility-metric  # noqa: E501

        :param visibility_score: The visibility_score of this ContentLandingPageIssue.  # noqa: E501
        :type: int
        """

        self._visibility_score = visibility_score

    @property
    def visibility_score_change(self):
        """Gets the visibility_score_change of this ContentLandingPageIssue.  # noqa: E501

        The visibility score change for the past 30 days as a positive or negative percentage. For more information on the visibility trend: https://help.seomonitor.com/en/articles/6344738-visibility-trend-explainer  # noqa: E501

        :return: The visibility_score_change of this ContentLandingPageIssue.  # noqa: E501
        :rtype: int
        """
        return self._visibility_score_change

    @visibility_score_change.setter
    def visibility_score_change(self, visibility_score_change):
        """Sets the visibility_score_change of this ContentLandingPageIssue.

        The visibility score change for the past 30 days as a positive or negative percentage. For more information on the visibility trend: https://help.seomonitor.com/en/articles/6344738-visibility-trend-explainer  # noqa: E501

        :param visibility_score_change: The visibility_score_change of this ContentLandingPageIssue.  # noqa: E501
        :type: int
        """

        self._visibility_score_change = visibility_score_change

    @property
    def difficulty(self):
        """Gets the difficulty of this ContentLandingPageIssue.  # noqa: E501


        :return: The difficulty of this ContentLandingPageIssue.  # noqa: E501
        :rtype: DifficultyValue
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        """Sets the difficulty of this ContentLandingPageIssue.


        :param difficulty: The difficulty of this ContentLandingPageIssue.  # noqa: E501
        :type: DifficultyValue
        """

        self._difficulty = difficulty

    @property
    def opportunity_score(self):
        """Gets the opportunity_score of this ContentLandingPageIssue.  # noqa: E501

        The opportunity score of this particular landing page. This indicates on a scale of 1 to 10 the potential benefits of optimizing this landing page to rank in top 3 for it's keywords as compared to the difficulty of reaching that milestone. For more information about keywords and groups of keywords opportunity score: https://help.seomonitor.com/en/articles/6222130-seo-opportunity  # noqa: E501

        :return: The opportunity_score of this ContentLandingPageIssue.  # noqa: E501
        :rtype: int
        """
        return self._opportunity_score

    @opportunity_score.setter
    def opportunity_score(self, opportunity_score):
        """Sets the opportunity_score of this ContentLandingPageIssue.

        The opportunity score of this particular landing page. This indicates on a scale of 1 to 10 the potential benefits of optimizing this landing page to rank in top 3 for it's keywords as compared to the difficulty of reaching that milestone. For more information about keywords and groups of keywords opportunity score: https://help.seomonitor.com/en/articles/6222130-seo-opportunity  # noqa: E501

        :param opportunity_score: The opportunity_score of this ContentLandingPageIssue.  # noqa: E501
        :type: int
        """

        self._opportunity_score = opportunity_score

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
        if issubclass(ContentLandingPageIssue, dict):
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
        if not isinstance(other, ContentLandingPageIssue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
