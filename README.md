## Overview

SEOmonitor API Documentation
- API version: 3.0.0

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
import seomonitor_client 
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
