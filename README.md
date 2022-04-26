# aws_dashboard
Creating AWS dashboard using Boto3 API
1. Clone the repository
2. Run the command- 
# pip install requirements.txt. 
3. Make sure you hve pip installed.
# Run python3 main.py
4. Build the docker image using Dockerfile with command
# docker build -t <image>:<tag>
5. Run the container using port binding and env variables-
  docker run --name <container> --rm -p 5000:5000 -it 
  -e AWS_ACCESS_KEY_ID=<key> 
  -e AWS_SECRET_ACCESS_KEY=<secret> 
  -e AWS_DEFAULT_REGION=<region>
  <image>:<tag>
    
6. Push the image to DockerHub.
