# Python Stress Testing 

This project is a python application where the main goal of stress testing is to identify the system's breaking point and to see how it behaves under intense load.

## Technologies Used
  - Python
  - Subprocess Module: This module is used to execute shell commands for performing stress tests.
  - Logging Module: For detailed logging of test results and error handling.
  - Twilio API: Used to send WhatsApp notifications with the stress test results.
  - Google Gemini API: Used for generating suggestions based on test outputs.
  - System Tools for Stress Testing:
      -  stress-ng: A tool to perform CPU, memory, and disk stress tests.
      -  iperf3: Used for network stress testing.
      -  sysbench: Used for MySQL stress testing.
  - Kubernetes to application scalability and reliability
  - Docker for containerization
  - Jenkins as a CI/CD tool for automating the python code when pull/push is triggered
  - Grafana for Visualization of logs
  - Prometheus for Monitoring and Logging
## Prerequisites
  - Docker installed on your machine.
  - Python environemt setup with libraries installed
  - Gemini API key configuration
  - Integrating Twilio with Whatsapp
  - MySQL database configuration
  - Kubernetes installed on your machine
  - Jenkins installed on your  machine
  - Prometheus and Grafana setup

## Getting Started

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/python-stress-testing-project.git
```

### 2. Build the Docker image:
```
docker build -t myproject . 
```
### OR

### Using docker pull:
```
docker pull sathvik1898/myproject
```
