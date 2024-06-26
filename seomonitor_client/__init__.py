# coding: utf-8

# flake8: noqa

"""
    SEOmonitor API Documentation

    `Introduction`  The SEOmonitor API allows you to programmatically access keyword ranking, traffic, and other SEO data from the SEOmonitor platform. You can use the API to build custom reports, automate workflows, and integrate SEOmonitor data into your own applications. The API enables free and unrestricted access to all your data in the platform, for all Tracked Campaigns. Additionally, it provides access to SEOmonitor's curated UK and US keyword database.   `Main Capabilities`  These are the main data sets you can retrieve with the API 3.0 endpoints:  `Campaign-level data`: Campaign details and campaign-wide keyword data, landing page data, groups data, traffic data, content opportunities data, forecast data, or campaign website research data.  `Keyword-level data`: Data for any and all keywords in the campaign, including ranking data, search data, SERP data, competitor data, SEO Opportunity, keyword-level traffic data, content optimization opportunities' data by keyword and keyword-level forecast projections data.  `Keyword group-level data`: Data for any keyword group in the campaign, including aggregated search and SERP data, website Visibility on specific groups, group SEO Opportunity data.  `Landing page-level data`: Data for specific landing pages that are ranking with the keywords in the campaign, including aggregated search and SERP data, SEO Opportunity, and landing page Visibility.  `Organic traffic data`: Data for the website's organic sessions, conversions, and revenue, including traffic data by segments (brand, non-brand, all traffic, and custom user-created traffic segments), by specific keywords and by specific landing pages.  `Keyword & website research data`: Data for any keyword in SEOmonitor's Research database – any domain-level aggregated search, SERP, and ranking data, and keyword-level and keyword list-level metrics, for the tracked website and for any competitor in top 100.  `Forecast data`: Overview data and details for specific Forecast Scenarios and Objectives, and keyword-level forecast data.  `Website content data`: Data related to content optimization opportunities of the tracked website, including landing page and keyword data for each of the content opportunities categories in SEOmonitor's Content Audit platform (Positive and negative correlations with Visibility, Cannibalization issues, Pages serving too many keywords, Keywords with missing pages, Suboptimal keyword inclusion in the title or H1 or page content, Pages with missing title or H1).   `Getting Started`  Log into your SEOmonitor account and retrieve your unique API Token (Account Settings > Edit Profile).  Check out the `quick start guide` to make your first API call.  Read through the `authentication guide` to learn how to properly authenticate your API requests.   `Libraries and SDKs`  SEOmonitor API uses HTTP protocol, which allows the application of our API to almost all programming languages. All the responses are returned in JSON format by default.  For convenience, we offer client libraries for popular programming languages:  JavaScript PHP Python Java   `Support`  Need help using the API, or have general inquiries? Please contact our support team.  For more information about the SEOmonitor platform, you can visit www.seomonitor.com.   `Changelog`      This is the first version of API 3.0. The Changelog page will be updated as we continue to develop new features and improvements.     `Quick Start Guide`  This guide will walk you through making your first API call.  `Get your API key`  First, you'll need to get an API key:      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Go to Account Settings > Edit Profile     3. Copy the API Token to use in your API requests  Note: Clicking `Regenerate API Token` will overwrite the current key and you will lose access if you or other users are currently using it.   `Make a request`  Next, we'll use cURL to make a request to get Tracked Campaigns details:      curl --request GET \\     --url https://apigw.seomonitor.com/v3//dashboard/v3.0/campaigns/tracked \\     --header 'Accept: application/json' \\     --header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZW9tb25pdG9yLmNvbSIsImlhdCI6MTY1Mjc4NTcwNCwidXNlcl9pZCI6IjY2NTI5In0.2_l9e7ohs9QHbwmr48mIoEF-QxZHNPFiAzJbMk00jcA'  This will retrieve the Tracked Campaigns data for an SEOmonitor account having the following API Token:      'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZW9tb25pdG9yLmNvbSIsImlhdCI6MTY1Mjc4NTcwNCwidXNlcl9pZCI6IjY2NTI5In0.2_l9e7ohs9QHbwmr48mIoEF-QxZHNPFiAzJbMk00jcA'   Let's break down the parts of the request:      - `--request GET` - Make a GET request     - `--url` - The API endpoint URL     - `--header` - Adds the Authorization header with your API key   Handle the response  The API will return a JSON response like this:      {       \"campaign_info\": {         \"id\": \"74516\",         \"name\": \"Asos.com\",          \"company\": \"Asos\",         \"company_id\": \"51256\",         \"domain\": \"www.asos.com\",         \"keyword_count\": 588,          \"date_created\": \"2023-04-25\",         \"location\": \"United Kingdom\",         \"currency\": \"EUR\",         \"mrr\": 3000       },       \"visibility\": {         \"desktop\": {           \"latest\": 0.28,           \"trend_7days\": 0.2,           \"trend_30days\": 0.2         },         \"mobile\": {           \"latest\": 0.27,            \"trend_7days\": 0.2,           \"trend_30days\": 0.2         }       },       \"multiple_locations\": [         {           \"campaign_id\": 12746,           \"location\": \"London, United Kingdom\",           \"visibility\": {             \"desktop\": {               \"latest\": 0.32,               \"trend_7days\": 0.02               \"trend_30days: 0.1               },             \"mobile\": {               \"latest\": 0.33,               \"trend\": 0.03               \"trend_30days\": 0.1                 }             }           }         }       ],       \"health_status\": \"healthy\",       \"objective_status\": {         \"actual_sessions\": 78400,         \"estimated_sessions\": 78400,           \"performance\": 1,         \"status\": \"on_track\",         \"start_month\": \"Jun, 2023\",          \"end_month\": \"Jul, 2024\"       },       \"reporting_status\": \"submitted\",       \"account_manager\": \"Jo Hart\"     }  And that's it! You just made your first API call. Check out the rest of the API reference documentation to see what else you can build.  `Best practices`      - Keep your API key private – do not share your key publicly.     - Do not include your key directly in code that you distribute – use environment variables instead.     - Regenerate your key periodically for improved security.     - Limit API key access to only required endpoints if possible.  `Revoking API keys`  If your API key is compromised, you can revoke it by regenerating the API Token in your SEOmonitor Account Settings. This will immediately invalidate the current key so further requests can't be made.  For any other issues with authentication, contact our support team.   `Retrieve the IDs of the company, campaigns, keywords and keyword groups`  The unique IDs of your company, campaigns, keywords, or keyword groups can be retrieved either from the specific URLs of the platform, or from specific API endpoint responses. Further below you'll find details on these alternatives.   `Company ID`  The company ID can only be retrieved from the platform. Follow these steps:      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Go to Account Settings > Billing     3. In the Billing section, the platform URL contains the company ID.     E.g.: \"app.seomonitor.com/v2/account/company/51244/billing\" – in this example, the company ID is \"51244\"   `Campaign ID`  To retrieve the campaign ID from the platform, follow these steps:       1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign by clicking on its name in the Agency Dashboard.     3. By default, the campaign opens in the Rank Tracker view. The platform URL contains the company ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/0/desktop/keywords?timeframe=2023-09-04%3A2023-10-04\" – in this example, the campaign ID is \"72416\".  To retrieve the campaign ID through the API, make a call through the `Get Tracked Campaigns Details endpoint`. The response will contain the details of the requested Tracked Campaigns, including their IDs, which you can further use in other endpoint requests.   `Keyword ID`  To retrieve the keyword ID from the platform, follow these steps:       1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and click on the required keyword.     3. The platform URL for the keyword view (Keyword Sidebar) contains the keyword ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/0/desktop/keywords?timeframe=2023-09-04%3A2023-10-04&ksid=7063139\" – in this example, the keyword ID is \"7063139\"   To retrieve the keyword ID through the API, make a call through the `Get Keyword Data endpoint`. The response will contain the details of the requested keywords, including their IDs, which you can further use in other endpoint requests.   `Keyword Group ID`      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and click on the required keyword group (Groups side-menu).     3. The platform URL for the keyword group view contains the keyword ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/69976/desktop/keywords?timeframe=2023-09-04%3A2023-10-04\" – in this example, the keyword group ID is \"69976\"  To retrieve the keyword group ID through the API, make a call through the `Get Groups List endpoint`. The response will contain the details of the requested keyword groups, including their IDs, which you can further use in other endpoint requests.   `Forecast ID for Scenarios or Objectives`      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and go to Forecast from the main menu (top).     3. Select a Scenario or the Objective (if set). The platform URL for the specific scenario contains the forecast ID.     E.g.: \"https://app.seomonitor.com/v2/forecast/118794/3788\" – in this example, the forecast ID is \"3788\"   To retrieve the forecast ID through the API, make a call through the`Get Forecast Scenarios endpoint`. The response will contain the details of the requested Scenario or Objective, including their IDs, which you can further use in other endpoint requests.   `SERP Feature Abbreviations`  The returned data for some endpoints will contain SERP feature names in abbreviated form.  The returned values for SERP features are abbreviated as follows:      - \"adt\": Ads Pack Top     - \"def\": Definitions      - \"dir\": Directions      - \"fsn\": Featured Snippet      - \"flt\": Flights      - \"htl\": Hotels      - \"img\": Images Pack      - \"job\": Jobs      - \"kng\": Knowledge Graph      - \"geo\": Local Pack      - \"shp\": Product listing      - \"rcp\": Recipes      - \"qns\": Questions      - \"new\": Top Stories      - \"vid\": Video Carousel      - \"app\": Apps    `Rate Limits`  There are request limits in place to prevent abuse and ensure fair usage.   Exceeding the request limits will lead to HTTP 429 responses. If you need higher limits, contact our support team.   `Limits & Quotas`      -------------------------------------------------------------------------     |Limit                                    |  Number of requests              -------------------------------------------------------------------------     |Maximum requests per second              |  10                              -------------------------------------------------------------------------     |Maximum rows per request (Request Quota) |  1000                            -------------------------------------------------------------------------     |Daily Quota                              |  10 000                          -------------------------------------------------------------------------   `Exceeding Limits`  If you exceed the rate limits, you will receive a 429 Too Many Requests response.  Daily Quota Exceeded      {       \"error\": {         \"message\": \"Daily quota exceeded\",         \"details\": [           \"You have exceeded the allowed daily requests\"          ]       }     }  Details:  This error message indicates that the request exceeds the rate limits for daily requests. Retry the request after some delay.  Rate Limit Exceeded      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }  Details:  This error message indicates that the request exceeds the rate limits for requests per second. Retry the request after some delay.   `Increasing Limits`  The default limits allow most normal API usage patterns. However, if you need higher limits, please contact our support team.    Provide details on:      - Your specific use case      - The endpoints you are using     - The increased limits you are looking for  We will review your request and adjust limits where appropriate   `Need Higher Limits?`  For most use cases, the default limits are sufficient. But if you require higher limits, please contact our support team. We will review your use case and adjust limits where appropriate.   `Errors`  SEOmonitor API uses standard HTTP response codes to indicate the success or failure of API requests.   HTTP Status Codes      ----------------------------------------------------------------------------------     | Code  | Description                                                                 ----------------------------------------------------------------------------------     | 200   | Success                                                                     ----------------------------------------------------------------------------------     | 400   | Bad request - the request was malformed or missing required parameters      ----------------------------------------------------------------------------------      | 401   | Unauthorized - invalid or missing API key                                   ----------------------------------------------------------------------------------     | 403   | Forbidden - API key does not have access to the requested resource          ----------------------------------------------------------------------------------     | 404   | Not found - the requested resource does not exist                           ----------------------------------------------------------------------------------     | 429   | Too many requests - rate or quota limit exceeded                            ----------------------------------------------------------------------------------     | 500   | Internal server error - an unexpected error on the API server               ----------------------------------------------------------------------------------     | 50x   | Errors specific to various endpoints                                        ----------------------------------------------------------------------------------   `Error Response Format`  Error responses will be returned in JSON format:      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }   The error object contains:  - `message` - A general error message   - `details` - More specific details about the error   `Common Errors`  401 Unauthorized      {       \"error\": {         \"message\": \"Invalid authentication\",         \"details\": [           \"The API key provided is invalid\"          ]       }     }   Details:   This error message indicates there is a problem with the API key:  - The API key is missing from the request  - The key is invalid or incorrect  - The key is expired or revoked   Check that you are sending the correct API key in the Authorization header.  403 Forbidden      {       \"error\": {         \"message\": \"Forbidden access\",         \"details\": [           \"Your API key does not have access to the requested data\"          ]       }     }  Details:  This error message indicates that the API key being used does not have access to perform the requested operation. Ensure the key has the required scopes enabled.   404 Not Found      {       \"error\": {         \"message\": \"Data not found\",         \"details\": [           \"The requested data does not exist.\"          ]       }     }   Details:  This error message indicates that the object specified by the request does not exist. For example, requesting a keyword that is not in your SEOmonitor account.   429 Too Many Requests   Daily Quota Exceeded      {       \"error\": {         \"message\": \"Daily quota exceeded\",         \"details\": [           \"You have exceeded the allowed daily requests\"          ]       }     }   Details:  This error message indicates that the request exceeds the rate limits for daily requests. Retry the request after some delay.   Rate Limit Exceeded      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }   Details:  This error message indicates that the request exceeds the rate limits for requests per second. Retry the request after some delay.   500 Internal Server Error       {       \"error\": {         \"message\": \"Internal server error\",         \"details\": [           \"The server encountered an error while processing your requests\"          ]       }     }   Details:  This error message indicates that an unexpected error occurred on the API server. Try the request again later. If the issue persists, contact support.   50X Endpoint-specific errors  You may encounter errors on specific endpoint requests – these are listed and explained under each endpoint page.   Support  If you have any questions about API errors, please contact our support team.   `Changelog`  Version 3.0 (current)   Release Date: ?  This is the first version of the API 3.0.    # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: customer.success@seomonitor.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from seomonitor_client.api.campaigns_api import CampaignsApi
from seomonitor_client.api.forecast_api import ForecastApi
from seomonitor_client.api.keyword_research_api import KeywordResearchApi
from seomonitor_client.api.keyword_vault_api import KeywordVaultApi
from seomonitor_client.api.organic_traffic_api import OrganicTrafficApi
from seomonitor_client.api.rank_tracker_api import RankTrackerApi
# import ApiClient
from seomonitor_client.api_client import ApiClient
from seomonitor_client.configuration import Configuration
# import models into sdk package
from seomonitor_client.models.add_campaign_post_body import AddCampaignPostBody
from seomonitor_client.models.add_keywords import AddKeywords
from seomonitor_client.models.analytics_data import AnalyticsData
from seomonitor_client.models.best_rank import BestRank
from seomonitor_client.models.campaign_details_regular import CampaignDetailsRegular
from seomonitor_client.models.campaign_info import CampaignInfo
from seomonitor_client.models.campaign_visibility import CampaignVisibility
from seomonitor_client.models.campaign_visibility_timeframes import CampaignVisibilityTimeframes
from seomonitor_client.models.completion_status30days import CompletionStatus30days
from seomonitor_client.models.completion_status_date_sessions import CompletionStatusDateSessions
from seomonitor_client.models.content_change import ContentChange
from seomonitor_client.models.content_changes import ContentChanges
from seomonitor_client.models.content_landing_page_issue import ContentLandingPageIssue
from seomonitor_client.models.daily_share_of_clicks import DailyShareOfClicks
from seomonitor_client.models.difficulty_value import DifficultyValue
from seomonitor_client.models.domain_competitor_rank import DomainCompetitorRank
from seomonitor_client.models.domain_competitor_visibility import DomainCompetitorVisibility
from seomonitor_client.models.domain_overview_traffic import DomainOverviewTraffic
from seomonitor_client.models.domain_overview_visibility import DomainOverviewVisibility
from seomonitor_client.models.domain_ranking_keywords_data import DomainRankingKeywordsData
from seomonitor_client.models.domain_rankings_data import DomainRankingsData
from seomonitor_client.models.domain_visibility import DomainVisibility
from seomonitor_client.models.forecast_additional_traffic import ForecastAdditionalTraffic
from seomonitor_client.models.forecast_ads_equivalent import ForecastAdsEquivalent
from seomonitor_client.models.forecast_config_conversion_data import ForecastConfigConversionData
from seomonitor_client.models.forecast_configuration import ForecastConfiguration
from seomonitor_client.models.forecast_keyword_additional_traffic import ForecastKeywordAdditionalTraffic
from seomonitor_client.models.forecast_keyword_avg_rank import ForecastKeywordAvgRank
from seomonitor_client.models.forecast_keyword_data import ForecastKeywordData
from seomonitor_client.models.forecast_keywords import ForecastKeywords
from seomonitor_client.models.forecast_monthly_forecast_traffic_sessions import ForecastMonthlyForecastTrafficSessions
from seomonitor_client.models.forecast_monthly_forecasts import ForecastMonthlyForecasts
from seomonitor_client.models.forecast_monthly_forecasts_traffic import ForecastMonthlyForecastsTraffic
from seomonitor_client.models.forecast_objective_data import ForecastObjectiveData
from seomonitor_client.models.forecast_objective_details import ForecastObjectiveDetails
from seomonitor_client.models.forecast_overview_data import ForecastOverviewData
from seomonitor_client.models.forecast_overview_inertial_traffic import ForecastOverviewInertialTraffic
from seomonitor_client.models.forecast_scenario_data import ForecastScenarioData
from seomonitor_client.models.forecast_scenario_search_data import ForecastScenarioSearchData
from seomonitor_client.models.forecast_seo_goal import ForecastSeoGoal
from seomonitor_client.models.forecast_target_avg_rank import ForecastTargetAvgRank
from seomonitor_client.models.forecast_target_avg_visibility import ForecastTargetAvgVisibility
from seomonitor_client.models.forecast_target_data import ForecastTargetData
from seomonitor_client.models.forecast_traffic_conversions import ForecastTrafficConversions
from seomonitor_client.models.forecast_traffic_estimated_avg_ranks import ForecastTrafficEstimatedAvgRanks
from seomonitor_client.models.forecast_traffic_revenue import ForecastTrafficRevenue
from seomonitor_client.models.forecast_traffic_visibility import ForecastTrafficVisibility
from seomonitor_client.models.group import Group
from seomonitor_client.models.group_daily_visibility import GroupDailyVisibility
from seomonitor_client.models.group_details import GroupDetails
from seomonitor_client.models.group_details_visibility import GroupDetailsVisibility
from seomonitor_client.models.group_keyword_counters import GroupKeywordCounters
from seomonitor_client.models.groups_avg_rank import GroupsAvgRank
from seomonitor_client.models.groups_desktop_visibility import GroupsDesktopVisibility
from seomonitor_client.models.groups_details_keywords_counters import GroupsDetailsKeywordsCounters
from seomonitor_client.models.groups_feature_visibility import GroupsFeatureVisibility
from seomonitor_client.models.groups_import_post_body import GroupsImportPostBody
from seomonitor_client.models.groups_mobile_visibility import GroupsMobileVisibility
from seomonitor_client.models.groups_opportunity import GroupsOpportunity
from seomonitor_client.models.groups_search_data import GroupsSearchData
from seomonitor_client.models.groups_search_intent import GroupsSearchIntent
from seomonitor_client.models.groups_serp_data import GroupsSerpData
from seomonitor_client.models.groups_serp_mobile_desktop import GroupsSerpMobileDesktop
from seomonitor_client.models.groups_traffic_data import GroupsTrafficData
from seomonitor_client.models.groups_visibility import GroupsVisibility
from seomonitor_client.models.groups_volume_by_device import GroupsVolumeByDevice
from seomonitor_client.models.gsc_data import GscData
from seomonitor_client.models.keyword_canibalization_landing_page_change import KeywordCanibalizationLandingPageChange
from seomonitor_client.models.keyword_canibalization_on_date import KeywordCanibalizationOnDate
from seomonitor_client.models.keyword_canibalization_rank_data import KeywordCanibalizationRankData
from seomonitor_client.models.keyword_competition import KeywordCompetition
from seomonitor_client.models.keyword_competitor_ranking_data import KeywordCompetitorRankingData
from seomonitor_client.models.keyword_daily_rank import KeywordDailyRank
from seomonitor_client.models.keyword_daily_ranking_data import KeywordDailyRankingData
from seomonitor_client.models.keyword_daily_ranks import KeywordDailyRanks
from seomonitor_client.models.keyword_detail import KeywordDetail
from seomonitor_client.models.keyword_landing_pages import KeywordLandingPages
from seomonitor_client.models.keyword_rank_trend import KeywordRankTrend
from seomonitor_client.models.keyword_ranking_data import KeywordRankingData
from seomonitor_client.models.keyword_research_ranking_data import KeywordResearchRankingData
from seomonitor_client.models.keyword_serp_data import KeywordSerpData
from seomonitor_client.models.keyword_serp_feature import KeywordSerpFeature
from seomonitor_client.models.keyword_serp_result import KeywordSerpResult
from seomonitor_client.models.keyword_traffic_data import KeywordTrafficData
from seomonitor_client.models.keyword_traffic_ecommerce import KeywordTrafficEcommerce
from seomonitor_client.models.keyword_traffic_goals import KeywordTrafficGoals
from seomonitor_client.models.keyword_vault_get_keyword_data_by_list import KeywordVaultGetKeywordDataByList
from seomonitor_client.models.keyword_vault_get_overview_data import KeywordVaultGetOverviewData
from seomonitor_client.models.keywords_import_post_body import KeywordsImportPostBody
from seomonitor_client.models.keywords_import_status import KeywordsImportStatus
from seomonitor_client.models.landing_pages import LandingPages
from seomonitor_client.models.monthly_searches import MonthlySearches
from seomonitor_client.models.objective import Objective
from seomonitor_client.models.objective_completion_status import ObjectiveCompletionStatus
from seomonitor_client.models.opportunity import Opportunity
from seomonitor_client.models.overview_traffic_data import OverviewTrafficData
from seomonitor_client.models.ranking_keywords import RankingKeywords
from seomonitor_client.models.ranking_pages import RankingPages
from seomonitor_client.models.research_domain_overview import ResearchDomainOverview
from seomonitor_client.models.research_domain_ranking import ResearchDomainRanking
from seomonitor_client.models.research_keywords import ResearchKeywords
from seomonitor_client.models.research_ranking_data import ResearchRankingData
from seomonitor_client.models.research_search_data import ResearchSearchData
from seomonitor_client.models.research_serp_data import ResearchSerpData
from seomonitor_client.models.research_serp_feature import ResearchSerpFeature
from seomonitor_client.models.scenarios import Scenarios
from seomonitor_client.models.search_data import SearchData
from seomonitor_client.models.searches_percentages_by_device import SearchesPercentagesByDevice
from seomonitor_client.models.serp_featuers_counter import SerpFeatuersCounter
from seomonitor_client.models.serp_feature_presence import SerpFeaturePresence
from seomonitor_client.models.serp_feature_presence_by_device import SerpFeaturePresenceByDevice
from seomonitor_client.models.serp_feature_presence_serp_data import SerpFeaturePresenceSerpData
from seomonitor_client.models.share_of_clicks_domains import ShareOfClicksDomains
from seomonitor_client.models.top100_results import Top100Results
from seomonitor_client.models.top_results import TopResults
from seomonitor_client.models.topic_keyword_detail import TopicKeywordDetail
from seomonitor_client.models.topic_overview_serp_data import TopicOverviewSerpData
from seomonitor_client.models.topic_overview_serp_feature import TopicOverviewSerpFeature
from seomonitor_client.models.topic_overview_visibility import TopicOverviewVisibility
from seomonitor_client.models.topics_overview import TopicsOverview
from seomonitor_client.models.traffic_ecommerce import TrafficEcommerce
from seomonitor_client.models.traffic_goals import TrafficGoals
from seomonitor_client.models.traffic_keywords import TrafficKeywords
from seomonitor_client.models.traffic_keywords_ecommerce import TrafficKeywordsEcommerce
from seomonitor_client.models.traffic_keywords_goals import TrafficKeywordsGoals
from seomonitor_client.models.traffic_overview import TrafficOverview
from seomonitor_client.models.traffic_unallocated import TrafficUnallocated
from seomonitor_client.models.visibility_desktop_mobile import VisibilityDesktopMobile
from seomonitor_client.models.website_explorer_keyword_competitor_data import WebsiteExplorerKeywordCompetitorData
