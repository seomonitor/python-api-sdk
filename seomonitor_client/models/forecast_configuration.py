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

class ForecastConfiguration(object):
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
        'timeframe': 'str',
        'start_month': 'str',
        'extended_forecast': 'bool',
        'target_rank_range': 'bool',
        'progression_speed': 'str',
        'use_year_over_year': 'bool',
        'use_search_volume_by_device': 'bool',
        'use_long_tail_effect': 'bool',
        'use_percentage_clicks': 'bool',
        'conversion_data': 'ForecastConfigConversionData'
    }

    attribute_map = {
        'timeframe': 'timeframe',
        'start_month': 'start_month',
        'extended_forecast': 'extended_forecast',
        'target_rank_range': 'target_rank_range',
        'progression_speed': 'progression_speed',
        'use_year_over_year': 'use_year_over_year',
        'use_search_volume_by_device': 'use_search_volume_by_device',
        'use_long_tail_effect': 'use_long_tail_effect',
        'use_percentage_clicks': 'use_percentage_clicks',
        'conversion_data': 'conversion_data'
    }

    def __init__(self, timeframe=None, start_month=None, extended_forecast=None, target_rank_range=None, progression_speed=None, use_year_over_year=None, use_search_volume_by_device=None, use_long_tail_effect=None, use_percentage_clicks=None, conversion_data=None):  # noqa: E501
        """ForecastConfiguration - a model defined in Swagger"""  # noqa: E501
        self._timeframe = None
        self._start_month = None
        self._extended_forecast = None
        self._target_rank_range = None
        self._progression_speed = None
        self._use_year_over_year = None
        self._use_search_volume_by_device = None
        self._use_long_tail_effect = None
        self._use_percentage_clicks = None
        self._conversion_data = None
        self.discriminator = None
        if timeframe is not None:
            self.timeframe = timeframe
        if start_month is not None:
            self.start_month = start_month
        if extended_forecast is not None:
            self.extended_forecast = extended_forecast
        if target_rank_range is not None:
            self.target_rank_range = target_rank_range
        if progression_speed is not None:
            self.progression_speed = progression_speed
        if use_year_over_year is not None:
            self.use_year_over_year = use_year_over_year
        if use_search_volume_by_device is not None:
            self.use_search_volume_by_device = use_search_volume_by_device
        if use_long_tail_effect is not None:
            self.use_long_tail_effect = use_long_tail_effect
        if use_percentage_clicks is not None:
            self.use_percentage_clicks = use_percentage_clicks
        if conversion_data is not None:
            self.conversion_data = conversion_data

    @property
    def timeframe(self):
        """Gets the timeframe of this ForecastConfiguration.  # noqa: E501

        The duration of the scenario in months.  # noqa: E501

        :return: The timeframe of this ForecastConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._timeframe

    @timeframe.setter
    def timeframe(self, timeframe):
        """Sets the timeframe of this ForecastConfiguration.

        The duration of the scenario in months.  # noqa: E501

        :param timeframe: The timeframe of this ForecastConfiguration.  # noqa: E501
        :type: str
        """

        self._timeframe = timeframe

    @property
    def start_month(self):
        """Gets the start_month of this ForecastConfiguration.  # noqa: E501

        The month and year when the scenario was set to start.  # noqa: E501

        :return: The start_month of this ForecastConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._start_month

    @start_month.setter
    def start_month(self, start_month):
        """Sets the start_month of this ForecastConfiguration.

        The month and year when the scenario was set to start.  # noqa: E501

        :param start_month: The start_month of this ForecastConfiguration.  # noqa: E501
        :type: str
        """

        self._start_month = start_month

    @property
    def extended_forecast(self):
        """Gets the extended_forecast of this ForecastConfiguration.  # noqa: E501

        Whether the projection includes the extended forecast timeframe and the results estimated for it.  # noqa: E501

        :return: The extended_forecast of this ForecastConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._extended_forecast

    @extended_forecast.setter
    def extended_forecast(self, extended_forecast):
        """Sets the extended_forecast of this ForecastConfiguration.

        Whether the projection includes the extended forecast timeframe and the results estimated for it.  # noqa: E501

        :param extended_forecast: The extended_forecast of this ForecastConfiguration.  # noqa: E501
        :type: bool
        """

        self._extended_forecast = extended_forecast

    @property
    def target_rank_range(self):
        """Gets the target_rank_range of this ForecastConfiguration.  # noqa: E501

        Whether the target rank range option is enabled for the Objective. If 'true', the estimated results of the forecast will be returned for both the lower (worst) and the higher (best) target.  # noqa: E501

        :return: The target_rank_range of this ForecastConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._target_rank_range

    @target_rank_range.setter
    def target_rank_range(self, target_rank_range):
        """Sets the target_rank_range of this ForecastConfiguration.

        Whether the target rank range option is enabled for the Objective. If 'true', the estimated results of the forecast will be returned for both the lower (worst) and the higher (best) target.  # noqa: E501

        :param target_rank_range: The target_rank_range of this ForecastConfiguration.  # noqa: E501
        :type: bool
        """

        self._target_rank_range = target_rank_range

    @property
    def progression_speed(self):
        """Gets the progression_speed of this ForecastConfiguration.  # noqa: E501

        The user-configured speed at which the average selected target rank will be reached.  Possible values are `conservative`, `mostly conservative`, `moderate`, `mostly moderate`, `optimistic`, `mostly optimistic`, and `custom`.  # noqa: E501

        :return: The progression_speed of this ForecastConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._progression_speed

    @progression_speed.setter
    def progression_speed(self, progression_speed):
        """Sets the progression_speed of this ForecastConfiguration.

        The user-configured speed at which the average selected target rank will be reached.  Possible values are `conservative`, `mostly conservative`, `moderate`, `mostly moderate`, `optimistic`, `mostly optimistic`, and `custom`.  # noqa: E501

        :param progression_speed: The progression_speed of this ForecastConfiguration.  # noqa: E501
        :type: str
        """

        self._progression_speed = progression_speed

    @property
    def use_year_over_year(self):
        """Gets the use_year_over_year of this ForecastConfiguration.  # noqa: E501

        Whether the option to include the Year-over-Year search trends of the keywords in the forecast calculation is enabled.  # noqa: E501

        :return: The use_year_over_year of this ForecastConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_year_over_year

    @use_year_over_year.setter
    def use_year_over_year(self, use_year_over_year):
        """Sets the use_year_over_year of this ForecastConfiguration.

        Whether the option to include the Year-over-Year search trends of the keywords in the forecast calculation is enabled.  # noqa: E501

        :param use_year_over_year: The use_year_over_year of this ForecastConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_year_over_year = use_year_over_year

    @property
    def use_search_volume_by_device(self):
        """Gets the use_search_volume_by_device of this ForecastConfiguration.  # noqa: E501

        Whether the option to include the search volume for each device of the keywords in the forecast calculation is enabled.  # noqa: E501

        :return: The use_search_volume_by_device of this ForecastConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_search_volume_by_device

    @use_search_volume_by_device.setter
    def use_search_volume_by_device(self, use_search_volume_by_device):
        """Sets the use_search_volume_by_device of this ForecastConfiguration.

        Whether the option to include the search volume for each device of the keywords in the forecast calculation is enabled.  # noqa: E501

        :param use_search_volume_by_device: The use_search_volume_by_device of this ForecastConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_search_volume_by_device = use_search_volume_by_device

    @property
    def use_long_tail_effect(self):
        """Gets the use_long_tail_effect of this ForecastConfiguration.  # noqa: E501

        Whether the option to include the estimation of additional traffic generated by other keywords semantically related to the ones included in the forecast is enabled.  # noqa: E501

        :return: The use_long_tail_effect of this ForecastConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_long_tail_effect

    @use_long_tail_effect.setter
    def use_long_tail_effect(self, use_long_tail_effect):
        """Sets the use_long_tail_effect of this ForecastConfiguration.

        Whether the option to include the estimation of additional traffic generated by other keywords semantically related to the ones included in the forecast is enabled.  # noqa: E501

        :param use_long_tail_effect: The use_long_tail_effect of this ForecastConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_long_tail_effect = use_long_tail_effect

    @property
    def use_percentage_clicks(self):
        """Gets the use_percentage_clicks of this ForecastConfiguration.  # noqa: E501

        Whether the option to include the Percentage Clicks metric in the forecast calculation is enabled.  # noqa: E501

        :return: The use_percentage_clicks of this ForecastConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_percentage_clicks

    @use_percentage_clicks.setter
    def use_percentage_clicks(self, use_percentage_clicks):
        """Sets the use_percentage_clicks of this ForecastConfiguration.

        Whether the option to include the Percentage Clicks metric in the forecast calculation is enabled.  # noqa: E501

        :param use_percentage_clicks: The use_percentage_clicks of this ForecastConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_percentage_clicks = use_percentage_clicks

    @property
    def conversion_data(self):
        """Gets the conversion_data of this ForecastConfiguration.  # noqa: E501


        :return: The conversion_data of this ForecastConfiguration.  # noqa: E501
        :rtype: ForecastConfigConversionData
        """
        return self._conversion_data

    @conversion_data.setter
    def conversion_data(self, conversion_data):
        """Sets the conversion_data of this ForecastConfiguration.


        :param conversion_data: The conversion_data of this ForecastConfiguration.  # noqa: E501
        :type: ForecastConfigConversionData
        """

        self._conversion_data = conversion_data

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
        if issubclass(ForecastConfiguration, dict):
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
        if not isinstance(other, ForecastConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
