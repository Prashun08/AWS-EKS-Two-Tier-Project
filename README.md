# AWS-EKS-Two-Tier-Project

In this project, We are going to deploy two deployments. One for frontend and other for backend.

## Some Key points to consider: -

 - We will be using AWS EKS to deploy our Kubernetes.
 - Also, We will push docker images to Dockerhub and fetch them to deploy our pods!

### Project Layout

![](https://github.com/Prashun08/AWS-EKS-Two-Tier-Project/blob/main/AWS_EKS.gif)

## Use the following commands for EKS Cluster: -

```
# To Create Cluster without NodeGroup
eksctl create cluster --name eksdemo1 \
--region=us-east-1 --zones=us-east-1a,us-east-1b --without-nodegroup

```

```

# To Create NodeGroup for the Cluster
eksctl create nodegroup --cluster=eksdemo1 \
--region=us-east-1 --name=eksdemo1-ng-public1 \
--node-type=t2.micro --nodes=2 --nodes-min=2 --nodes-max=4 --node-volume-size=20 \
--ssh-access --ssh-public-key=kube-demo \
--managed \
--asg-access --external-dns-access --full-ecr-access --appmesh-access --alb-ingress-access

```

```

# To Provide OIDC Credentials
eksctl utils associate-iam-oidc-provider \
--region us-east-1 --cluster eksdemo1 --approve

```