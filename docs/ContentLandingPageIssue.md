# ContentLandingPageIssue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_id** | **int** | Internal ID for this issue. | [optional] 
**url** | **str** | URL of the landing page | [optional] 
**type** | **str** | The type of the issue reported. Available values are: missing_title &#x3D;&gt; Pages with missing title or h1; suboptimal_title_inclusion &#x3D;&gt; Pages with suboptimal keyword inclusion in the title or h1; suboptimal_content_inclusion &#x3D;&gt; Pages with suboptimal keyword inclusion in the content; pages_with_many_keywords &#x3D;&gt; Pages considered to be serving too many keywords; visibility_increase &#x3D;&gt; Pages with an increase in the visibility metric that can be correlated with a content change; visibility_drop &#x3D;&gt; Pages with a drop in the visibility metric that can be correlated with a content change; | [optional] 
**keywords** | **list[int]** | Array of keyword IDs of the keywords which rank for this landing page. | [optional] 
**average_ctr** | **float** | The percentage of the search volume that ends up by clicking on the organic results. This is calculated for every keyword for their unique mix of SERP features. For a landing page, this is calculated by taking into account the CTR of every keyword it ranks for and the potential search volume of that particular keyword. | [optional] 
**search_volume** | **int** | The sum of the average search volume as an integer as provided by Google Ads for the keywords ranking for this landing page. | [optional] 
**year_over_year** | **float** | The Year-over-Year search trend as a positive or negative percentage calculated as last month Search Volume compared to one year ago, as provided by Google Ads. | [optional] 
**visibility_score** | **int** | The visibility score of the landing page as a percentage calculated by taking into account the ranks and the search volumes of the keywords the landing page ranks for. For more detalils on visibility metric: https://help.seomonitor.com/en/articles/6344566-reliable-visibility-metric | [optional] 
**visibility_score_change** | **int** | The visibility score change for the past 30 days as a positive or negative percentage. For more information on the visibility trend: https://help.seomonitor.com/en/articles/6344738-visibility-trend-explainer | [optional] 
**difficulty** | [**DifficultyValue**](DifficultyValue.md) |  | [optional] 
**opportunity_score** | **int** | The opportunity score of this particular landing page. This indicates on a scale of 1 to 10 the potential benefits of optimizing this landing page to rank in top 3 for it&#x27;s keywords as compared to the difficulty of reaching that milestone. For more information about keywords and groups of keywords opportunity score: https://help.seomonitor.com/en/articles/6222130-seo-opportunity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

