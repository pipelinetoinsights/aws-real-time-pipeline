# Real-Time IoT Temperature Pipeline on AWS

This project demonstrates how to build a real-time data processing pipeline using managed AWS services with infrastructure provisioned via Terraform.

It simulates multiple IoT devices sending temperature readings and processes them in near real-time. The latest reading from each device is stored in Amazon DynamoDB using a Lambda function triggered by Amazon Kinesis Data Stream.

## Prerequisites

- Python 3.8+
- AWS CLI configured with a valid profile
- Terraform v1.3+ installed
- A verified AWS account

## Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:pipelinetoinsights/aws-real-time-pipeline.git
cd aws-real-time-pipeline
```

### 2. Deploy AWS Resources with Terraform

```bash
cd terraform/
terraform init
terraform apply
```

### 3. Simulate Real-Time Data

Back in the project root, install boto3 and run the simulator:

```bash
pip install boto3
python simulate_temperature.py
```

This will start sending one event per second to Kinesis.

### 4. Monitor and View Results

- CloudWatch Logs → Lambda function logs each received event

- DynamoDB Console → See latest readings for each device in the table explorer

### 5. Cleanup

When you're done testing, you can destroy all resources with:

```bash
cd terraform/
terraform destroy
```