# AWS-EKS-Two-Tier-Project

In this project, We are going to deploy two deployments. One for frontend and other for backend.

## Some Key points to consider: -

 - We will be using AWS EKS to deploy our Kubernetes.
 - Also, We will push docker images to Dockerhub and fetch them to deploy our pods!

### Project Layout

![](https://github.com/Prashun08/AWS-EKS-Two-Tier-Project/blob/main/AWS_EKS.gif)

## Use the following commands for EKS Cluster: -

'''
 # To Create Cluster without NodeGroup
 eksctl create cluster --name eksdemo1 --region=us-east-1 --zones=us-east-1a,us-east-1b --without-nodegroup
'''
