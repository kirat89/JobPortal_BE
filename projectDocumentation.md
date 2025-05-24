🚀 Project Overview

Project Name: JobBoard Platform

Description:
A multi-tenant job board platform where companies can manage their own job postings and candidates can apply through custom subdomains (e.g., company.jobboard.com). Designed to scale for multiple organizations, with modern best practices in backend development and deployment.

🎯 Scope

This project is a full-featured backend system for a job portal with:

Multi-company support via subdomains

Role-based access control (Admin, Recruiter, Candidate)

Job creation, listing, and application management

Secure authentication (JWT)

Scalable backend architecture with FastAPI and PostgreSQL

API layer designed to eventually integrate with GraphQL and modern frontends

✅ Key Features
User Authentication & Authorization

Register, login, JWT-based auth

Roles: Candidate, Recruiter, Admin

Company Profiles

Create/manage company info

Subdomain support per company

Job Postings

Recruiters can post jobs

Search and filter jobs (by title, company, etc.)

Job Applications

Candidates can apply to jobs

Track application status (applied, shortlisted, rejected)

Multi-Tenant Architecture

Subdomain-based tenant isolation

Shared backend, logically separated data

Admin Portal (Future Phase)

Overview of all companies, jobs, users

Manage roles, moderate listings

Dev Experience

Pre-commit hooks, linters (flake8), type-checking (mypy)

Alembic migrations for DB versioning

Docker-ready for deployment

🧱 Tech Stack
Backend: Python, FastAPI

ORM: SQLAlchemy

Database: PostgreSQL (local in dev)

Dev Tooling: pre-commit, flake8, mypy, isort

Testing: Pytest

Migrations: Alembic

(Future): GraphQL Gateway Layer (Node.js), Docker, CI/CD

🗂 Directory Structure
(Reference your actual structure here once it's scaffolded.)

🧪 Development Setup
Instructions for setting up local dev (from your dev-doc will link here).