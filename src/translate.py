import boto3
import click

phrase = "Bonjour Madamme"
def action(phrase):
    client = boto3.client('translate', region_name='us-east-1')
    result = client.translate_text(Text=phrase, SourceLanguageCode="auto",
        TargetLanguageCode='en')
    text = result['TranslatedText']
    print(text)
    
if __name__=="__main__":    
    action(phrase)