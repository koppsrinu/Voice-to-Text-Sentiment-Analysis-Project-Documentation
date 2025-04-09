import boto3

transcribe = boto3.client('transcribe', region_name='ap-south-1')

job_name = "glance-transcription-job"
job_uri = "s3://norturareviewus/nputaudio/glance-136577.mp3"

response = transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='mp3',
    LanguageCode='en-US',
    OutputBucketName='norturareviewus',
    OutputKey='nputaudio/output/glance-136577.json'
)

print("🎙️ Transcription job started...")
