# 🚀 Outreach Pipeline - Automated B2B Lead Generation System

## 📌 Overview

Outreach Pipeline is an automated lead generation system that discovers relevant companies and extracts professional contacts from those companies using real-world APIs.

Instead of manually searching for companies and decision-makers, this project automates the complete workflow from company discovery to lead generation and CSV export.

The system takes a seed company domain as input, finds similar companies using Ocean.io, discovers professionals associated with those companies using Prospeo, and exports the generated leads into a structured CSV file.

---

# 🎯 Problem Statement

Sales teams, recruiters, agencies, and growth teams spend significant time:

* Finding relevant companies
* Identifying decision-makers
* Collecting professional profiles
* Organizing leads manually

This process is repetitive, time-consuming, and difficult to scale.

---

# 💡 Solution

This project automates the lead generation process by integrating multiple APIs into a single pipeline.

Input a company domain:

```text
hubspot.com
```

The system automatically:

```text
Find Similar Companies
        ↓
Find People Associated With Those Companies
        ↓
Extract Professional Information
        ↓
Generate Structured Lead List
        ↓
Export CSV
```

---

# 🏗️ System Architecture

```text
                ┌───────────────────┐
                │ User Input Domain │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │    Ocean API      │
                │ Company Discovery │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Similar Companies │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │   Prospeo API     │
                │  People Search    │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Contact Extraction│
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Data Processing   │
                │ Deduplication     │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │   CSV Export      │
                └───────────────────┘
```

---

# ✨ Features

### Company Discovery

* Search companies using Ocean API
* Find lookalike companies from a seed domain
* Extract company names and domains

### Contact Discovery

* Search professionals using Prospeo API
* Extract:

  * Full Name
  * Job Title
  * LinkedIn URL
  * Person ID

### Data Processing

* Automatic deduplication
* Error handling
* Logging
* CSV generation

### Output

Generated leads are exported to:

```text
output/leads.csv
```

---

# 📂 Project Structure

```text
outreach-pipeline/
│
├── src/
│   ├── main.py
│   ├── ocean.py
│   ├── prospeo.py
│   └── config.py
│
├── output/
│   └── leads.csv
│
├── logs/
│   └── run.log
│
├── requirements.txt
├── README.md
└── .env.example
```

---

# 🛠️ Technologies Used

| Technology  | Purpose               |
| ----------- | --------------------- |
| Python      | Core Development      |
| Ocean API   | Company Discovery     |
| Prospeo API | Contact Discovery     |
| Pandas      | Data Processing       |
| Requests    | API Communication     |
| dotenv      | Environment Variables |

---

# 📊 Sample Workflow

### Input

```text
hubspot.com
```

### Companies Discovered

```text
HubSpot
LeadSquared
Thryv
Portalcloner
Beyond Creative Works
```

### Leads Generated

```text
Company, Name, Title, LinkedIn

LeadSquared,
John Doe,
VP Sales,
linkedin.com/in/johndoe

Thryv,
Jane Smith,
Marketing Director,
linkedin.com/in/janesmith
```

### Output

```text
output/leads.csv
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
OCEAN_API_KEY=your_ocean_api_key
PROSPEO_API_KEY=your_prospeo_api_key
```

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/yourusername/outreach-pipeline.git
cd outreach-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run project:

```bash
python src/main.py
```

---

# 📈 Results

The pipeline successfully:

* Discovers similar companies from a seed domain
* Retrieves professional profiles
* Generates structured lead lists
* Exports leads automatically
* Handles API failures gracefully
* Removes duplicate contacts

Example execution:

```text
Input Domain: hubspot.com

Companies Found: 10
Leads Generated: 30

Output:
output/leads.csv
```

---

# 🚀 Future Improvements

* Email enrichment
* Automated outreach campaigns
* CRM integration
* Lead scoring
* Web dashboard
* Scheduled lead generation
* AI-powered lead qualification

---

# 👨‍💻 Author

Somnath

Built as a practical outreach automation project demonstrating API integration, data processing, workflow automation, and lead generation using real-world SaaS platforms.
