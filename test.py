## Documentation


# List the ec2 instances

# import boto3

# ec2 = boto3.client('ec2')
# response = ec2.describe_instances()
# print(response)

# ======================================================================

# Reboot ec2 instance

# import boto3
# from botocore.exceptions import ClientError


# ec2 = boto3.client('ec2')
# INSTANCE_ID = "i-0e7dc2689985f4ba2"

# try:
#     ec2.reboot_instances(InstanceIds=[INSTANCE_ID], DryRun=True)
# except ClientError as e:
#     if 'DryRunOperation' not in str(e):
#         print("You don't have permission to reboot instances.")
#         raise

# try:
#     response = ec2.reboot_instances(InstanceIds=[INSTANCE_ID], DryRun=False)
#     print('Success', response)
# except ClientError as e:
#     print('Error', e)

#====================================================================
# Stop ec2 instance

# import boto3
# from botocore.exceptions import ClientError

# ec2 = boto3.client('ec2')
# instance_id = "i-0e7dc2689985f4ba2"
# try:
#         ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
# except ClientError as e:
#         if 'DryRunOperation' not in str(e):
#             raise

#     # Dry run succeeded, call stop_instances without dryrun
# try:
#         response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
#         print(response)
# except ClientError as e:
#         print(e)

# =====================================================================

# start the ec2 instance

# import boto3
# from botocore.exceptions import ClientError

# ec2 = boto3.client('ec2')
# instance_id = "i-0e7dc2689985f4ba2"

# try:
#     ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
# except ClientError as e:
#         if 'DryRunOperation' not in str(e):
#             raise

#     # Dry run succeeded, run start_instances without dryrun
# try:
#     response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
#     print(response)
# except ClientError as e:
#         print(e)

# ============================================================
# create the instances

# import boto3
# from botocore.exceptions import ClientError

# ec2 = boto3.client('ec2')

# instances = ec2.run_instances(
#     ImageId='ami-04505e74c0741db8d',                     ubuntu
#     MinCount=1,
#     MaxCount=1,
#     InstanceType='t2.micro',
#     SecurityGroupIds= ['sg-0be1291dabfeeface']           security-wizard-2
# )
# for instance in ec2.instances:
#     print(f'EC2 instance "{instance.id}" has been launched')


# instance_id = 'i-0e7dc2689985f4ba2'
# print(len(ec2.describe_instances().get('Reservations')))
# ec2.terminate_instances(InstanceIds=[instance_id])




# --Command to run container
# docker run --name aws -p 5000:5000 -e AWS_ACCESS_KEY_ID=AKIASGW66NBFMUM3I5NS
# -e AWS_SECRET_ACCESS_KEY=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 
# -e AWS_DEFAULT_REGION=us-east-1 aws_boto 

# For outside localhost-
                #1.  if __name__ == '__main__':
                #    #adding environment port
                #     port = int(os.environ.get('PORT', 5000))
                #     app.run(debug=True, host='0.0.0.0', port=port)


                #2.  # ec2 = boto3.client('ec2',
                #                 region_name="",
                #                   access_key=<key>,
                #                         secret=<secret>)

#Run pm2 in ec2:-
# pm2 start main.py --interpreter /usr/bin/python3

# ---------------------------------