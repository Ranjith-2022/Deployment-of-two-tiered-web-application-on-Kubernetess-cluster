
# Deployment of 2-tiered web application to managed K8s cluster on Amazon EKS, with pod auto-scaling and deployment automation 

## Objective

The objective of the Final Project is to combine everything we learned so far in the scope of CLO835 about building, hosting, and deploying a containerized application using Kubernetes orchestration tool and Docker. In this assignment, you will enhance an existing web application backed by MySQL DB and add configuration, security, and persistent data features. You will build the Docker image of the enhanced application automatically using GitHub Actions and publish it to the private Docker registry hosted by Amazon ECR. You will create an Amazon EKS cluster to host the application. To deploy the application to the Amazon EKS cluster, you will create all the relevant manifests and deploy them using the kubectl client.


## Architecture 

![image](https://github.com/Ranjith-2022/Deployment-of-two-tiered-web-application-on-Kubernetess-cluster/assets/114111480/bbbdd1d7-74ac-4611-a43c-ec9b4ee781a8)

## Steps

1. **Enhance Existing Web Application**: Modify and enhance the existing web application, including adding configuration, security, and persistent data features.

2. **Build Docker Image**: Configure GitHub Actions to automatically build the Docker image of the enhanced application on every push to the main branch.

3. **Publish to Amazon ECR**: Set up Amazon ECR repository and configure GitHub Actions to push the built Docker image to the private Docker registry.

4. **Create Amazon EKS Cluster**: Use Amazon EKS to create a Kubernetes cluster where the application will be deployed.

5. **Create Manifests**: Write Kubernetes manifests (Deployment, Service, PersistentVolume, PersistentVolumeClaim, ConfigMap, Secret) for deploying the enhanced application and MySQL database.

6. **Deploy Application**: Use kubectl client to apply the Kubernetes manifests and deploy the application to the Amazon EKS cluster.

## Services and Tools Used

- **GitHub Actions**: Automate the build and publishing of the application’s image.
- **Docker CLI**: Build the image, test it locally, and publish it to Amazon ECR.
- **Amazon ECR**: Securely store your Docker images.
- **Amazon EKS**: Host your application.
- **Amazon EBS**: Provide persistent storage for the MySQL database.
- **Amazon S3**: Store images used by your application as a background.
- **AWS IAM**: Grant application access to your private Amazon S3 bucket.
- **Cloud9 IDE** (or your local environment): Develop your application and build container images.
- **kubectl**: Work with your Amazon EKS cluster.
- **eksctl**: Create and delete your cluster.

