# ContentChange

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**element** | **str** | The type of HTML element on the landing page. Types are Title, H1, H2, H3, H4, H5, H6 or BODY | [optional] 
**state_from** | **str** | The keyword occurrences status in the previous element content. States are missing, not-present, partialy-present or fully-present | [optional] 
**state_to** | **str** | The keyword occurrences status in the current element content. States are missing, not-present, partialy-present or fully-present | [optional] 
**content_from** | **str** | The previous content of the element | [optional] 
**content_to** | **str** | The current content of the element | [optional] 
**full_occurences** | **int** | This indicates if there are fully present keywords in the HTML element | [optional] 
**partial_occurences** | **int** | This indicates if there are partially present keywords in the HTML element | [optional] 
**full_occurences_change** | **int** | This is the difference between previous fully present occurrences count and the current fully present occurrences count in the element | [optional] 
**partial_occurences_change** | **int** | This is the difference between previous partially present occurrences count and the current partially present occurrences count in the element | [optional] 
**words_from** | **int** | The total number of words in the previous content of the BODY element. This is only applicable to BODY element | [optional] 
**words_to** | **int** | The total number of words in the current content of the BODY element. This is only applicable to BODY element | [optional] 
**percentage_change** | **float** | The percentage change of the content in the BODY element. This is only applicable to BODY element | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

