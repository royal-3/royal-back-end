
import os

env_content = """SECRET_KEY='django-insecure-(*06b@y4+oz5ozfo(4=(f8la_dr#bbvjcb#hti6=ob6mfv_w-_'
DEBUG=True
DATABASE_URL=postgresql://postgres.xoovtfudjbxrrqlyoxyd:Royaltouchup@360@aws-1-ap-south-1.pooler.supabase.com:6543/postgres
AWS_ACCESS_KEY_ID=03303d7eda4d59445862a8e0aa3ecbf1
AWS_SECRET_ACCESS_KEY=c5a7b15dd2dbcd0d5962765c9c46c4d3e7aaf0484048dba1f8bffa8d31d86265
AWS_STORAGE_BUCKET_NAME=royalimage
AWS_S3_ENDPOINT_URL=https://xoovtfudjbxrrqlyoxyd.storage.supabase.co/storage/v1/s3
AWS_S3_REGION_NAME=ap-south-1
"""

with open('.env', 'w', encoding='utf-8') as f:
    f.write(env_content.strip())

print("Refreshed .env file successfully.")
