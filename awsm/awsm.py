import boto3


class AWSManager():
    ec2_client = boto3.client('ec2')

    def ec2_instance(self):
        return self.ec2_client.describe_instances()
