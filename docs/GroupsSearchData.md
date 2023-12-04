# GroupsSearchData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_volume** | **int** | The average 12-month search volume of all the keywords included in the group, as provided by Google Ads. | [optional] 
**monthly_searches** | [**list[MonthlySearches]**](MonthlySearches.md) | An array of objects containing the aggregated search volumes for each of the previous 13 months as provided by Google Ads. | [optional] 
**volume_by_device** | [**GroupsVolumeByDevice**](GroupsVolumeByDevice.md) |  | [optional] 
**year_over_year** | **float** | A numeric value representing the last month&#x27;s search volume divided by the search volume of the same month of the previous year. E.g. +49% year-over-year search trend would be represented as 1.49.  The returned values will be capped at 10, which represents \&quot;newcomers\&quot; (keywords that registered very low search volumes in the previous year). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

