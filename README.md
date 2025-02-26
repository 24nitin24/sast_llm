# 📜 Code Security Scanner  
![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?style=flat&logo=python) ![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=flat&logo=flask) ![Ollama](https://img.shields.io/badge/Ollama-AI-red?style=flat&logo=ai) ![License](https://img.shields.io/badge/License-MIT-green.svg)

🔍 **Scan Python code & architecture diagrams for security vulnerabilities and compliance issues.**  
🚀 **AI-Powered security analysis using Ollama.**  
💻 **Web-based security scanner for teams & projects.**  

---

## 🏆 Features
✅ **Code Scanning**: Analyze Python code for vulnerabilities like **SQL injection, sensitive data leaks, and unsafe functions**.  
✅ **Image Scanning**: Upload architecture diagrams for **Threat Modeling, Architecture Overview, Developer Security Questions, and GRC Compliance Analysis**.  
✅ **Findings Management**: View, delete, and manage scan results in Markdown format.  
✅ **User Authentication**: Secure **login, signup, and logout** for team-based security scans.  
✅ **Team & Project Management**: Create **teams, manage projects, and collaborate** on security scans.  
✅ **Real-Time Updates**: Dynamic **AJAX-based scanning** with **live notifications**.  

---

## 🛠️ Prerequisites
Before running the application, install the following:

\`\`\`bash
pip install flask flask-login flask-sqlalchemy flask-migrate werkzeug requests
\`\`\`

📌 **Additional Requirements**:
- **Python 3.9+**  
- **SQLite** (included with Python)  
- **Ollama** (AI Model) running at \`http://localhost:11434/api/generate\`  
- **Front-end Libraries** (Included via CDN in \`project_detail.html\`):
  - **jQuery**
  - **Tailwind CSS**
  - **Marked.js**  

---

## 🚀 Installation & Setup

### 📥 1. Clone the Repository
\`\`\`bash
git clone <your-repository-url>
cd code-security-scanner
\`\`\`

### 🔧 2. Create a Virtual Environment
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

### 📦 3. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 🏗️ 4. Set Up the Database
\`\`\`bash
flask db init       # One-time setup
flask db migrate    # Generate migration scripts
flask db upgrade    # Apply migrations
\`\`\`
Alternatively, **run \`python app.py\`**, and the database will be created automatically.

### 🤖 5. Start Ollama AI
\`\`\`bash
ollama pull llama3   # Pull AI model
ollama run llama3    # Start the Ollama AI server
\`\`\`
**Verify Server**:  
Check \`http://localhost:11434\` in the browser or use:
\`\`\`bash
curl http://localhost:11434/api/generate
\`\`\`

### 🏃 6. Run the Application
\`\`\`bash
python app.py
\`\`\`
🔗 Open in Browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)  

---

## 📌 Usage Guide
### 🔑 1. Sign Up & Log In
- Visit **\`/signup\`** to create an account.  
- Log in at **\`/login\`** to access the **dashboard**.

### 📁 2. Create Teams & Projects
- Use **"Create Team"** on the **dashboard (\`/dashboard\`)**.
- Navigate to **Team Page (\`/team/<team_id>\`)** to create projects.

### 🔍 3. Scan Code & Images
- **Code Scanning**: Upload **Python files** or paste **code** for security analysis.  
- **Image Scanning**: Upload **architecture diagrams** for:  
  🔹 **Threat Modeling**  
  🔹 **Architecture Overview**  
  🔹 **Developer Questions**
  🔹 **Code Scanning**  
  🔹 **GRC & Compliance Analysis**  

### 📜 4. View & Manage Findings
- Navigate to **"Findings" tab** in a project.  
- Results are displayed in **Markdown format**.  
- **Delete findings** when no longer needed.

---

## 📂 Project Structure
\`\`\`plaintext
code-security-scanner/
├── app.py              # Flask application logic, routes, and models
├── run_llava_job.py    # Ollama integration for scanning code and images
├── templates/          # HTML templates
│   ├── project_detail.html  # Main UI for scanning and findings
│   ├── dashboard.html       # User dashboard
│   ├── team_detail.html     # Team management
│   ├── index.html          # Landing page
│   ├── login.html          # Login page
│   ├── signup.html         # Signup page
│   └── edit_project.html   # Project editing
├── uploads/            # Directory for uploaded files (code and images)
├── app.db              # SQLite database file
├── requirements.txt    # Python dependencies
└── README.md           # This documentation
\`\`\`

---

## ⚙️ Configuration
- **Secret Key**: Update \`app.config['SECRET_KEY']\` in \`app.py\` with a secure random string.  
- **Uploads**: Ensure \`uploads/\` directory exists.  
- **Ollama URL**: If running on a different server, update \`run_llava_job.py\`.  

---

## 🤝 Contributing
We welcome contributions! To contribute:

1️⃣ **Fork the repository.**  
2️⃣ **Create a feature branch:**
   \`\`\`bash
   git checkout -b feature/your-feature-name
   \`\`\`
3️⃣ **Make changes & commit:**
   \`\`\`bash
   git commit -m "Add feature: GRC compliance scanning"
   \`\`\`
4️⃣ **Push to your fork & submit a pull request.**

---

## 💡 Acknowledgments
💙 **Powered by**:
- 🧠 **[Ollama](https://ollama.com/)** - AI model for security analysis  
- 🏗️ **[Flask](https://flask.palletsprojects.com/)** - Web framework  
- 🎨 **[Tailwind CSS](https://tailwindcss.com/)** - UI styling  
- 🔗 **[jQuery](https://jquery.com/)** - Frontend interactions  
- 📜 **[Marked.js](https://marked.js.org/)** - Markdown rendering  


---

🔥 **Happy Coding! Secure Your Apps with Code Security Scanner!** 🛡️💻
