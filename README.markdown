# BlogSphere - A Modern Blogging Platform

## Overview
BlogSphere is a sleek and modern blogging platform built as a vacation project while learning Django. It allows users to create, edit, and share blog posts, manage their profiles, and engage with the community through likes and comments. The project features a stylish dark theme with gradient elements, glassmorphism effects, and smooth animations for an enhanced user experience.

## Features
- **User Authentication**: Secure signup, login, and logout functionality.
- **Blog Management**: Create, edit, and delete blog posts with images, categories, and tags.
- **Profile Management**: Update user bio and profile picture with a glowing circular frame.
- **Engagement**: Like posts and add comments (requires login).
- **Search**: Search posts by keywords.
- **Trending Posts**: Displays posts with the most likes.
- **Stylish UI**: Dark theme with gradient navbar/buttons, glassmorphism login/signup forms, and hover animations.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite (default, can be switched to PostgreSQL or MySQL)
- **Styling**: Custom CSS with Google Fonts (Poppins), Bootstrap Icons
- **Media**: Support for image uploads for posts and profile pictures


## Default Users
The platform includes the following pre-created users for testing:
- **User IDs and Passwords**:
  - AlexHarper (Password: Blog@123)
  - SophieLaurent (Password: Blog@123)
  - LiamCarter (Password: Blog@123)
  - EmmaBrooks (Password: Blog@123)
  - NoahFletcher (Password: Blog@123)
  - RyanMitchell (Password: Blog@123)

## Admin Access
To manage the database:
- **URL**: `http://localhost:8000/admin/`
- **Username**: Purvarajsinh
- **Password**: Blog@123

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Virtualenv (optional but recommended)
- Git (optional, for cloning the repository)

## Installation and Setup
Follow these steps to set up and run BlogSphere on your local machine:

1. **Clone the Repository** (if you have Git):
   ```bash
   git clone <repository-url>
   cd blog_project
   ```
   Alternatively, download and extract the project ZIP file.

2. **Create a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   Ensure you're in the project directory (`blog_project`) and run:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is not present, install Django manually:
   ```bash
   pip install django
   ```

4. **Set Up the Database**:
   Navigate to the project directory and run migrations to set up the SQLite database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Collect Static Files**:
   The project uses custom CSS for styling. Collect static files to make them accessible:
   ```bash
   python manage.py collectstatic
   ```
   When prompted, type `yes` to overwrite existing files (if any).

6. **Create a Superuser** (optional, for admin access):
   To access the Django admin panel, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up a username, email, and password.

7. **Run the Development Server**:
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```
   Open your browser and go to `http://127.0.0.1:8000/` to see the BlogSphere homepage.

## Screenshots
> ⚠️ All screenshots saved in the `images/` folder of your project directory.

### 1️⃣ Home
![Home](images/home.png)

### 2️⃣ Search
![Search](images/search.png)

### 3️⃣ Login
![Login](images/login.png)

### 4️⃣ Signup
![Signup](images/signup.png)  

### 5️⃣ Profile
![Profile](images/profile_2.png)
![Profile_Main](images/profile_main.png)

### 6️⃣ Edit Profile
![Edit_Profile](images/edit_profile.png)  

### 7️⃣ Create Post
![New_Post](images/new_post.png)

### 8️⃣ Edit Post 
![Edit_Post](images/edit_post.png)

### 9️⃣  Delete Post
![Delete_Post](images/delete_post.png)


## Troubleshooting
- **Static Files Not Loading**:
  - Ensure `{% load static %}` is at the top of each template.
  - Verify that `STATICFILES_DIRS` and `STATIC_ROOT` are correctly set in `settings.py`.
  - Run `python manage.py collectstatic` again.
  - Clear browser cache (`Ctrl + Shift + R`).
- **Database Errors**:
  - Run `python manage.py makemigrations` and `python manage.py migrate` to fix migration issues.
  - Delete `db.sqlite3` and re-run migrations if necessary (you'll lose existing data).
- **Styling Issues**:
  - Check if `style.css` is in `static/css/` and collected in `staticfiles/`.
  - Inspect the browser console (F12) for 404 errors on static files.

## Credits
- **Developed by**: Vaghela Purvarajsinh  
  A vacation project created while learning Django, aimed at mastering web development with Python.
- **Special Thanks**: To Grok (xAI) for providing guidance and support during the development process, helping with debugging, styling, and enhancing the project.
