# 📜 Code Security Scanner  
![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?style=flat&logo=python) ![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=flat&logo=flask) ![Ollama](https://img.shields.io/badge/Ollama-AI-red?style=flat&logo=ai) ![License](https://img.shields.io/badge/License-MIT-green.svg)

🔍 **AI-Powered Web Application for Security Scanning of Python Code & Architecture Diagrams**  
🚀 **Detect security vulnerabilities, perform threat modeling, and ensure GRC compliance with AI**  
💻 **Designed for developers, security engineers, and teams to analyze code and system architectures**  

---

## 🏆 Features
- 🔹 **Code Scanning**: Analyze Python code for **security vulnerabilities**, including:
  - SQL Injection  
  - Sensitive Data Exposure  
  - Insecure Function Usage  
  - Code Injection Risks  
- 🔹 **Image Scanning**: Upload **architecture diagrams** for:
  - Threat Modeling  
  - Architecture Overview  
  - Developer Security Questions  
  - GRC Compliance Analysis  
- 🔹 **Findings Management**: View, delete, and manage scan results in **Markdown format**.  
- 🔹 **User Authentication**: Secure **login, signup, and logout** for team-based scanning.  
- 🔹 **Team & Project Management**: Create **teams, manage projects, and collaborate** on security scans.  
- 🔹 **Real-Time Updates**: Dynamic **AJAX-based scanning** with **instant notifications**.  
- 🔹 **Multi-File Scanning Support**: Upload **multiple files** at once for batch security analysis.  
- 🔹 **REST API for Integration**: Easily integrate with **CI/CD pipelines, security tools, and DevSecOps workflows**.  

---

## 🛠️ Prerequisites
Ensure you have the following installed before running the application:

```bash
pip install flask flask-login flask-sqlalchemy flask-migrate werkzeug requests
```

### Additional Requirements:
- **Python 3.9+**  
- **SQLite** (included with Python)  
- **Ollama** (AI Model) running at `http://localhost:11434/api/generate`  
- **Front-end Libraries** (Included via CDN in `project_detail.html`):
  - jQuery
  - Tailwind CSS
  - Marked.js  

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <your-repository-url>
cd code-security-scanner
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scriptsctivate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up the Database
```bash
flask db init       # One-time setup
flask db migrate    # Generate migration scripts
flask db upgrade    # Apply migrations
```
Alternatively, run `python app.py`, and the database will be created automatically.

### 5️⃣ Start Ollama AI
```bash
ollama pull llama3   # Pull AI model
ollama run llama3    # Start the Ollama AI server
```
Verify the server:  
Check `http://localhost:11434` in the browser or use:
```bash
curl http://localhost:11434/api/generate
```

### 6️⃣ Run the Application
```bash
python app.py
```
Open in Browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)  

---

## 📌 Usage Guide
### 🔑 1. User Authentication
- Visit `/signup` to create an account.  
- Log in at `/login` to access the **dashboard**.

### 📁 2. Team & Project Management
- Create teams using the **"Create Team"** feature on the dashboard (`/dashboard`).
- Navigate to **Team Page (`/team/<team_id>`)** to create projects.

### 🔍 3. Security Scanning
- **Code Scanning**: Upload **Python files** or paste **code** for AI-driven security analysis.  
- **Image Scanning**: Upload **architecture diagrams** for:
  - **Threat Modeling**  
  - **Architecture Overview**  
  - **Developer Security Questions**  
  - **GRC & Compliance Analysis**  

### 📜 4. Findings & Reports
- Navigate to the **"Findings" tab** in a project.  
- Results are displayed in **Markdown format** with severity levels.  
- **Delete findings** when no longer needed.  
- **Export findings** as **JSON, CSV, or PDF** reports.

---

## 📂 Project Structure
```
code-security-scanner/
├── app.py              # Flask application logic, routes, and models
├── run_llava_job.py    # Ollama integration for scanning code and images
├── templates/          # HTML templates
│   ├── project_detail.html  # Main UI for scanning and findings
│   ├── dashboard.html       # User dashboard
│   ├── team_detail.html     # Team management
│   ├── index.html           # Landing page
│   ├── login.html           # Login page
│   ├── signup.html          # Signup page
│   └── edit_project.html    # Project editing
├── uploads/            # Directory for uploaded files (code and images)
├── app.db              # SQLite database file
├── requirements.txt    # Python dependencies
└── README.md           # This documentation
```

---

## ⚙️ Configuration
- **Secret Key**: Update `app.config['SECRET_KEY']` in `app.py` with a secure random string.  
- **Uploads**: Ensure `uploads/` directory exists or is automatically created.  
- **Ollama URL**: If running on a different server, update `run_llava_job.py`.  

---

## 🔌 REST API Endpoints
This project provides REST APIs for integration with DevSecOps workflows.

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/scan/code` | Upload Python code for security analysis |
| `POST` | `/api/scan/image` | Upload an architecture diagram for AI-based analysis |
| `GET`  | `/api/findings` | Retrieve previous scan results |
| `DELETE` | `/api/findings/<id>` | Delete a specific finding |

For more details, refer to the API documentation.

---

## 🤝 Contributing
We welcome contributions! To contribute:

1. Fork the repository.  
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make changes & commit:
   ```bash
   git commit -m "Add feature: GRC compliance scanning"
   ```
4. Push to your fork & submit a pull request.

---

## 💡 Acknowledgments
**Powered by**:
- [Ollama](https://ollama.com/) - AI model for security analysis  
- [Flask](https://flask.palletsprojects.com/) - Web framework  
- [Tailwind CSS](https://tailwindcss.com/) - UI styling  
- [jQuery](https://jquery.com/) - Frontend interactions  
- [Marked.js](https://marked.js.org/) - Markdown rendering  

---

## 📞 Contact
For issues or questions, open a GitHub issue or email:  
📧 [your-email@example.com](mailto:your-email@example.com)

---

🔥 **Happy Coding! Secure Your Apps with Code Security Scanner!** 🛡️💻
