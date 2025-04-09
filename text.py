import json

s3 = boto3.client('s3', region_name='ap-south-1')

bucket = 'norturareviewus'
key = 'nputaudio/output/glance-136577.json'

response = s3.get_object(Bucket=bucket, Key=key)
transcript_data = json.loads(response['Body'].read())

transcribed_text = transcript_data['results']['transcripts'][0]['transcript']
print("📝 Transcribed Text:\n", transcribed_text)
