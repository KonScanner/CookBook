import boto3
import os


class S3:

    def __init__(self):
        self.access_key = cr.a_key
        self.private_key = cr.p_key
        self.data_path = cr.data_path
        self.path_to_files = cr.path_to_files
        self.bucket_name = cr.bucket_name
        self.client = self._client()

    def _client(self):
        return boto3.client(
            's3',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.private_key
        )

    def _resource(self):
        return boto3.resource('s3', aws_access_key_id=self.access_key,
                              aws_secret_access_key=self.private_key)

    def _get_bucket(self, bucket, name):

        return self.client.get_object(Bucket=bucket, Key=name)

    def _make_bucket(self):
        return self.client.create_bucket(
            ACL='private',
            Bucket=cr.bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'eu-west-2'},)

    def _upload_files(self, path, bucket):
        for name in os.listdir(path):
            self._resource().meta.client.upload_file(
                Filename=path+name, Bucket=bucket, Key=name)

    def _download_file(self, bucket: str, bucket_path: str, local_path: str):
        return self._resource().meta.client.download_file(bucket, bucket_path, local_path)

    def _list_buckets(self):
        response = self._client().list_buckets()
        print('Existing buckets:')
        buckets = []
        for c, bucket in enumerate(response['Buckets']):
            buckets.append(bucket)
            print(f'  {bucket["Name"]}', c)
        return buckets

    def _terminate(self, bucket):
        self._resource().Bucket(bucket).objects.all().delete()
        self.client.delete_bucket(Bucket=bucket)
