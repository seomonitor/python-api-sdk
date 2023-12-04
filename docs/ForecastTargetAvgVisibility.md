# ForecastTargetAvgVisibility

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_visibility** | **float** | The average Visibility calculated for the keywords included in the Objective for the month when the scenario was created. | [optional] 
**trend_3months** | **float** | The average increase or drop in Visibility for the keywords in the Objective, over the previous 3 months up to the month the scenario was created, weighted by the keywords&#x27; search volume. | [optional] 
**target_visibility** | **float** | The average target Visibility for the keywords in the Objective. If the &#x60;target_rank_range&#x60; parameter returns \&quot;true\&quot;, the &#x60;target_visibility&#x60; is the lower (worst) average target Visibility. | [optional] 
**best_target_visibility** | **int** | If the &#x60;target_rank_range&#x60; parameter returns \&quot;true\&quot;, this parameter is the higher (best) average target Visibility. If the &#x60;target_rank_range&#x60; parameter returns \&quot;false\&quot;, this parameter will return empty. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

