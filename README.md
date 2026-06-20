# SECP3843: Special Topic in Data Engineering

Welcome to my GitHub E-Portfolio for the **SECP3843 - Special Topic in Data Engineering** course (Semester II, 2025/2026), Faculty of Computing, Universiti Teknologi Malaysia (UTM). 

This repository serves as a comprehensive digital collection of my academic coursework, showcasing my learning progression, technical achievements, and hands-on experience in building modern data architectures. The projects enclosed demonstrate a wide spectrum of data engineering disciplines, from cloud-based ETL pipelines and big data processing to artificial intelligence and system design.

---

## 👨‍💻 About the Authors & Team
While this E-Portfolio is an individual submission, the projects within were collaboratively developed alongside my teammates in **Group 17** under the supervision of **Dr. Aryati Binti Bakri**.
*   **Choh Jing Yi** (A23CS0296)
*   **Tan Zhi Ming** (A23CS0189)
*   **Lau Yan Kai** (A23CS0098)

---

## 📁 Repository Contents (Assignments & Tutorials)

Below is an overview of the tutorials and academic assignments contained in this repository. Navigate to their respective folders to view the full documentation, code, and detailed markdown reports.

### 📝 [Assignment 1: Academic Writing (Tutorial Article)](./Tutorial Article  PT. MPM Business Intelligence System)
*   **Topic:** Conceptualizing a Business Intelligence (BI) System for PT. MPM.
*   **Summary:** Authored an academic article designing a 5-layer BI architecture to solve performance monitoring issues for a packaging manufacturing company.
*   **Key Skills:** Requirements gathering (User Stories), Entity Relationship Diagram (ERD) design, Star Schema multidimensional modeling, and translating business KPIs into technical data warehouse requirements.

### ☁️ [Tutorial 1: Microsoft Azure End-to-End Pipeline](./Tutorial 1 Microsoft Azure)
*   **Topic:** Cloud Data Engineering & Analytics.
*   **Summary:** Built a complete ETL pipeline to extract `AdventureWorks` SQL data into the cloud to analyze customer gender demographics and product dependencies. 
*   **Key Skills:** Implemented a Medallion Architecture (Bronze, Silver, Gold layers) using Azure Data Lake Storage Gen2, Azure Data Factory, Databricks (PySpark), Synapse Analytics, and Microsoft Power BI.

### 🚀 [Tutorial 2: Apache Spark Data Warehousing](./Tutorial 2 PySpark)
*   **Topic:** Big Data Processing & Star Schema Architecture.
*   **Summary:** Processed 2.2 GB of Brazilian school census data using distributed computing, transformed it into optimized Parquet files, and loaded it into a containerized PostgreSQL data warehouse.
*   **Key Skills:** PySpark DataFrame manipulations, explicit type casting, Docker containerization, JDBC database connections, and managing Windows-specific Hadoop/Spark environments.

### 🧠 [Tutorial 3: AI Algorithm (Image Classification)](./Tutorial 3 AI Algorithm)
*   **Topic:** Deep Learning with Convolutional Neural Networks (CNN).
*   **Summary:** Developed and evaluated machine learning models to classify the CIFAR-10 image dataset using TensorFlow and Keras.
*   **Key Skills:** Transitioned from a baseline Artificial Neural Network (ANN) to an enhanced CNN, significantly improving accuracy from ~48% to ~85% by implementing deep architectures, Batch Normalization, Dropout Regularization, and Data Augmentation. 

### 🤖 [Tutorial 4: Generative AI-Assisted ETL](./Tutorial 4 Generative AI)
*   **Topic:** AI Agents in Pipeline Automation.
*   **Summary:** Utilized Generative AI prompts to build an automated ETL pipeline that extracts real-time meteorological data from WeatherAPI.com and loads it into a Firebase Firestore document database.
*   **Key Skills:** Prompt engineering, API integration, flattening highly nested JSON responses into NoSQL-friendly formats, and scheduling cron jobs for continuous data ingestion.

---

## 💡 Overall Subject Reflection

Completing the **Special Topic in Data Engineering** course has profoundly transformed my understanding of how modern data ecosystems operate. Before this course, my perspective on data was largely limited to writing simple queries on static databases. Now, I understand that data engineering is the critical infrastructure that powers all modern business intelligence and artificial intelligence.

**Key Takeaways:**
1.  **Architectural Thinking:** Through the PT. MPM Article and the Azure tutorial, I learned that raw data is useless without structure. Mastering the Medallion Architecture and Star Schemas taught me how to logically step data from chaotic raw formats into clean, business-ready insights. 
2.  **Scalability & Big Data:** The Apache Spark project was a major turning point. Watching a 2.2 GB CSV file compress down to a highly optimized 420 MB Parquet file while actually speeding up query times highlighted the necessity of distributed computing and modern file formats.
3.  **The Intersection of AI and Engineering:** Tutorials 3 and 4 demonstrated that AI is both a *product* of data engineering (requiring massive, clean datasets to train CNNs) and a *tool* for data engineers (using AI agents to write boilerplate API extraction code). 
4.  **Resilience in Troubleshooting:** Across all projects, from bypassing UTM firewall restrictions in Azure to configuring `winutils.exe` for local Hadoop environments, I learned that a successful data engineer must possess robust system administration and debugging skills.

**Moving Forward:**
I plan to take the skills acquired in this subject—particularly PySpark, cloud orchestration, and AI-assisted automation—and apply them to real-time streaming architectures. I am excited to continue building pipelines that not only describe historical data but use machine learning to predict future trends.