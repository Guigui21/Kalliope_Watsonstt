# Kalliope_Watsonstt
## Synopsis
This TTS is based on the [Watson engine](https://www.ibm.com/watson/services/text-to-speech/)
## Options
| Parameters | Type | Required | Description |
| :------------- |:-------------|:-----|:-----|
| text | string | YES | The text to be synthesized. Provide plain text or text that is annotated with SSML. Text size is limited to 5 KB. |
| accept | string | NO | The requested audio format (MIME type) of the audio, 13 available ( [Infos](https://www.ibm.com/watson/developercloud/text-to-speech/api/v1/#synthesis_methods) ) |
| voice | string | NO | The voice that is to be used for the synthesis, see the voice column. |
## Voices
| Languages | Voice | Gender |
| :------------- |:-------------|:-----|
| Brazilian Portuguese | pt-BR_IsabelaVoice | Female |
| Castilian Spanish | es-ES_EnriqueVoice | Male |
| | es-ES_LauraVoice | Female |
| French | fr-FR_ReneeVoice | Female |
| German | de-DE_BirgitVoice | Female |
| | de-DE_DieterVoice | Male |
| Italian | it-IT_FrancescaVoice | Female |
| Japanese | ja-JP_EmiVoice | Female |
| Latin American Spanish | es-LA_SofiaVoice | Female |
| North American Spanish | es-US_SofiaVoice | Female |
| UK English | en-GB_KateVoice | Female |
| US English | en-US_AllisonVoice | Female |
| | en-US_LisaVoice | Female |
| | en-US_MichaelVoice | Male |
## Notes
Before to use you **need to register** [here](https://www.ibm.com/watson/services/text-to-speech/), choose get started free. 
On this [page](https://console.bluemix.net/catalog/services/text-to-speech/) choose Lite Tarification (by default).
When your account is validated you need to create Speech To Text Credential.
Once you’ve logged into Bluemix, go to your [dashboard](https://console.bluemix.net/dashboard/apps/). You should see the service you just created under the Services section.
Click on it and go to the "Service Credentials" section to “Add Credentials”.
Now you have your **username** and your **password** to use Watson STT.
