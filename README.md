# Code Security Scanner

## Overview

The Code Security Scanner is a web-based application that allows users to scan Python code and architecture diagrams (images) for security vulnerabilities and compliance issues. It leverages the Ollama model to perform security audits, threat modeling, architecture overviews, developer questions, and Governance, Risk, and Compliance (GRC) analysis. The application provides a user-friendly interface to upload files, enter code, and view detailed findings in Markdown format.

This project is built with Flask, SQLAlchemy, and JavaScript, and it’s designed to run on a local server with integration to Ollama for AI-powered analysis.

## Features

- **Code Scanning**: Upload Python files or enter code to perform security audits, identifying vulnerabilities like SQL injection, sensitive data exposure, and unsafe function usage.
- **Image Scanning**: Upload architecture diagrams to generate threat models, architecture overviews, developer security questions, and GRC compliance analysis.
- **Findings Management**: View, delete, and manage scan results in a "Findings" tab, with results rendered in Markdown for readability.
- **User Authentication**: Secure user authentication with login, signup, and logout functionality for teams and projects.
- **Team and Project Management**: Create teams, manage projects, and assign users to teams for collaborative scanning.
- **Real-Time Updates**: Dynamic fetching of scan results via AJAX, with popup notifications for scan status.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.9+**
- **Flask**: `pip install flask`
- **Flask-Login**: `pip install flask-login`
- **Flask-SQLAlchemy**: `pip install flask-sqlalchemy`
- **Flask-Migrate**: `pip install flask-migrate`
- **Werkzeug**: `pip install werkzeug`
- **Jinja2**: (Included with Flask)
- **Requests**: `pip install requests` (for Ollama integration)
- **Marked.js**: Included via CDN in `project_detail.html` (no installation needed for client-side use)
- **jQuery**: Included via CDN in `project_detail.html` (no installation needed for client-side use)
- **Tailwind CSS**: Included via CDN in `project_detail.html` (no installation needed for client-side use)
- **SQLite**: Included with Python (used for the database)
- **Ollama**: Running locally at `http://localhost:11434/api/generate` (ensure the model server is operational)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <your-repository-url>
   cd code-security-scanner
