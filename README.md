***

# 🎓 Student Grievance Support System

***

## 🚀 Project Overview

The Student Grievance Support System is a web-based application developed with Django and Python to streamline the process of lodging, tracking, and resolving student complaints in academic institutions. Students can submit grievances on academic, administrative, or social matters. Admins and faculty handle and resolve complaints efficiently, ensuring confidentiality and transparency throughout.

***

## 📝 Key Features

- **Student Complaint Registration**: Register, activate with OTP, and lodge complaints by department, year, type.
- **Complaint Tracking**: View status and history of submitted complaints.
- **Role-Based Dashboards**: Distinct dashboards for students, faculty, and admin.
- **Automated Assignment**: Complaints routed to relevant faculty/committee.
- **Sentiment Analysis**: NLP classifies sentiment (positive, negative, neutral) of complaints for priority.
- **Confidentiality**: Anonymous complaint submission.
- **Admin Controls**: Add/remove faculty, oversee complaints, and manage system data.
- **Faculty Interaction**: Respond and update status on assigned complaints.
- **Email & OTP Notifications**: Account activations and important updates sent by email.

***

## 🛠️ Technology Stack

| Layer      | Tech/Tool                     |
|------------|------------------------------|
| Backend    | Django (Python)              |
| Frontend   | HTML, CSS (via Django)       |
| Database   | SQLite (default, switchable) |
| NLP        | Node.js Sentiment Analysis API (local) |
| Others     | JavaScript, SMTP (Email)     |

***

## 📁 Project Structure

| File/Module        | Description                                                      |
|--------------------|------------------------------------------------------------------|
| `models.py`        | Database models for Students, Complaints, Faculty                |
| `views.py`         | Route logic for dashboards, complaint processing, faculty mgmt   |
| `forms.py`         | Django forms for login, registration                             |
| `apps.py`          | Django application configuration                                 |
| `admin.py`         | Admin panel integration                                          |
| `README.md`        | Sentiment Analysis API details                                   |
| `Student grievance Support System.pdf` | Documentation (requirements, UML, ER, survey) |

***

## 🖥️ Setup and Installation

### **Prerequisites**

- Python 3.7+
- Anaconda or VS Code (IDE)
- Node.js (for Sentiment Analysis API)
- SQLite (default database)
- Minimum 4GB RAM, i5/i7 Processor

### **Steps**

1. **Clone the Repository**
    ```sh
    git clone <repo-url>
    cd StudentComplaintManagement
    ```

2. **Setup Python & Django**
    Create and activate a virtual environment (example with Anaconda):
    ```sh
    conda create -n project python=3.9
    conda activate project
    ```
    Install dependencies:
    ```sh
    pip install django
    ```

3. **Run the Django Server**
    ```sh
    python manage.py runserver
    ```

4. **Integrate Node.js Sentiment Analysis (Optional)**
    ```sh
    git clone https://github.com/cdw1p/Sentiment-Analysis.git
    cd Sentiment-Analysis
    npm install
    node index.js
    ```
    This exposes an endpoint at `http://localhost/word` for sentiment classification.

***

## 🔗 API Endpoints

### Django Backend

- `/login` — User authentication (student/faculty/admin)
- `/dashboard` — Dashboard for logged-in user role
- `/addfaculty` — Admin: add faculty/committee member
- `/viewcomplaints` — Admin/Faculty: list complaints
- `/addcomplaint` — Student: submit complaint
- `/deletefaculty` — Admin: remove faculty
- `/deletecomplaint` — Student: remove complaint

### Sentiment Analysis (Node.js)

- `GET http://localhost/word`
    ```json
    {
      "response": "negative" // or "positive", "neutral"
    }
    ```

***

## 👥 User Roles & Workflow

### Students
- Register and activate via OTP
- Submit, delete, and track complaints
- View complaint status

### Faculty
- Log in (added by admin)
- View and update assigned complaints

### Admins
- Manage users, faculty, complaints
- Access overall stats

***

## 🛤️ Future Enhancements

- Mobile application for on-the-go submissions
- Upload audio/video evidence to complaints
- 24/7 toll-free hotline integration
- Performance tracker for committee members

***


