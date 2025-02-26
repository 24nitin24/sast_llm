# Code Security Scanner

## Overview

The Code Security Scanner is a web-based application that allows users to scan Python code and architecture diagrams (images) for security vulnerabilities and compliance issues. It leverages the Ollama model to perform security audits, threat modeling, architecture overviews, developer questions, and Governance, Risk, and Compliance (GRC) analysis. The application provides a user-friendly interface to upload files, enter code, and view detailed findings in Markdown format.

This project is built with Flask, SQLAlchemy, and JavaScript, and it’s designed to run on a local server with integration to Ollama for AI-powered analysis.

## Features

- Code Scanning: Upload Python files or enter code to perform security audits, identifying vulnerabilities like SQL injection, sensitive data exposure, and unsafe function usage.
- Image Scanning: Upload architecture diagrams to generate threat models, architecture overviews, developer security questions, and GRC compliance analysis.
- Findings Management: View, delete, and manage scan results in a "Findings" tab, with results rendered in Markdown for readability.
- User Authentication: Secure user authentication with login, signup, and logout functionality for teams and projects.
- Team and Project Management: Create teams, manage projects, and assign users to teams for collaborative scanning.
- Real-Time Updates: Dynamic fetching of scan results via AJAX, with popup notifications for scan status.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.9+
- Flask: `pip install flask`
- Flask-Login: `pip install flask-login`
- Flask-SQLAlchemy: `pip install flask-sqlalchemy`
- Flask-Migrate: `pip install flask-migrate`
- Werkzeug: `pip install werkzeug`
- Jinja2: (Included with Flask)
- Requests: `pip install requests` (for Ollama integration)
- Marked.js: Included via CDN in `project_detail.html` (no installation needed for client-side use)
- jQuery: Included via CDN in `project_detail.html` (no installation needed for client-side use)
- Tailwind CSS: Included via CDN in `project_detail.html` (no installation needed for client-side use)
- SQLite: Included with Python (used for the database)
- Ollama: Running locally at `http://localhost:11434/api/generate` (ensure the model server is operational)

## Installation

Clone the Repository: `git clone <your-repository-url>`; `cd code-security-scanner`

Create a Virtual Environment: `python -m venv venv`; `source venv/bin/activate` (On Windows use `venv\Scripts\activate`)

Install Dependencies: `pip install -r requirements.txt`; Create a `requirements.txt` file with the following content: `flask`, `flask-login`, `flask-sqlalchemy`, `flask-migrate`, `werkzeug`, `requests`

Set Up the Database: Ensure `app.db` is created in the project root directory. Run the following to initialize the database: `flask db init` (Only needed once for Flask-Migrate); `flask db migrate` (Generate migration scripts); `flask db upgrade` (Apply migrations); Alternatively, run the application with `python app.py`, and it will create the database automatically with `db.create_all()`.

Start Ollama: Ensure Ollama is running locally at `http://localhost:11434/api/generate`. Follow the Ollama setup instructions to install and start the server with your desired model: `ollama pull llama3` (Pull a specific model, e.g., llama3); `ollama run llama3` (Start the model server); Verify the server is running by accessing `http://localhost:11434` in your browser or using `curl`.

Run the Application: `python app.py`; Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

Sign Up and Log In: Visit `/signup` to create a new user account; Log in at `/login` with your credentials to access the dashboard.

Create Teams and Projects: On the dashboard (`/dashboard`), use the "Create Team" form to create a team; Navigate to the team detail page (`/team/<team_id>`), use the "Create Project" form to create projects within the team.

Scan Code or Images: Go to a project detail page (`/project/<project_id>`); Code Scans: Select "Upload Python File" to upload a `.py` file or "Enter Code" to paste Python code; Click "Scan" to analyze the code for security vulnerabilities; Image Scans: Select "Upload Image" to upload an architecture diagram; Choose an analysis type: "Threat Modeling," "Architecture Overview," "Developer Questions," or "GRC and Compliance"; Click "Analyze" to generate findings.

View Findings: Switch to the "Findings" tab on the project page to view scan results; Results are displayed in Markdown format, sorted by creation date (newest first); Use the "Delete" button to remove individual scan results.

## Project Structure


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
├── app.db             # SQLite database file
├── requirements.txt    # Python dependencies
└── README.md          # This documentation


## Configuration

- Secret Key: Update `app.config['SECRET_KEY']` in `app.py` with a secure random string.
- Upload Folder: Ensure the `uploads/` directory exists or is created automatically by `app.py`.
- Ollama URL: Ensure Ollama is running at `http://localhost:11434/api/generate`. Update the URL in `run_llava_job.py` if it’s hosted elsewhere.

## Contributing

We welcome contributions to improve the Code Security Scanner! To contribute:

Fork the repository.
Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name`
Make your changes and commit them with descriptive messages: `git commit -m "Add feature: GRC compliance scanning"`
Push to your fork and submit a pull request.


## Acknowledgments

- Ollama: For providing the AI model used for scanning and analysis.
- Flask Community: For the robust web framework.
- Open Source Contributors: For tools like Tailwind CSS, jQuery, and Marked.js.

## Contact

For questions or issues, please open an issue on GitHub or contact the maintainers at [your-email@example.com](mailto:your-email@example.com).
