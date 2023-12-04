# swagger-client
`Introduction`  The SEOmonitor API allows you to programmatically access keyword ranking, traffic, and other SEO data from the SEOmonitor platform. You can use the API to build custom reports, automate workflows, and integrate SEOmonitor data into your own applications. The API enables free and unrestricted access to all your data in the platform, for all Tracked Campaigns. Additionally, it provides access to SEOmonitor's curated UK and US keyword database.   `Main Capabilities`  These are the main data sets you can retrieve with the API 3.0 endpoints:  `Campaign-level data`: Campaign details and campaign-wide keyword data, landing page data, groups data, traffic data, content opportunities data, forecast data, or campaign website research data.  `Keyword-level data`: Data for any and all keywords in the campaign, including ranking data, search data, SERP data, competitor data, SEO Opportunity, keyword-level traffic data, content optimization opportunities' data by keyword and keyword-level forecast projections data.  `Keyword group-level data`: Data for any keyword group in the campaign, including aggregated search and SERP data, website Visibility on specific groups, group SEO Opportunity data.  `Landing page-level data`: Data for specific landing pages that are ranking with the keywords in the campaign, including aggregated search and SERP data, SEO Opportunity, and landing page Visibility.  `Organic traffic data`: Data for the website's organic sessions, conversions, and revenue, including traffic data by segments (brand, non-brand, all traffic, and custom user-created traffic segments), by specific keywords and by specific landing pages.  `Keyword & website research data`: Data for any keyword in SEOmonitor's Research database – any domain-level aggregated search, SERP, and ranking data, and keyword-level and keyword list-level metrics, for the tracked website and for any competitor in top 100.  `Forecast data`: Overview data and details for specific Forecast Scenarios and Objectives, and keyword-level forecast data.  `Website content data`: Data related to content optimization opportunities of the tracked website, including landing page and keyword data for each of the content opportunities categories in SEOmonitor's Content Audit platform (Positive and negative correlations with Visibility, Cannibalization issues, Pages serving too many keywords, Keywords with missing pages, Suboptimal keyword inclusion in the title or H1 or page content, Pages with missing title or H1).   `Getting Started`  Log into your SEOmonitor account and retrieve your unique API Token (Account Settings > Edit Profile).  Check out the `quick start guide` to make your first API call.  Read through the `authentication guide` to learn how to properly authenticate your API requests.   `Libraries and SDKs`  SEOmonitor API uses HTTP protocol, which allows the application of our API to almost all programming languages. All the responses are returned in JSON format by default.  For convenience, we offer client libraries for popular programming languages:  JavaScript PHP Python Java   `Support`  Need help using the API, or have general inquiries? Please contact our support team.  For more information about the SEOmonitor platform, you can visit www.seomonitor.com.   `Changelog`      This is the first version of API 3.0. The Changelog page will be updated as we continue to develop new features and improvements.     `Quick Start Guide`  This guide will walk you through making your first API call.  `Get your API key`  First, you'll need to get an API key:      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Go to Account Settings > Edit Profile     3. Copy the API Token to use in your API requests  Note: Clicking `Regenerate API Token` will overwrite the current key and you will lose access if you or other users are currently using it.   `Make a request`  Next, we'll use cURL to make a request to get Tracked Campaigns details:      curl --request GET \\     --url https://apix.seomonitor.com/dashboard/v3.0/campaigns/tracked \\     --header 'Accept: application/json' \\     --header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZW9tb25pdG9yLmNvbSIsImlhdCI6MTY1Mjc4NTcwNCwidXNlcl9pZCI6IjY2NTI5In0.2_l9e7ohs9QHbwmr48mIoEF-QxZHNPFiAzJbMk00jcA'  This will retrieve the Tracked Campaigns data for an SEOmonitor account having the following API Token:      'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZW9tb25pdG9yLmNvbSIsImlhdCI6MTY1Mjc4NTcwNCwidXNlcl9pZCI6IjY2NTI5In0.2_l9e7ohs9QHbwmr48mIoEF-QxZHNPFiAzJbMk00jcA'   Let's break down the parts of the request:      - `--request GET` - Make a GET request     - `--url` - The API endpoint URL     - `--header` - Adds the Authorization header with your API key   Handle the response  The API will return a JSON response like this:      {       \"campaign_info\": {         \"id\": \"74516\",         \"name\": \"Asos.com\",          \"company\": \"Asos\",         \"company_id\": \"51256\",         \"domain\": \"www.asos.com\",         \"keyword_count\": 588,          \"date_created\": \"2023-04-25\",         \"location\": \"United Kingdom\",         \"currency\": \"EUR\",         \"mrr\": 3000       },       \"visibility\": {         \"desktop\": {           \"latest\": 0.28,           \"trend_7days\": 0.2,           \"trend_30days\": 0.2         },         \"mobile\": {           \"latest\": 0.27,            \"trend_7days\": 0.2,           \"trend_30days\": 0.2         }       },       \"multiple_locations\": [         {           \"campaign_id\": 12746,           \"location\": \"London, United Kingdom\",           \"visibility\": {             \"desktop\": {               \"latest\": 0.32,               \"trend_7days\": 0.02               \"trend_30days: 0.1               },             \"mobile\": {               \"latest\": 0.33,               \"trend\": 0.03               \"trend_30days\": 0.1                 }             }           }         }       ],       \"health_status\": \"healthy\",       \"objective_status\": {         \"actual_sessions\": 78400,         \"estimated_sessions\": 78400,           \"performance\": 1,         \"status\": \"on_track\",         \"start_month\": \"Jun, 2023\",          \"end_month\": \"Jul, 2024\"       },       \"reporting_status\": \"submitted\",       \"account_manager\": \"Jo Hart\"     }  And that's it! You just made your first API call. Check out the rest of the API reference documentation to see what else you can build.  `Best practices`      - Keep your API key private – do not share your key publicly.     - Do not include your key directly in code that you distribute – use environment variables instead.     - Regenerate your key periodically for improved security.     - Limit API key access to only required endpoints if possible.  `Revoking API keys`  If your API key is compromised, you can revoke it by regenerating the API Token in your SEOmonitor Account Settings. This will immediately invalidate the current key so further requests can't be made.  For any other issues with authentication, contact our support team.   `Retrieve the IDs of the company, campaigns, keywords and keyword groups`  The unique IDs of your company, campaigns, keywords, or keyword groups can be retrieved either from the specific URLs of the platform, or from specific API endpoint responses. Further below you'll find details on these alternatives.   `Company ID`  The company ID can only be retrieved from the platform. Follow these steps:      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Go to Account Settings > Billing     3. In the Billing section, the platform URL contains the company ID.     E.g.: \"app.seomonitor.com/v2/account/company/51244/billing\" – in this example, the company ID is \"51244\"   `Campaign ID`  To retrieve the campaign ID from the platform, follow these steps:       1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign by clicking on its name in the Agency Dashboard.     3. By default, the campaign opens in the Rank Tracker view. The platform URL contains the company ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/0/desktop/keywords?timeframe=2023-09-04%3A2023-10-04\" – in this example, the campaign ID is \"72416\".  To retrieve the campaign ID through the API, make a call through the `Get Tracked Campaigns Details endpoint`. The response will contain the details of the requested Tracked Campaigns, including their IDs, which you can further use in other endpoint requests.   `Keyword ID`  To retrieve the keyword ID from the platform, follow these steps:       1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and click on the required keyword.     3. The platform URL for the keyword view (Keyword Sidebar) contains the keyword ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/0/desktop/keywords?timeframe=2023-09-04%3A2023-10-04&ksid=7063139\" – in this example, the keyword ID is \"7063139\"   To retrieve the keyword ID through the API, make a call through the `Get Keyword Data endpoint`. The response will contain the details of the requested keywords, including their IDs, which you can further use in other endpoint requests.   `Keyword Group ID`      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and click on the required keyword group (Groups side-menu).     3. The platform URL for the keyword group view contains the keyword ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/69976/desktop/keywords?timeframe=2023-09-04%3A2023-10-04\" – in this example, the keyword group ID is \"69976\"  To retrieve the keyword group ID through the API, make a call through the `Get Groups List endpoint`. The response will contain the details of the requested keyword groups, including their IDs, which you can further use in other endpoint requests.   `Forecast ID for Scenarios or Objectives`      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and go to Forecast from the main menu (top).     3. Select a Scenario or the Objective (if set). The platform URL for the specific scenario contains the forecast ID.     E.g.: \"https://app.seomonitor.com/v2/forecast/118794/3788\" – in this example, the forecast ID is \"3788\"   To retrieve the forecast ID through the API, make a call through the`Get Forecast Scenarios endpoint`. The response will contain the details of the requested Scenario or Objective, including their IDs, which you can further use in other endpoint requests.   `SERP Feature Abbreviations`  The returned data for some endpoints will contain SERP feature names in abbreviated form.  The returned values for SERP features are abbreviated as follows:      - \"adt\": Ads Pack Top     - \"def\": Definitions      - \"dir\": Directions      - \"fsn\": Featured Snippet      - \"flt\": Flights      - \"htl\": Hotels      - \"img\": Images Pack      - \"job\": Jobs      - \"kng\": Knowledge Graph      - \"geo\": Local Pack      - \"shp\": Product listing      - \"rcp\": Recipes      - \"qns\": Questions      - \"new\": Top Stories      - \"vid\": Video Carousel      - \"app\": Apps    `Rate Limits`  There are request limits in place to prevent abuse and ensure fair usage.   Exceeding the request limits will lead to HTTP 429 responses. If you need higher limits, contact our support team.   `Limits & Quotas`      -------------------------------------------------------------------------     |Limit                                    |  Number of requests              -------------------------------------------------------------------------     |Maximum requests per second              |  10                              -------------------------------------------------------------------------     |Maximum rows per request (Request Quota) |  1000                            -------------------------------------------------------------------------     |Daily Quota                              |  10 000                          -------------------------------------------------------------------------   `Exceeding Limits`  If you exceed the rate limits, you will receive a 429 Too Many Requests response.  Daily Quota Exceeded      {       \"error\": {         \"message\": \"Daily quota exceeded\",         \"details\": [           \"You have exceeded the allowed daily requests\"          ]       }     }  Details:  This error message indicates that the request exceeds the rate limits for daily requests. Retry the request after some delay.  Rate Limit Exceeded      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }  Details:  This error message indicates that the request exceeds the rate limits for requests per second. Retry the request after some delay.   `Increasing Limits`  The default limits allow most normal API usage patterns. However, if you need higher limits, please contact our support team.    Provide details on:      - Your specific use case      - The endpoints you are using     - The increased limits you are looking for  We will review your request and adjust limits where appropriate   `Need Higher Limits?`  For most use cases, the default limits are sufficient. But if you require higher limits, please contact our support team. We will review your use case and adjust limits where appropriate.   `Errors`  SEOmonitor API uses standard HTTP response codes to indicate the success or failure of API requests.   HTTP Status Codes      ----------------------------------------------------------------------------------     | Code  | Description                                                                 ----------------------------------------------------------------------------------     | 200   | Success                                                                     ----------------------------------------------------------------------------------     | 400   | Bad request - the request was malformed or missing required parameters      ----------------------------------------------------------------------------------      | 401   | Unauthorized - invalid or missing API key                                   ----------------------------------------------------------------------------------     | 403   | Forbidden - API key does not have access to the requested resource          ----------------------------------------------------------------------------------     | 404   | Not found - the requested resource does not exist                           ----------------------------------------------------------------------------------     | 429   | Too many requests - rate or quota limit exceeded                            ----------------------------------------------------------------------------------     | 500   | Internal server error - an unexpected error on the API server               ----------------------------------------------------------------------------------     | 50x   | Errors specific to various endpoints                                        ----------------------------------------------------------------------------------   `Error Response Format`  Error responses will be returned in JSON format:      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }   The error object contains:  - `message` - A general error message   - `details` - More specific details about the error   `Common Errors`  401 Unauthorized      {       \"error\": {         \"message\": \"Invalid authentication\",         \"details\": [           \"The API key provided is invalid\"          ]       }     }   Details:   This error message indicates there is a problem with the API key:  - The API key is missing from the request  - The key is invalid or incorrect  - The key is expired or revoked   Check that you are sending the correct API key in the Authorization header.  403 Forbidden      {       \"error\": {         \"message\": \"Forbidden access\",         \"details\": [           \"Your API key does not have access to the requested data\"          ]       }     }  Details:  This error message indicates that the API key being used does not have access to perform the requested operation. Ensure the key has the required scopes enabled.   404 Not Found      {       \"error\": {         \"message\": \"Data not found\",         \"details\": [           \"The requested data does not exist.\"          ]       }     }   Details:  This error message indicates that the object specified by the request does not exist. For example, requesting a keyword that is not in your SEOmonitor account.   429 Too Many Requests   Daily Quota Exceeded      {       \"error\": {         \"message\": \"Daily quota exceeded\",         \"details\": [           \"You have exceeded the allowed daily requests\"          ]       }     }   Details:  This error message indicates that the request exceeds the rate limits for daily requests. Retry the request after some delay.   Rate Limit Exceeded      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }   Details:  This error message indicates that the request exceeds the rate limits for requests per second. Retry the request after some delay.   500 Internal Server Error       {       \"error\": {         \"message\": \"Internal server error\",         \"details\": [           \"The server encountered an error while processing your requests\"          ]       }     }   Details:  This error message indicates that an unexpected error occurred on the API server. Try the request again later. If the issue persists, contact support.   50X Endpoint-specific errors  You may encounter errors on specific endpoint requests – these are listed and explained under each endpoint page.   Support  If you have any questions about API errors, please contact our support team.   `Changelog`  Version 3.0 (current)   Release Date: ?  This is the first version of the API 3.0.  

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://www.seomonitor.com/](https://www.seomonitor.com/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = swagger_client.CampaignsApi(swagger_client.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *https://apix.seomonitor.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CampaignsApi* | [**dashboard_v30_campaigns_tracked_get**](docs/CampaignsApi.md#dashboard_v30_campaigns_tracked_get) | **GET** /dashboard/v3.0/campaigns/tracked | Get Tracked Campaigns
*ForecastApi* | [**forecast_v30_keywords_get**](docs/ForecastApi.md#forecast_v30_keywords_get) | **GET** /forecast/v3.0/keywords | Get Forecast keywords
*ForecastApi* | [**forecast_v30_objective_get**](docs/ForecastApi.md#forecast_v30_objective_get) | **GET** /forecast/v3.0/objective | Get Forecast objective Data
*ForecastApi* | [**forecast_v30_scenario_get**](docs/ForecastApi.md#forecast_v30_scenario_get) | **GET** /forecast/v3.0/scenario | Get Forecast scenario Data
*ForecastApi* | [**forecast_v30_scenarios_get**](docs/ForecastApi.md#forecast_v30_scenarios_get) | **GET** /forecast/v3.0/scenarios | Get Forecast scenarios
*KeywordResearchApi* | [**research_v30_domain_overview_get**](docs/KeywordResearchApi.md#research_v30_domain_overview_get) | **GET** /research/v3.0/domain-overview | Get URL/Domain Overview
*KeywordResearchApi* | [**research_v30_domain_ranking_keywords_get**](docs/KeywordResearchApi.md#research_v30_domain_ranking_keywords_get) | **GET** /research/v3.0/domain-ranking-keywords | Get Ranking Keywords
*KeywordResearchApi* | [**research_v30_keywords_get**](docs/KeywordResearchApi.md#research_v30_keywords_get) | **GET** /research/v3.0/keywords | Get Keyword Data
*KeywordResearchApi* | [**research_v30_ranking_data_get**](docs/KeywordResearchApi.md#research_v30_ranking_data_get) | **GET** /research/v3.0/ranking-data | Get Ranking Data
*KeywordResearchApi* | [**research_v30_related_keywords_get**](docs/KeywordResearchApi.md#research_v30_related_keywords_get) | **GET** /research/v3.0/related-keywords | Get Related Keywords
*KeywordResearchApi* | [**research_v30_topic_overview_get**](docs/KeywordResearchApi.md#research_v30_topic_overview_get) | **GET** /research/v3.0/topic-overview | Get Topic Overview
*KeywordVaultApi* | [**keyword_vault_v30_get_keyword_data_by_list_get**](docs/KeywordVaultApi.md#keyword_vault_v30_get_keyword_data_by_list_get) | **GET** /keyword-vault/v3.0/get-keyword-data-by-list | Get Keyword Data by List
*KeywordVaultApi* | [**keyword_vault_v30_get_overview_data_get**](docs/KeywordVaultApi.md#keyword_vault_v30_get_overview_data_get) | **GET** /keyword-vault/v3.0/get-overview-data | Get Overview Data
*OrganicTrafficApi* | [**organic_traffic_v30_daily_traffic_get**](docs/OrganicTrafficApi.md#organic_traffic_v30_daily_traffic_get) | **GET** /organic-traffic/v3.0/daily-traffic | Get Daily Traffic Data by Segment
*OrganicTrafficApi* | [**organic_traffic_v30_keywords_get**](docs/OrganicTrafficApi.md#organic_traffic_v30_keywords_get) | **GET** /organic-traffic/v3.0/keywords | Get Traffic Data by Keywords
*RankTrackerApi* | [**rank_tracker_v30_daily_share_of_clicks_get**](docs/RankTrackerApi.md#rank_tracker_v30_daily_share_of_clicks_get) | **GET** /rank-tracker/v3.0/daily-share-of-clicks | Get Daily Share of Clicks
*RankTrackerApi* | [**rank_tracker_v30_groups_daily_visibility_get**](docs/RankTrackerApi.md#rank_tracker_v30_groups_daily_visibility_get) | **GET** /rank-tracker/v3.0/groups/daily-visibility | Get Daily Group Visibility
*RankTrackerApi* | [**rank_tracker_v30_groups_data_get**](docs/RankTrackerApi.md#rank_tracker_v30_groups_data_get) | **GET** /rank-tracker/v3.0/groups/data | Get Groups Data
*RankTrackerApi* | [**rank_tracker_v30_groups_get**](docs/RankTrackerApi.md#rank_tracker_v30_groups_get) | **GET** /rank-tracker/v3.0/groups | Get Groups List
*RankTrackerApi* | [**rank_tracker_v30_keywords_competition_get**](docs/RankTrackerApi.md#rank_tracker_v30_keywords_competition_get) | **GET** /rank-tracker/v3.0/keywords/competition | Get Keywords Competition Data
*RankTrackerApi* | [**rank_tracker_v30_keywords_daily_ranks_get**](docs/RankTrackerApi.md#rank_tracker_v30_keywords_daily_ranks_get) | **GET** /rank-tracker/v3.0/keywords/daily-ranks | Get Daily Keyword Ranks
*RankTrackerApi* | [**rank_tracker_v30_keywords_get**](docs/RankTrackerApi.md#rank_tracker_v30_keywords_get) | **GET** /rank-tracker/v3.0/keywords | Get Keyword Data
*RankTrackerApi* | [**rank_tracker_v30_keywords_import_post**](docs/RankTrackerApi.md#rank_tracker_v30_keywords_import_post) | **POST** /rank-tracker/v3.0/keywords/import | Add New Keywords
*RankTrackerApi* | [**rank_tracker_v30_keywords_import_status_get**](docs/RankTrackerApi.md#rank_tracker_v30_keywords_import_status_get) | **GET** /rank-tracker/v3.0/keywords/import-status | Get Keywords Import Status
*RankTrackerApi* | [**rank_tracker_v30_keywords_ranking_pages_get**](docs/RankTrackerApi.md#rank_tracker_v30_keywords_ranking_pages_get) | **GET** /rank-tracker/v3.0/keywords/ranking-pages | Get Ranking Pages
*RankTrackerApi* | [**rank_tracker_v30_keywords_serp_feature_presence_get**](docs/RankTrackerApi.md#rank_tracker_v30_keywords_serp_feature_presence_get) | **GET** /rank-tracker/v3.0/keywords/serp-feature-presence | Get Daily SERP Feature Presence
*RankTrackerApi* | [**rank_tracker_v30_keywords_top_results_get**](docs/RankTrackerApi.md#rank_tracker_v30_keywords_top_results_get) | **GET** /rank-tracker/v3.0/keywords/top-results | Get Top 100 Results

## Documentation For Models

 - [AddCampaignPostBody](docs/AddCampaignPostBody.md)
 - [AddKeywords](docs/AddKeywords.md)
 - [AnalyticsData](docs/AnalyticsData.md)
 - [BestRank](docs/BestRank.md)
 - [CampaignDetailsRegular](docs/CampaignDetailsRegular.md)
 - [CampaignInfo](docs/CampaignInfo.md)
 - [CampaignVisibility](docs/CampaignVisibility.md)
 - [CampaignVisibilityTimeframes](docs/CampaignVisibilityTimeframes.md)
 - [CompletionStatus30days](docs/CompletionStatus30days.md)
 - [CompletionStatusDateSessions](docs/CompletionStatusDateSessions.md)
 - [ContentChange](docs/ContentChange.md)
 - [ContentChanges](docs/ContentChanges.md)
 - [ContentLandingPageIssue](docs/ContentLandingPageIssue.md)
 - [DailyShareOfClicks](docs/DailyShareOfClicks.md)
 - [DifficultyValue](docs/DifficultyValue.md)
 - [DomainCompetitorRank](docs/DomainCompetitorRank.md)
 - [DomainCompetitorVisibility](docs/DomainCompetitorVisibility.md)
 - [DomainOverviewTraffic](docs/DomainOverviewTraffic.md)
 - [DomainOverviewVisibility](docs/DomainOverviewVisibility.md)
 - [DomainRankingKeywordsData](docs/DomainRankingKeywordsData.md)
 - [DomainRankingsData](docs/DomainRankingsData.md)
 - [DomainVisibility](docs/DomainVisibility.md)
 - [ForecastAdditionalTraffic](docs/ForecastAdditionalTraffic.md)
 - [ForecastAdsEquivalent](docs/ForecastAdsEquivalent.md)
 - [ForecastConfigConversionData](docs/ForecastConfigConversionData.md)
 - [ForecastConfiguration](docs/ForecastConfiguration.md)
 - [ForecastKeywordAdditionalTraffic](docs/ForecastKeywordAdditionalTraffic.md)
 - [ForecastKeywordAvgRank](docs/ForecastKeywordAvgRank.md)
 - [ForecastKeywordData](docs/ForecastKeywordData.md)
 - [ForecastKeywords](docs/ForecastKeywords.md)
 - [ForecastMonthlyForecastTrafficSessions](docs/ForecastMonthlyForecastTrafficSessions.md)
 - [ForecastMonthlyForecasts](docs/ForecastMonthlyForecasts.md)
 - [ForecastMonthlyForecastsTraffic](docs/ForecastMonthlyForecastsTraffic.md)
 - [ForecastObjectiveData](docs/ForecastObjectiveData.md)
 - [ForecastObjectiveDetails](docs/ForecastObjectiveDetails.md)
 - [ForecastOverviewData](docs/ForecastOverviewData.md)
 - [ForecastOverviewInertialTraffic](docs/ForecastOverviewInertialTraffic.md)
 - [ForecastScenarioData](docs/ForecastScenarioData.md)
 - [ForecastScenarioSearchData](docs/ForecastScenarioSearchData.md)
 - [ForecastSeoGoal](docs/ForecastSeoGoal.md)
 - [ForecastTargetAvgRank](docs/ForecastTargetAvgRank.md)
 - [ForecastTargetAvgVisibility](docs/ForecastTargetAvgVisibility.md)
 - [ForecastTargetData](docs/ForecastTargetData.md)
 - [ForecastTrafficConversions](docs/ForecastTrafficConversions.md)
 - [ForecastTrafficEstimatedAvgRanks](docs/ForecastTrafficEstimatedAvgRanks.md)
 - [ForecastTrafficRevenue](docs/ForecastTrafficRevenue.md)
 - [ForecastTrafficVisibility](docs/ForecastTrafficVisibility.md)
 - [Group](docs/Group.md)
 - [GroupDailyVisibility](docs/GroupDailyVisibility.md)
 - [GroupDetails](docs/GroupDetails.md)
 - [GroupDetailsVisibility](docs/GroupDetailsVisibility.md)
 - [GroupKeywordCounters](docs/GroupKeywordCounters.md)
 - [GroupsAvgRank](docs/GroupsAvgRank.md)
 - [GroupsDesktopVisibility](docs/GroupsDesktopVisibility.md)
 - [GroupsDetailsKeywordsCounters](docs/GroupsDetailsKeywordsCounters.md)
 - [GroupsFeatureVisibility](docs/GroupsFeatureVisibility.md)
 - [GroupsImportPostBody](docs/GroupsImportPostBody.md)
 - [GroupsMobileVisibility](docs/GroupsMobileVisibility.md)
 - [GroupsOpportunity](docs/GroupsOpportunity.md)
 - [GroupsSearchData](docs/GroupsSearchData.md)
 - [GroupsSearchIntent](docs/GroupsSearchIntent.md)
 - [GroupsSerpData](docs/GroupsSerpData.md)
 - [GroupsSerpMobileDesktop](docs/GroupsSerpMobileDesktop.md)
 - [GroupsTrafficData](docs/GroupsTrafficData.md)
 - [GroupsVisibility](docs/GroupsVisibility.md)
 - [GroupsVolumeByDevice](docs/GroupsVolumeByDevice.md)
 - [GscData](docs/GscData.md)
 - [KeywordCanibalizationLandingPageChange](docs/KeywordCanibalizationLandingPageChange.md)
 - [KeywordCanibalizationOnDate](docs/KeywordCanibalizationOnDate.md)
 - [KeywordCanibalizationRankData](docs/KeywordCanibalizationRankData.md)
 - [KeywordCompetition](docs/KeywordCompetition.md)
 - [KeywordCompetitorRankingData](docs/KeywordCompetitorRankingData.md)
 - [KeywordDailyRank](docs/KeywordDailyRank.md)
 - [KeywordDailyRankingData](docs/KeywordDailyRankingData.md)
 - [KeywordDailyRanks](docs/KeywordDailyRanks.md)
 - [KeywordDetail](docs/KeywordDetail.md)
 - [KeywordLandingPages](docs/KeywordLandingPages.md)
 - [KeywordRankTrend](docs/KeywordRankTrend.md)
 - [KeywordRankingData](docs/KeywordRankingData.md)
 - [KeywordResearchRankingData](docs/KeywordResearchRankingData.md)
 - [KeywordSerpData](docs/KeywordSerpData.md)
 - [KeywordSerpFeature](docs/KeywordSerpFeature.md)
 - [KeywordSerpResult](docs/KeywordSerpResult.md)
 - [KeywordTrafficData](docs/KeywordTrafficData.md)
 - [KeywordTrafficEcommerce](docs/KeywordTrafficEcommerce.md)
 - [KeywordTrafficGoals](docs/KeywordTrafficGoals.md)
 - [KeywordVaultGetKeywordDataByList](docs/KeywordVaultGetKeywordDataByList.md)
 - [KeywordVaultGetOverviewData](docs/KeywordVaultGetOverviewData.md)
 - [KeywordsImportPostBody](docs/KeywordsImportPostBody.md)
 - [KeywordsImportStatus](docs/KeywordsImportStatus.md)
 - [LandingPages](docs/LandingPages.md)
 - [MonthlySearches](docs/MonthlySearches.md)
 - [Objective](docs/Objective.md)
 - [ObjectiveCompletionStatus](docs/ObjectiveCompletionStatus.md)
 - [Opportunity](docs/Opportunity.md)
 - [OverviewTrafficData](docs/OverviewTrafficData.md)
 - [RankingKeywords](docs/RankingKeywords.md)
 - [RankingPages](docs/RankingPages.md)
 - [ResearchDomainOverview](docs/ResearchDomainOverview.md)
 - [ResearchDomainRanking](docs/ResearchDomainRanking.md)
 - [ResearchKeywords](docs/ResearchKeywords.md)
 - [ResearchRankingData](docs/ResearchRankingData.md)
 - [ResearchSearchData](docs/ResearchSearchData.md)
 - [ResearchSerpData](docs/ResearchSerpData.md)
 - [ResearchSerpFeature](docs/ResearchSerpFeature.md)
 - [Scenarios](docs/Scenarios.md)
 - [SearchData](docs/SearchData.md)
 - [SearchesPercentagesByDevice](docs/SearchesPercentagesByDevice.md)
 - [SerpFeatuersCounter](docs/SerpFeatuersCounter.md)
 - [SerpFeaturePresence](docs/SerpFeaturePresence.md)
 - [SerpFeaturePresenceByDevice](docs/SerpFeaturePresenceByDevice.md)
 - [SerpFeaturePresenceSerpData](docs/SerpFeaturePresenceSerpData.md)
 - [ShareOfClicksDomains](docs/ShareOfClicksDomains.md)
 - [Top100Results](docs/Top100Results.md)
 - [TopResults](docs/TopResults.md)
 - [TopicKeywordDetail](docs/TopicKeywordDetail.md)
 - [TopicOverviewSerpData](docs/TopicOverviewSerpData.md)
 - [TopicOverviewSerpFeature](docs/TopicOverviewSerpFeature.md)
 - [TopicOverviewVisibility](docs/TopicOverviewVisibility.md)
 - [TopicsOverview](docs/TopicsOverview.md)
 - [TrafficEcommerce](docs/TrafficEcommerce.md)
 - [TrafficGoals](docs/TrafficGoals.md)
 - [TrafficKeywords](docs/TrafficKeywords.md)
 - [TrafficKeywordsEcommerce](docs/TrafficKeywordsEcommerce.md)
 - [TrafficKeywordsGoals](docs/TrafficKeywordsGoals.md)
 - [TrafficOverview](docs/TrafficOverview.md)
 - [TrafficUnallocated](docs/TrafficUnallocated.md)
 - [VisibilityDesktopMobile](docs/VisibilityDesktopMobile.md)
 - [WebsiteExplorerKeywordCompetitorData](docs/WebsiteExplorerKeywordCompetitorData.md)

## Documentation For Authorization


## AuthorizationToken

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

customer.success@seomonitor.com
