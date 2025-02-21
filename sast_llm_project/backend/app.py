from backend import create_app, db
from flask import render_template, redirect, url_for, session, request, flash, jsonify
from backend.models import Project, User
from flask_ckeditor import CKEditor
import markdown

app = create_app()
ckeditor = CKEditor(app)

app.config["CKEDITOR_PKG_TYPE"] = "full"  # Enable full CKEditor package

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    # Handle project creation
    if request.method == "POST":
        project_name = request.form.get("project_name")
        project_description = request.form.get("description")
        team_members = request.form.get("team_members")
        deadline = request.form.get("deadline")
        priority = request.form.get("priority")
        category = request.form.get("category")
        
        if project_name:
            new_project = Project(
                name=project_name, 
                description=project_description, 
                team_members=team_members, 
                deadline=deadline,
                priority=priority,
                category=category
            )
            db.session.add(new_project)
            db.session.commit()
            return redirect(url_for("dashboard"))
    
    projects = Project.query.all()
    return render_template("dashboard.html", user=session.get("user"), projects=projects)

@app.route("/project/<int:project_id>", methods=["GET"])
def view_project(project_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    project = Project.query.get_or_404(project_id)
    markdown_description = markdown.markdown(project.description or "")
    
    return render_template("project_view.html", project=project, markdown_description=markdown_description)

@app.route("/project/<int:project_id>/edit", methods=["GET", "POST"])
def edit_project(project_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    project = Project.query.get_or_404(project_id)
    
    if request.method == "POST":
        project.description = request.form.get("description")
        project.team_members = request.form.get("team_members")
        project.deadline = request.form.get("deadline")
        project.priority = request.form.get("priority")
        project.category = request.form.get("category")
        
        file = request.files.get("image")
        if file:
            file.save(f"backend/static/uploads/{file.filename}")
            project.image_path = f"uploads/{file.filename}"
        
        db.session.commit()
        return jsonify({"message": "Changes saved successfully!"})
    
    return render_template("project_creation.html", project=project)

@app.route("/project/<int:project_id>/delete", methods=["POST"])
def delete_project(project_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    
    return jsonify({"message": "Project deleted successfully!"})

@app.route("/auth/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        
        if User.query.filter_by(email=email).first():
            flash("Email already registered!", "danger")
        else:
            new_user = User(username=username, email=email, password_hash=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully! Please log in.", "success")
            return redirect(url_for("auth.login"))
    
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)