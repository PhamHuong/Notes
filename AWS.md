SDK for PHP
============================
- http://docs.aws.amazon.com/AWSSDKforPHP/latest/index.html#m=AmazonS3/get_object_filesize


ECS & EC2
============================
- https://aws.amazon.com/blogs/compute/how-to-create-a-custom-scheduler-for-amazon-ecs/
- http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_life_cycle.html
- http://boto3.readthedocs.org/en/latest/reference/services/ecs.html#id9
- Je18iMH&tIP!

ECS & EC2 API:
==================
- https://boto3.readthedocs.org/en/latest/guide/migrationec2.html#creating-the-connection
- https://boto.readthedocs.org/en/latest/ec2_tut.html
- https://boto.readthedocs.org/en/latest/ref/ec2containerservice.html
- https://boto.readthedocs.org/en/latest/ref/ec2.html#module-boto.ec2.connection
- http://boto3.readthedocs.org/en/latest/guide/migrationec2.html
- https://www.happycloudsolutions.com.au/blog/amazon-container-service-preview-docker-on-aws/#Definingatask - Example


```
import boto.ec2
boto.ec2.connection.EC2Connection(aws_access_key_id=None, aws_secret_access_key=None, is_secure=True, host=None, port=None, proxy=None, proxy_port=None, proxy_user=None, proxy_pass=None, debug=0, https_connection_factory=None, region=None, path='/', api_version=None, security_token=None, validate_certs=True, profile_name=None)
create_image(name, description=None, no_reboot=False, dry_run=False)¶

//connect to ec2
import boto.ecs
conn = boto.ecs.ECSConnection(aws_access_key_id = AWS_ACCESS_KEY, aws_secret_access_key = AWS_SECRET_KEY)
conn.get_all_instance_status()

//conect to ecs
import boto.ec2containerservice.layer1
ecs_conn= boto.ec2containerservice.layer1.EC2ContainerServiceConnection(aws_access_key_id = AWS_ACCESS_KEY, aws_secret_access_key = AWS_SECRET_KEY)
containers = ecs_conn.list_container_instances('aol-reporting-ecs')
```
