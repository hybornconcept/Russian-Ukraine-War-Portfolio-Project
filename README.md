# 🎯 Russian-Ukraine War Data Analysis Pipeline

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-green)

## 📋 Overview

This project implements an automated ETL (Extract, Transform, Load) pipeline that collects and processes data about the Russian-Ukraine conflict. The pipeline fetches survey data from KoboToolbox, processes it, and stores it in a PostgreSQL database for further analysis and visualization.

## 🌟 Key Features

- **Automated Data Collection**: Direct integration with KoboToolbox API
- **Data Processing**: Comprehensive data cleaning and transformation
- **Database Storage**: Structured PostgreSQL database schema
- **Casualty Tracking**: Monitors military and civilian casualties
- **Territory Analysis**: Tracks territorial changes and occupation percentages
- **Combat Metrics**: Measures combat intensity and military activities

## 🔧 Technical Architecture

```plaintext
KoboToolbox API → Python Pipeline → PostgreSQL Database
     ↓               ↓                    ↓
Raw Data       Transformation       Structured Data
```

## 📦 Prerequisites

- Python 3.9 or higher
- PostgreSQL 13 or higher
- KoboToolbox account with API access
- Required Python packages (see requirements.txt)

## 🚀 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/hybornconcept/Russian-Ukraine-War-Portfolio-Project.git
   cd Russian-Ukraine-War-Portfolio-Project
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the project root:
   ```env
   # KoboToolbox Credentials
   KOBOTOOLBOX_USERNAME=your_username
   KOBOTOOLBOX_PASSWORD=your_password

   # PostgreSQL Configuration
   PG_HOST=localhost
   PG_PORT=5432
   PG_DATABASE=Russian_Ukrain_War
   PG_USER=postgres
   PG_PASSWORD=your_password
   ```

## 💾 Database Schema

### Schema: `war_data`
### Table: `russian_ukrain_conflict`

| Column Name | Type | Description |
|------------|------|-------------|
| id | SERIAL | Primary Key |
| start | TIMESTAMP | Event start time |
| end | TIMESTAMP | Event end time |
| Enter a date | DATE | Date of record |
| Country | TEXT | Country involved |
| Event | TEXT | Type of military event |
| Oblast | TEXT | Administrative region |
| Casualties | INTEGER | Number of deaths |
| Injured | INTEGER | Number of injured |
| Captured | INTEGER | POW count |
| Civilian Casualties | INTEGER | Civilian death count |
| Combat Intensity | FLOAT | Combat intensity scale |
| Territory Status | TEXT | Current territory status |
| Total_soldiers_casualties | INTEGER | Total military casualties |

## 🔄 Pipeline Workflow

1. **Data Extraction**
   - Connects to KoboToolbox API
   - Fetches latest survey data
   - Validates response status

2. **Data Transformation**
   - Cleans raw data
   - Calculates derived metrics
   - Standardizes data formats

3. **Data Loading**
   - Creates/updates database schema
   - Loads processed data
   - Performs data integrity checks

## 🛠️ Usage

1. **Run the Pipeline**
   ```bash
   python pipeline.py
   ```

2. **Monitor Execution**
   - Check terminal output for progress
   - Verify database updates
   - Review error logs if any

## 📊 Data Visualization

*Coming Soon: Integration with visualization tools and dashboards*

## 🔐 Security Notes

- Sensitive credentials are stored in `.env` file (not tracked in git)
- Database connection uses secure authentication
- API access is authenticated and encrypted

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 👥 Author

**Hayze Concept**
- GitHub: [@hybornconcept](https://github.com/hybornconcept)

## 🙏 Acknowledgments

- KoboToolbox for providing the data collection platform
- Contributors to the open-source libraries used in this project
- The humanitarian data community

---
⭐️ Star this repository if you find it helpful!
