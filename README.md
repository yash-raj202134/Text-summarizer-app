# Text Summarizer App

The Text Summarizer App uses the advanced Google Pegasus SamSum model for effective and efficient text summarization. This project is integrated with AWS services for CI/CD deployment, offering a streamlined process for creating, building, and launching the app using Docker and AWS services. It includes a Conda environment setup for seamless local operations and configurations.

## Features

- **Google Pegasus SamSum Model**: Leverages state-of-the-art text summarization capabilities.
- **AWS Integration**: Streamlines deployment with AWS services.
- **CI/CD Pipeline**: Automates deployment and updates for the app.
- **Conda Environment**: Simplifies dependency management and project setup.
- **Docker**: Supports containerization for consistent application performance.

## Workflows

1. **Update `config.yaml`**: Customize configuration settings.
2. **Update `params.yaml`**: Modify parameters for the summarization model.
3. **Update Entity**: Customize data entities as needed.
4. **Update Configuration Manager**: Modify `src/config` for configurations.
5. **Update Components**: Update various app components for new features.
6. **Update Pipeline**: Modify pipeline configurations as needed.
7. **Update `main.py`**: Implement changes in the main application file.
8. **Update `app.py`**: Update the application entry point.

## How to Run

1. **Clone the Repository**: 
    ```bash
    git clone https://github.com/yash-raj202134/Text-summarizer-app.git
    ```
2. **Create and Activate Conda Environment**:
    ```bash
    conda create -n summary python=3.8 -y
    conda activate summary
    ```
3. **Install Requirements**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the App**:
    ```bash
    python app.py
    ```

After running the app, open your local host and port.

## AWS CI/CD Deployment with GitHub Actions

1. **Login to AWS Console**.
2. **Create IAM User for Deployment**:
    - **EC2 Access**: Provides access to the virtual machine.
    - **ECR**: Allows use of Elastic Container Registry for storing Docker images.
    - **Policies**:
        - `AmazonEC2ContainerRegistryFullAccess`
        - `AmazonEC2FullAccess`
3. **Create ECR Repository**: Save the URI for the repository (e.g., `566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s`).
4. **Create EC2 Machine (Ubuntu)**.
5. **Install Docker in EC2 Machine**:
    - Optional:
        ```bash
        sudo apt-get update -y
        sudo apt-get upgrade
        ```
    - Required:
        ```bash
        curl -fsSL https://get.docker.com -o get-docker.sh
        sudo sh get-docker.sh
        sudo usermod -aG docker ubuntu
        newgrp docker
        ```
6. **Configure EC2 as Self-Hosted Runner**: Follow GitHub settings for actions and runners to set up the self-hosted runner.
7. **Setup GitHub Secrets**:
    - `AWS_ACCESS_KEY_ID`
    - `AWS_SECRET_ACCESS_KEY`
    - `AWS_REGION` (e.g., `us-east-1`)
    - `AWS_ECR_LOGIN_URI` (e.g., `566373416292.dkr.ecr.ap-south-1.amazonaws.com`)
    - `ECR_REPOSITORY_NAME` (e.g., `simple-app`)

## Author

Yash Raj  
Data Scientist  
Email: yashraj3376@gmail.com
