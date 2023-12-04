# ForecastTargetAvgRank

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_rank** | **int** | The average initial rank of the keywords included in the scenario, calculated for the month when the scenario was created. | [optional] 
**trend_3months** | **int** | The average increase or drop in positions of the keywords in the scenario, over the previous 3 months up to the month the scenario was created, weighted by the keywords&#x27; search volume. | [optional] 
**target_rank** | **int** | The average target rank of the keywords in the Objective. If the &#x60;target_rank_range&#x60; parameter returns \&quot;true\&quot;, the &#x60;target_rank&#x60; is the lower (worst) average target rank. | [optional] 
**best_target_rank** | **int** | If the &#x60;target_rank_range&#x60; parameter returns \&quot;true\&quot;, this parameter is the higher (best) average target rank. If the &#x60;target_rank_range&#x60; parameter returns \&quot;false\&quot;, this parameter will return empty. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

