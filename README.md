
🔐 Authentication System
========================

A **production-grade authentication system** built with a strong focus on **security, scalability, and clean architecture**.This project demonstrates real-world backend engineering practices, not just basic login/signup flows.

✨ Features
----------

### Core Authentication

*   User signup with email & password
    
*   Secure password hashing
    
*   Login with JWT-based authentication
    
*   Logout with refresh token revocation
    

### Token Strategy

*   **Short-lived access tokens (JWT)**
    
*   **Long-lived refresh tokens** with:
    
    *   Database persistence
        
    *   Token rotation
        
    *   Revocation support
        
*   Stateless access token validation for scalability
    

### Email Verification

*   Email verification flow after signup
    
*   One-time, expiring verification tokens
    
*   Verified email enforcement for user trust
    

### Security

*   Rate limiting on sensitive endpoints (login, refresh)
    
*   Protection against brute-force attacks
    
*   UUID-based user identifiers
    
*   Explicit error handling with correct HTTP status codes
    

### Database & Migrations

*   PostgreSQL for persistent storage
    
*   SQLAlchemy 2.0 ORM
    
*   Alembic for schema migrations
    
*   Proper handling of schema evolution
    

🧱 Architecture Overview
------------------------

The project follows a **layered architecture** to ensure maintainability and scalability:

    app/
    ├── api/            # FastAPI routes (controllers)
    ├── core/           # Core utilities (JWT, hashing, rate limiting, Redis)
    ├── models/         # SQLAlchemy models
    ├── repositories/   # Database access layer
    ├── services/       # Business logic layer
    └── main.py         # Application entry point

### Key Design Principles

*   Clear separation of concerns
    
*   Stateless authentication using JWT
    
*   Stateful control using refresh tokens
    
*   Dependency-based security in FastAPI
    
*   Avoidance of tight coupling between services
    

🔑 Authentication Flow
----------------------

### Signup

1.  User registers with email & password
    
2.  Password is securely hashed
    
3.  User account is created as **unverified**
    
4.  Email verification token is generated
    
5.  Verification link is sent to the user
    

### Email Verification

1.  User clicks verification link
    
2.  Token is validated and expired tokens are rejected
    
3.  User account is marked as verified
    

### Login

1.  Credentials are validated
    
2.  Access token (JWT) is issued
    
3.  Refresh token is generated and stored in the database
    

### Token Refresh

1.  Refresh token is validated
    
2.  Old refresh token is revoked
    
3.  New access & refresh tokens are issued
    

### Logout

*   Refresh token is revoked, preventing further access token generation
    

🚦 Rate Limiting
----------------

Rate limiting is implemented using **Redis** to protect critical endpoints:

*   /auth/login
    
*   /auth/refresh
    
*   /auth/signup
    

This prevents:

*   Brute-force login attempts
    
*   Credential stuffing
    
*   Abuse of refresh token endpoints
    

🛠️ Tech Stack
--------------

**Backend**

*   FastAPI
    
*   SQLAlchemy 2.0
    
*   Alembic
    
*   PostgreSQL
    

**Security & Infrastructure**

*   JWT (Access & Refresh tokens)
    
*   Redis (rate limiting)
    
*   Password hashing (secure algorithms)
    

**Dev & Ops**

*   Docker & Docker Compose
    
*   Structured project layout
    
*   Environment-based configuration
    

▶️ Running the Project
----------------------

### Prerequisites

*   Docker & Docker Compose
    
*   Python 3.12+
    
### Clone Project

    git clone https://github.com/DeviSriPrasad9999/auth-system.git
    cd auth-system
    docker-compose up --build

### Start services

    docker compose up --build  

### Run migrations

    docker compose exec auth-system uv run  alembic upgrade head  

### API Docs

Once running, access:

    http://localhost:8000/docs  

📌 Why This Project Matters
---------------------------

This is **not a tutorial-level auth system**.

It demonstrates:

*   Real-world authentication patterns
    
*   Secure token handling
    
*   Scalable stateless design
    
*   Thoughtful trade-offs between simplicity and security
    
*   Backend system design principles used in production systems
    

🚀 Future Enhancements
----------------------

*   Store refresh tokens as HttpOnly cookies
    
*   JWT signing with asymmetric keys (RS256 + JWKS)
    
*   Role-based authorization
    
*   Password reset flow
    
*   Audit logging for security events
    
*   Gateway-level rate limiting
    
## 👨‍💻 Author

**Devi Sri Prasad Perni** 

Full Stack Developer | Angular | Django | System Design 

🔗 GitHub: https://github.com/DeviSriPrasad9999 

🔗 LinkedIn: https://www.linkedin.com/in/devisriprasadperni/
