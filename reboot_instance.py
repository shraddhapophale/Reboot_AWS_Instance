#!/usr/bin/env python3
from cortexutils.responder import Responder
import requests
import boto3

class Reboot_AWS_Instance(Responder):
   def __init__(self):
       Responder.__init__(self)
       self.access_key = self.get_param('config.access_key', None, 'Access Key not found')
       self.secret_access_key = self.get_param('config.secret_access_key', None, 'Secret Access Key not found')
       self.observable = self.get_param('data.data', None, "Data is empty")

   def run(self):
       Responder.run(self)
       s3 = boto3.client(
            'ec2',
            # best stored keys in environmental variables
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_access_key,
       )

       my_ec2_instance_id = self.observable # add ec2 instance id but also best stored in env

       def start_ec2(ec2_instance_id):
            response = s3.start_instances(
            InstanceIds=[
            ec2_instance_id,
            ],
       # DryRun=True # change to fals to usd
       )
       return response

       start_ec2(my_ec2_instance_id)

if __name__ == '__main__':
  Reboot_AWS_Instance().run()
