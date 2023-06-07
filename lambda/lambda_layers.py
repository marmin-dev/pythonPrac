import boto3 # 파이썬 기반의 AWS API 라이브러리 AWS SDK
import os
import sys
import uuid # universal unique id
from urllib.parse import unquote_plus
from PIL import Image
import PIL.image

s3_client = boto3.client('s3')

def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail(tuple(x/2 for x in image.size))
        image.save(resized_path)

# 이벤트 파라미터에는 람다 함수를 트리거한 s3에서 전달한 값이 포함되어 있으며
# 테스트케이스에서 확인이 가능하다
def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name'] # example bucket
        key = record['s3']['object']['key'] # 버킷 값 키
        tmpkey = key.replace('/', '') # pathfilename 형식으로 변경

        # S3 버킷으로 부터 가져와서 저장할 경로와 썸네일 이미지를 저장할 경로를 지정
        download_path = '/tmp/{}{}'.format(uuid.uuid4(),tmpkey)
        upload_path = '/tmp/resized-{}'.format(tmpkey)

        s3_client.download_file(bucket,key,download_path)
        resize_image(download_path, upload_path)

        s3_client.uploadfild(upload_path, '{}-resized'.format(bucket), key)


