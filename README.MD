# 🔍 JobBoard - Scalable Job Posting Platform

A fully featured, production-ready backend system for managing job listings, candidate applications, and multi-tenant company dashboards. Built with FastAPI, PostgreSQL, Celery, Redis, and Docker.

---

## 🚀 Features

### ✅ Core Features
- **Multi-tenant Support**: Companies can register and manage their own job boards
- **Role-based Access Control**: Admin, Recruiter, and Candidate roles
- **Authentication**: JWT-based login system with secure password hashing
- **Job Management**: CRUD for job listings with search & filtering
- **Application Tracking**: Track candidates through various stages
- **Public REST API**: Well-documented endpoints with OpenAPI (Swagger)

### ⚙️ Infrastructure & DevOps
- **Dockerized**: Consistent development and production environments
- **PostgreSQL**: Scalable and production-grade database
- **Redis + Celery**: Background task queue (emails, parsing, etc.)
- **Alembic**: Database migrations
- **Environment Variables**: Secure and configurable `.env` support

### 📈 Advanced Features (Planned)
- Resume upload & parsing (AI)
- Email/SMS notifications
- Admin analytics dashboard
- Stripe subscription integration
- Slack/webhook integration
- Interview scheduling with calendar sync

---

## 🛠️ Tech Stack

| Layer           | Tech                         |
|----------------|------------------------------|
| Backend         | FastAPI                      |
| Auth            | JWT (with OAuth optional)    |
| Database        | PostgreSQL                   |
| Background Jobs | Celery + Redis               |
| Migrations      | Alembic                      |
| Containerization| Docker + docker-compose      |
| DevOps          | GitHub Actions (CI/CD)       |
| Hosting         | Render / AWS ECS / GCP Run   |

---

## 🚧 Setup Instructions

```bash
# Clone repo
git clone https://github.com/yourusername/jobboard.git
cd jobboard

# Copy environment variables
cp .env.example .env

# Build and run containers
docker-compose up --build

# Run database migrations
docker-compose exec web alembic upgrade head
