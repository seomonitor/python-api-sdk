# ForecastKeywordAvgRank

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_rank** | **int** | The initial rank of the keyword for the month when the scenario was created. | [optional] 
**actual_rank** | **int** | The latest rank of the keyword on the day the data is returned. Returns empty if the scenario is not set as an Objective. | [optional] 
**estimated_rank** | **int** | The estimated rank of the keyword for the month when the data is returned. If the Target Rank Range parameter is enabled for the Scenario or Objective, this is the value for the lower (worst) target rank. | [optional] 
**estimated_rank_best_target** | **int** | If the Target Rank Range parameter is enabled for the Scenario or Objective, this is the value for the higher (best) target rank. If not enabled, this parameter will return empty. | [optional] 
**target_rank** | **int** | The targetted rank of the keyword for the last month of the timeframe. If the Target Rank Range parameter is enabled for the Scenario or Objective, this is the value for the lower (worst) target rank. | [optional] 
**target_rank_best** | **int** | If the Target Rank Range parameter is enabled for the Scenario or Objective, this is the value for the higher (best) target rank. If not enabled, this parameter will return empty. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

