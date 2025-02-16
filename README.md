# akhomelab

## Overview

akhomelab is my self-hosted cloud-based homelab designed for:

- **Analytics**: ETL pipelines, dashboards, BI, and reporting
- **Automation**: CI/CD, workflow orchestration, and scripting
- **ML & AI**: Self-hosted models, experimentation, and AI services

## Repository Structure
```
akhomelab/
│── infrastructure/       # Infrastructure as Code (Terraform, Ansible, etc.)
│── automation/           # CI/CD pipelines, scripts, workflow automation
│── analytics/            # ETL scripts, dashboards, reporting
│── ml-ai/                # ML models, AI services, experimentation
│── notebooks/            # Jupyter notebooks for analytics & ML experiments
│── python/               # Scripts
│── .github/workflows/    # GitHub Actions for automation
│── docker-compose.yml    # Docker Compose setup for services
│── README.md             # Project overview & setup instructions
│── docs/                 # Documentation, setup guides, architecture details
```

## Getting Started
### 1️⃣ Prerequisites
Ensure you have the following installed:
- **Docker** & **Docker Compose**
- **Git**

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/AymanKhalissi/akhomelab.git
cd akhomelab
```

### 3️⃣ Start the Services
Run the following command to start all containers:
```sh
docker-compose up -d
```

### 4️⃣ Access Services
- **PostgreSQL**: `localhost:5432`
- **Apache Airflow**: `http://localhost:8080`
- **Jupyter Notebook**: `http://localhost:8888`

## Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.

## License
This project is open-source under the MIT License.

