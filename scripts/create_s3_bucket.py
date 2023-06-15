import boto3

def create_s3_bucket(bucket_name):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Create the S3 bucket
    s3.create_bucket(Bucket=bucket_name)

    print(f"Bucket {bucket_name} created successfully")
	# Replace 'my-bucket' with your desired bucket name
create_s3_bucket('my-bucket')