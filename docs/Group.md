# Group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** | The unique identifier for the keyword group. It can be used to reference the group in other endpoints. | [optional] 
**name** | **str** | The name of the group. | [optional] 
**type** | **str** | Indicates the type of group - either a regular group, a folder for organizing groups, or smart group based on rules.   Possible values are &#x60;group&#x60;, &#x60;folder&#x60;, or &#x60;smart_group&#x60;. | [optional] 
**subgroups** | [**list[Group]**](Group.md) | Parent field containing subgroup objects if the group type is &#x60;folder&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

