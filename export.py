import boto3
s3 = boto3.resource('s3')
s3.create_bucket(Bucket='sunill9432bucket')