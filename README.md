<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=30&pause=1000&color=2E75B6&center=true&vCenter=true&width=700&lines=E-Commerce+Platform+%F0%9F%9B%92;Browse+%C2%B7+Cart+%C2%B7+Checkout;Built+with+FastAPI+%2B+React" alt="Typing SVG" />

<br/>

<img src="https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge&logo=git" />
<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
<img src="https://img.shields.io/badge/PostgreSQL-16+-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/Version-1.0%20MVP-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />

<br/><br/>

> **ECP-2026**  A full-stack e-commerce platform built as a university group project. Enables customers to browse products, manage a cart, and complete purchases with a dedicated admin panel for product and order management.

<br/>

[📖 Documentation](#-documentation) · [🚀 Quick Start](#-quick-start) · [📡 API Reference](#-api-reference) · [🗺️ Roadmap](#-roadmap) · [👥 Team](#-team)

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [V1 Scope](#-v1-scope)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [API Reference](#-api-reference)
- [Database Schema](#-database-schema)
- [Roadmap](#-roadmap)
- [Team](#-team)
- [License](#-license)

---

## 🎯 About the Project

**ECP-2026** is a backend-first e-commerce platform developed by a team of four students at **Mbeya University of Science and Technology (MUST)**. The system follows a clean layered architecture separating API routing, business logic, data access, and the database and is paired with a React frontend for the customer-facing storefront and admin dashboard.

The project is structured around real-world software development practices: version control with Git, database migrations with Alembic, API documentation via Swagger, and role-based access control using JWT authentication.

**What the platform does:**

- 🛍️ **Browse** products by category with search and filter support
- 🛒 **Cart** management — add, update, and remove items
- 💳 **Checkout** flow with order placement and confirmation
- 🔐 **Authentication**  customer registration, login, and session management
- 🛠️ **Admin Panel**  manage products, categories, and view orders

---

## 📦 V1 Scope

Version 1 is intentionally scoped to the core buying flow. Scope is **locked** — any additions beyond what is listed below require a formal change request.

### ✅ What's Included in V1

| Area | Features |
|---|---|
| **Auth** | User registration, login (email + password), JWT session management |
| **Products** | Product listing, search by name, filter by category |
| **Cart** | Add to cart, update quantity, remove item, view cart total |
| **Checkout** | Place order, order confirmation page |
| **Orders** | Customer order history, order status tracking |
| **Admin** | Add / edit / delete products, view all orders |
| **Frontend** | Responsive storefront (React) — mobile and desktop |

### ❌ What's NOT in V1

| Excluded Feature | Reason |
|---|---|
| Real payment gateway (Stripe, PayPal, etc.) | Sandbox/mock only — integration complexity out of scope |
| Multi-vendor / marketplace | Out of V1 scope |
| Social login (Google, Facebook) | Post-MVP |
| Shipping & logistics integration | Post-MVP |
| Advanced analytics dashboard | Post-MVP |
| Native mobile app (iOS / Android) | Post-MVP |
| Product reviews and ratings | Post-MVP |

> ⚠️ **Note:** Scope is locked after Phase 1. Any change requests must be reviewed by the project lead and will affect the project timeline.

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                          │
│              React 18 · Tailwind CSS · Axios                 │
│         (Storefront · Cart · Checkout · Admin Panel)         │
└────────────────────────┬─────────────────────────────────────┘
                         │  HTTP / REST
┌────────────────────────▼─────────────────────────────────────┐
│                    API LAYER (FastAPI)                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐     │
│  │  /auth   │ │/products │ │  /cart   │ │   /orders    │     │
│  │  router  │ │  router  │ │  router  │ │    router    │     │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └──────┬───────┘     │
└───────┼────────────┼────────────┼──────────────┼────────────-┘
        │            │            │              │
┌───────▼────────────▼────────────▼──────────────▼───────────--┐
│                      SERVICE LAYER                           │
│          Business Logic · Validation · Orchestration         │
└───────────────────────────────┬──────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────┐
│                    REPOSITORY LAYER                          │
│              SQLAlchemy 2.0 Async ORM Queries                │
└───────────────────────────────┬──────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────┐
│                     DATABASE LAYER                           │
│               PostgreSQL 16 · Alembic Migrations             │
└──────────────────────────────────────────────────────────────┘
```

**Design Pattern:** Routes → Services → Repositories → Models  
**Auth:** JWT Bearer tokens with role-based access (Customer / Admin)  
**Validation:** Pydantic v2 schemas on all inputs and outputs  
**Frontend ↔ Backend:** REST API via Axios with CORS configured

---

## 🛠️ Tech Stack

### Backend

| Layer | Technology | Purpose |
|---|---|---|
| **Language** | Python 3.11+ | Core runtime |
| **Framework** | FastAPI 0.110+ | REST API & OpenAPI docs |
| **ORM** | SQLAlchemy 2.0 (async) | Database abstraction |
| **Database** | PostgreSQL 16+ | Primary data store |
| **Migrations** | Alembic | Schema version control |
| **Validation** | Pydantic v2 | Request / response schemas |
| **Auth** | JWT (python-jose) | Authentication & authorisation |
| **Testing** | pytest + httpx | Unit & integration tests |
| **Dev Server** | Uvicorn | ASGI server |
| **Env Config** | python-dotenv | Environment management |

### Frontend

| Layer | Technology | Purpose |
|---|---|---|
| **Framework** | React 18+ | UI component library |
| **Styling** | Tailwind CSS | Utility-first CSS framework |
| **HTTP Client** | Axios | API requests |
| **Routing** | React Router v6 | Client-side navigation |
| **State** | Context API | Cart & auth state management |
| **Build Tool** | Vite | Fast dev server & bundler |

---

## 📁 Project Structure

```
ecp-2025/
│
├── 📁 backend/
│   ├── 📁 app/
│   │   ├── 📁 api/
│   │   │   ├── 📁 v1/
│   │   │   │   ├── auth.py           # Register, login, token refresh
│   │   │   │   ├── products.py       # Product CRUD endpoints
│   │   │   │   ├── cart.py           # Cart management endpoints
│   │   │   │   └── orders.py         # Order placement & history
│   │   │   └── deps.py               # Shared dependencies (auth, db)
│   │   │
│   │   ├── 📁 core/
│   │   │   ├── config.py             # App settings (env vars)
│   │   │   ├── security.py           # JWT creation & verification
│   │   │   └── database.py           # Async DB engine & session
│   │   │
│   │   ├── 📁 models/
│   │   │   ├── user.py               # User ORM model
│   │   │   ├── product.py            # Product ORM model
│   │   │   ├── cart.py               # Cart & CartItem ORM models
│   │   │   └── order.py              # Order & OrderItem ORM models
│   │   │
│   │   ├── 📁 schemas/
│   │   │   ├── user.py               # Pydantic schemas for users
│   │   │   ├── product.py            # Pydantic schemas for products
│   │   │   ├── cart.py               # Pydantic schemas for cart
│   │   │   └── order.py              # Pydantic schemas for orders
│   │   │
│   │   ├── 📁 services/
│   │   │   ├── auth_service.py       # Auth & user business logic
│   │   │   ├── product_service.py    # Product business logic
│   │   │   ├── cart_service.py       # Cart operations & pricing
│   │   │   └── order_service.py      # Order placement logic
│   │   │
│   │   ├── 📁 repositories/
│   │   │   ├── user_repo.py          # User DB queries
│   │   │   ├── product_repo.py       # Product DB queries
│   │   │   ├── cart_repo.py          # Cart DB queries
│   │   │   └── order_repo.py         # Order DB queries
│   │   │
│   │   └── main.py                   # App entry point & router mount
│   │
│   ├── 📁 alembic/                   # Database migrations
│   │   ├── versions/
│   │   └── env.py
│   │
│   ├── 📁 tests/
│   │   ├── test_auth.py
│   │   ├── test_products.py
│   │   └── test_orders.py
│   │
│   ├── .env.example
│   ├── requirements.txt
│   ├── alembic.ini
│   └── README.md
│
├── 📁 frontend/
│   ├── 📁 src/
│   │   ├── 📁 components/            # Reusable UI components
│   │   ├── 📁 pages/                 # Route-level pages
│   │   │   ├── Home.jsx
│   │   │   ├── ProductList.jsx
│   │   │   ├── ProductDetail.jsx
│   │   │   ├── Cart.jsx
│   │   │   ├── Checkout.jsx
│   │   │   ├── OrderConfirmation.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   └── admin/
│   │   │       ├── Dashboard.jsx
│   │   │       ├── Products.jsx
│   │   │       └── Orders.jsx
│   │   ├── 📁 context/               # Auth & cart context
│   │   ├── 📁 services/              # Axios API calls
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── index.html
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── package.json
│
└── README.md                         # ← You are here
```

---

## 🚀 Quick Start

### Prerequisites

Make sure you have the following installed:

- [Python 3.11+](https://www.python.org/downloads/)
- [Node.js 18+](https://nodejs.org/)
- [PostgreSQL 16+](https://www.postgresql.org/download/)
- [Git](https://git-scm.com/)

---

### 1. Clone the Repository

```bash
git clone https://github.com/khamisngofi-web/ecp-2025.git
cd ecp-2025
```

---

### 2. Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate — Linux / macOS
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Configure environment variables:**

```bash
cp .env.example .env
```

Edit `.env` with your values:

```env
# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/ecp_db

# Security
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# App
APP_NAME=ECP-2025
DEBUG=True
ALLOWED_ORIGINS=http://localhost:5173
```

**Run database migrations:**

```bash
alembic upgrade head
```

**Start the backend server:**

```bash
uvicorn app.main:app --reload
```

Backend is live at **[http://localhost:8000](http://localhost:8000)**

```
🌐 Swagger UI  →  http://localhost:8000/docs
📘 ReDoc       →  http://localhost:8000/redoc
💓 Health      →  http://localhost:8000/health
```

---

### 3. Frontend Setup

```bash
# Open a new terminal and navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend is live at **[http://localhost:5173](http://localhost:5173)**

---

## 📡 API Reference

### Authentication

```http
POST /api/v1/auth/register        # Create a new customer account
POST /api/v1/auth/login           # Login and receive JWT token
POST /api/v1/auth/refresh         # Refresh access token
```

### Products

```http
GET    /api/v1/products                    # List all products (with search & filter)
GET    /api/v1/products/{id}               # Get single product details
POST   /api/v1/products                    # [Admin] Create a product
PUT    /api/v1/products/{id}               # [Admin] Update a product
DELETE /api/v1/products/{id}               # [Admin] Delete a product
GET    /api/v1/products?category={name}    # Filter products by category
GET    /api/v1/products?search={query}     # Search products by name
```

### Cart

```http
GET    /api/v1/cart                        # Get current user's cart
POST   /api/v1/cart/items                  # Add item to cart
PUT    /api/v1/cart/items/{item_id}        # Update item quantity
DELETE /api/v1/cart/items/{item_id}        # Remove item from cart
DELETE /api/v1/cart                        # Clear entire cart
```

### Orders

```http
POST   /api/v1/orders                      # Place an order from current cart
GET    /api/v1/orders                      # Get customer's order history
GET    /api/v1/orders/{id}                 # Get order details
GET    /api/v1/admin/orders                # [Admin] View all orders
PUT    /api/v1/admin/orders/{id}/status    # [Admin] Update order status
```

> 📘 Full interactive documentation available at `/docs` once the backend server is running.

---

## 🗄️ Database Schema

```
┌──────────────┐       ┌─────────────────┐       ┌───────────────────┐
│    users     │       │    products     │       │   categories      │
├──────────────┤       ├─────────────────┤       ├───────────────────┤
│ id (PK)      │       │ id (PK)         │       │ id (PK)           │
│ full_name    │       │ name            │       │ name              │
│ email        │       │ description     │◄──────│ slug              │
│ password     │       │ price           │       │ created_at        │
│ role         │       │ stock           │       └───────────────────┘
│ created_at   │       │ category_id(FK) │
└──────┬───────┘       │ image_url       │
       │               │ created_at      │
       │               └────────┬────────┘
       │                        │
┌──────▼───────┐                │
│     cart     │       ┌────────▼────────┐       ┌───────────────────┐
├──────────────┤       │   cart_items    │       │     orders        │
│ id (PK)      │       ├─────────────────┤       ├───────────────────┤
│ user_id (FK) │──────►│ id (PK)         │       │ id (PK)           │
│ created_at   │       │ cart_id (FK)    │       │ user_id (FK)      │
└──────────────┘       │ product_id (FK) │       │ total_amount      │
                       │ quantity        │       │ status            │
                       │ unit_price      │       │ created_at        │
                       └─────────────────┘       └────────┬──────────┘
                                                          │
                                                 ┌────────▼──────────┐
                                                 │   order_items     │
                                                 ├───────────────────┤
                                                 │ id (PK)           │
                                                 │ order_id (FK)     │
                                                 │ product_id (FK)   │
                                                 │ quantity          │
                                                 │ unit_price        │
                                                 └───────────────────┘
```

---

## 🗺️ Roadmap

### Phase 1 — Initiation ✅
- [x] Project Charter approved
- [x] Team roles assigned
- [x] Scope defined and locked

### Phase 2 — Planning 🔄
- [ ] Requirements documented
- [ ] Timeline and milestones set
- [ ] Risk register created

### Phase 3 — Design
- [ ] Wireframes created
- [ ] UI design approved
- [ ] Architecture diagram finalized

### Phase 4 — Development
- [ ] Repository setup & branch protection
- [ ] Backend: Auth endpoints
- [ ] Backend: Product CRUD
- [ ] Backend: Cart management
- [ ] Backend: Order placement
- [ ] Frontend: Storefront pages
- [ ] Frontend: Cart & checkout flow
- [ ] Frontend: Admin panel

### Phase 5 — Testing
- [ ] Functional testing per feature
- [ ] API integration testing
- [ ] User acceptance testing (UAT)
- [ ] Bug fixing sprint

### Phase 6 — Deployment
- [ ] Configure production environment
- [ ] Deploy backend (Railway / Render)
- [ ] Deploy frontend (Vercel / Netlify)
- [ ] Release validation

### Phase 7 — Closure
- [ ] Documentation handover
- [ ] Lessons learned review
- [ ] Project closure report

---

## 👥 Team

<div align="center">

| Role | Name | Responsibility |
|---|---|---|
| **Project Lead** | Khamis Mgofi | Architecture, code review, delivery |
| **Frontend Developer** | `Elizabeth` | React storefront & admin panel |
| **Backend Developer** | `Kaleb` | FastAPI routes & business logic |
| **Database Engineer** | `Nelson` | PostgreSQL models & migrations |
| **Integration & QA** | `Khamis` | API integration, testing & bug fixes |

*Developed at **Mbeya University of Science and Technology (MUST)**, Tanzania*

</div>

---

## 🤝 Contributing

This is a university group project. Contributions are limited to team members. Branch protection rules are enforced — all changes go through pull requests.

```bash
# 1. Pull the latest main
git pull origin main

# 2. Create your feature branch
git checkout -b feature/your-feature-name

# 3. Commit your changes (follow Conventional Commits)
git commit -m "feat: add product search filter"

# 4. Push to your branch
git push origin feature/your-feature-name

# 5. Open a Pull Request for review
```

**Branch naming convention:**
- `feature/` — new features
- `fix/` — bug fixes
- `docs/` — documentation updates
- `test/` — adding or updating tests

> ⚠️ No direct pushes to `main`. All PRs require review from the project lead before merging.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Built with ❤️ by **Khamis Mgofi & E-commerce Team** · MUST, Tanzania · 2025

⭐ Star this repo if you found it helpful!

</div>
