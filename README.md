# Voice-to-Text-Sentiment-Analysis-Project-Documentation
This project converts customer feedback audio into text using Amazon Transcribe, and then analyzes the sentiment of the transcribed text using a machine learning model deployed on SageMaker.
🎧 Upload audio file (glance-136577.mp3) to S3
Bucket: norturareviewus
Prefix: nputaudio/

📝 Start a Transcribe job in ap-south-1
Output is stored at:
s3://norturareviewus/nputaudio/output/glance-136577.json

🔍 Extract transcription result from the .json

🧠 Prepare train.txt with data like:

kotlin
Copy
Edit
I love this product!,1
Very disappointed,0
Uploaded to: s3://norturareviewus/sentiment-model/train/train.txt

🚀 Train an XGBoost model in SageMaker using this data

🛰️ Deploy the model as a real-time endpoint
Endpoint Name: sentiment-analyzer-endpoint

📊 Use the endpoint to predict sentiment from transcribed text.

🧰 Tech Stack
Amazon S3

Amazon Transcribe

Amazon SageMaker

XGBoost

Python (boto3, sagemaker SDK)

