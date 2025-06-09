# Vehicle Insurance Data Pipeline 🚗 

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange)](https://scikit-learn.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Latest-brightgreen)](https://www.mongodb.com/)
[![AWS](https://img.shields.io/badge/AWS-S3-yellow)](https://aws.amazon.com/s3/)

## 📋 Project Overview

A robust MLOps pipeline for predicting vehicle insurance cross-sell opportunities. This project implements a complete end-to-end machine learning pipeline with real-time prediction capabilities, automated model training, and cloud integration.

## 🎯 Key Features

- **End-to-End MLOps Pipeline**: Automated data ingestion, validation, transformation, and model training
- **Real-time Predictions**: FastAPI-powered REST API for instant predictions
- **Cloud Integration**: MongoDB for data storage and AWS S3 for model registry
- **Advanced Data Processing**: SMOTEENN for handling imbalanced datasets
- **Model Monitoring**: Continuous evaluation and automated model updates
- **Beautiful Web Interface**: User-friendly interface for predictions and model training

## 🏗️ Architecture

```
src/
├── components/          # Core ML Pipeline Components
├── constants/          # Configuration Constants
├── entity/            # Data Classes and Schemas
├── pipeline/          # Training and Prediction Pipelines
└── utils/             # Utility Functions

templates/            # Web Interface Templates
static/              # Static Assets
config/              # Configuration Files
logs/                # Application Logs
```

## 🔧 Technical Stack

- **Framework**: FastAPI
- **ML Libraries**: scikit-learn, imbalanced-learn
- **Data Processing**: pandas, numpy
- **Database**: MongoDB
- **Cloud Storage**: AWS S3
- **UI**: HTML/CSS with Jinja2 Templates
- **Containerization**: Docker

## 🚀 Features in Detail

### ML Pipeline Components

1. **Data Ingestion**
   - MongoDB integration for data sourcing
   - Automated train-test splitting
   - Feature store implementation

2. **Data Validation**
   - Schema validation
   - Data drift detection
   - Data quality checks

3. **Data Transformation**
   - Automated feature engineering
   - SMOTEENN for imbalanced data handling
   - Standardization and MinMax scaling
   - Custom preprocessing pipeline

4. **Model Training**
   - Random Forest Classifier implementation
   - Hyperparameter optimization
   - Cross-validation

5. **Model Evaluation**
   - Performance metrics tracking
   - Model comparison with production version
   - Automated acceptance criteria

6. **Model Deployment**
   - AWS S3 model registry
   - Versioning and rollback capability
   - Zero-downtime updates

## 📊 Model Features

The model predicts insurance cross-sell opportunities using the following features:
- Gender
- Age
- Driving License
- Region Code
- Previous Insurance
- Vehicle Age
- Vehicle Damage
- Annual Premium
- Policy Sales Channel
- Vintage

## 🛠️ Setup and Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/Vehicle-Insurance-Data-Pipeline.git
cd Vehicle-Insurance-Data-Pipeline
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up environment variables
```bash
MONGODB_URL=your_mongodb_url
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
```

4. Run the application
```bash
uvicorn app:app --host 0.0.0.0 --port 5000
```

## 🌐 API Endpoints

- `GET /`: Web interface for predictions
- `POST /`: Submit prediction request
- `GET /train`: Trigger model training pipeline

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

Your Name - [LinkedIn](https://linkedin.com/in/yourprofile) - your.email@example.com

## 🙏 Acknowledgments

- Thanks to all contributors who helped shape this project
- Special thanks to the open-source community for the amazing tools and libraries

---
⭐ Star this repository if you find it helpful!
