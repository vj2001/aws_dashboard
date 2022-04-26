import boto3
import os
from botocore.exceptions import ClientError
from django.shortcuts import render
from flask import Flask, redirect,render_template,request, url_for
app = Flask(__name__)

# AWS Dashboard

@app.route('/')
def index():
    return render_template('index.html')


# 1. getting all the ec2 instances

@app.route('/show')
def get_instances():
    ec2 = boto3.resource('ec2',region_name='us-east-1')
    instances= ec2.instances.all()
    if not(instances):
     return render_template("message.html",message="No Instances running. Create a instance first")

    return render_template("showInstances.html",instances=instances)

# 2. creating the ec2 instance

@app.route('/create',methods=["POST","GET"])
def create_instances():
    if request.method=='POST':
        ec2 = boto3.client('ec2',region_name='us-east-1')
        form = request.form
        image = form['image']
        type = form['type']
        group = form['group']
        ec2.run_instances(
        ImageId=image,
        MinCount=1,
        MaxCount=1,
        InstanceType=type,
        SecurityGroupIds= [group]
      )
        return render_template("message.html",message="Successfully created")
    else:
        return render_template("createInstances.html")
        
# 3. delete ec2 instances

@app.route('/terminate',methods=["POST","GET"])
def terminate_instances():
    if request.method=='POST':
        ec2 = boto3.client('ec2',region_name='us-east-1')
        form = request.form
        id = form['id']
        try:
            ec2.terminate_instances(InstanceIds=[id], DryRun=True)
        except ClientError as e:
                if 'DryRunOperation' not in str(e):
                    raise

        try:
            response = ec2.terminate_instances(InstanceIds=[id], DryRun=False)
            return render_template("message.html",message="Successfully terminated")
        except ClientError as e:
            print(e)
      
    else:
        return render_template("deleteInstances.html")

# 4. start ec2 instances

@app.route('/start',methods=["POST","GET"])
def start_instances():
    if request.method=='POST':
        ec2 = boto3.client('ec2',region_name='us-east-1')
        form = request.form
        id = form['id']
        try:
            ec2.start_instances(InstanceIds=[id], DryRun=True)
        except ClientError as e:
                if 'DryRunOperation' not in str(e):
                    raise

        try:
            response = ec2.start_instances(InstanceIds=[id], DryRun=False)
            return render_template("message.html",message="Successfully started")
        except ClientError as e:
            print(e)
      
    else:
        return render_template("startInstances.html")

# 5. stop ec2 instances

@app.route('/stop',methods=["POST","GET"])
def stop_instances():
    if request.method=='POST':
        ec2 = boto3.client('ec2',region_name='us-east-1')
        form = request.form
        id = form['id']
        try:
            ec2.stop_instances(InstanceIds=[id], DryRun=True)
        except ClientError as e:
                if 'DryRunOperation' not in str(e):
                    raise

        try:
            response = ec2.stop_instances(InstanceIds=[id], DryRun=False)
            return render_template("message.html",message="Successfully stopped")
        except ClientError as e:
            print(e)
      
    else:
        return render_template("stopInstances.html")

# 6. showing all IAM users

@app.route('/users')
def users():
        # Create IAM client
        iam = boto3.client('iam')
        users=list()
        # List users with the pagination interface
        # paginator = iam.get_paginator('list_users')
        users = iam.list_users()['Users']
        if len(users)==0:
         return render_template("message.html",message="No Users. Create a user first")

        return render_template("showUsers.html",users=users)

#7.  Creating IAM user

@app.route('/createUser',methods=["POST","GET"])
def createUser():
        if request.method == 'POST':
            # Create IAM client
            iam = boto3.client('iam')

            # Create user
            response = iam.create_user(
            UserName= request.form['name']
            )
            return render_template("message.html",message="Successfully Created User")
        else:
            return render_template('createUser.html')


#8. Get the list of S3 buckets

@app.route('/buckets')
def getBuckets():
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    if len(buckets["Buckets"])==0:
        return render_template("message.html",message="No buckets. Create a bucket first")
    
    return render_template("showBuckets.html",buckets=buckets)


if __name__ == '__main__':
    # adding environment port
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)