import boto3
import psycopg2 as pg


class Redshift:

    def __init__(self, access_key, private_key, rs_user):
        self.access_key = access_key
        self.private_key = private_key
        self.rs_port = 5439
        self.rs_user = rs_user
        self.db = 'dbName'
        self.cluster_id = 'your_cluster_id'
        self.rs_host = 'your_host'
        self.region_name = 'your_region'
        self.client = self._client()

    def _client(self):
        return boto3.client(
            'redshift',
            region_name=self.region_name,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.private_key
        )

    def _get_creds(self):
        return self.client.get_cluster_credentials(DbUser=self.rs_user,
                                                   DbName=self.db,
                                                   ClusterIdentifier=self.cluster_id,
                                                   AutoCreate=True)

    def connect(self):
        """Redshift connection through IAM credentials"""
        cluster_creds = self._get_creds()

        try:
            conn = pg.connect(
                host=self.rs_host,
                port=self.rs_port,
                user=cluster_creds['DbUser'],
                password=cluster_creds['DbPassword'],
                database=self.db)
            return conn

        except pg.Error as e:
            print(f'Failed to open database connection!\n{e}')
