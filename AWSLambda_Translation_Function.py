import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    translate = boto3.client('translate')
    srctext = "Hello, World Maaz is here"
    srclang = "en"
    targlang = "ar"
    print('1')
    srclang = event['sourcelang']
    print(srclang)
    targlang = event['targetlang']
    print(targlang)
    srctext = event['text']
    print(srctext)

    result = translate.translate_text(Text=srctext, SourceLanguageCode=srclang, TargetLanguageCode=targlang)
    print("Translation output: " + str(result))
    #logging.info("Translation output: " + str(result))
    print(result.get('TranslatedText'))
    #logging.info("TranslatedText: " + result.get('TranslatedText'))

    return {
        'statusCode': 200,
        'body': result.get('TranslatedText'),
        'Translationoutput': result
    }
