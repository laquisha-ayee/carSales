
```markdown
#  CarSales App

A full-stack peer-to-peer car marketplace built with Flask, React (Vite), and PostgreSQL. Users can buy and sell vehicles directly — avoiding dealership fees and gaining transparency through mechanic-verified listings.

**Live Site:** [https://carsales-4b09.onrender.com](https://carsales-4b09.onrender.com)

---

##  Project Overview

**CarSales** empowers individuals to buy and sell cars directly, without the overhead of dealership markups or hidden fees. The platform makes it easy to list vehicles, browse inventory, and connect with other users in a secure, user-friendly environment.

To build trust and transparency, CarSales introduces a unique **“Verified by Mechanic”** feature: sellers can request a certified mechanic to inspect their vehicle and assign a verified badge to the listing. This ensures buyers know the car matches its description and is in reliable working condition.

Whether you're looking to sell your car quickly or find a great deal without dealership pressure, CarSales puts the power back in your hands.

---

##  Tech Stack

- **Frontend:** React + Vite, CSS Grid/Flexbox
- **Backend:** Flask, SQLAlchemy, PostgreSQL
- **Deployment:** Docker, Render.com
- **Auth:** Multi-layered login/logout logic
- **Dev Tools:** Git, VSCode, Postman, Flask CLI

---

##  Features

- Peer-to-peer car listings with full CRUD
- Secure user authentication and session management
- Mechanic-verified badge system for trusted listings
- Responsive UI with dynamic filtering
- RESTful API integration
- Seeded database with sample inventory

---

##  Future Roadmap

Planned features to expand functionality and user trust:

-  **Payment Integration** — enable secure transactions between buyers and sellers  
-  **Mechanic Scheduling** — allow sellers to book inspections and receive verified status  
-  **Messaging System** — facilitate direct communication between buyers and sellers  

---

## Getting Started

### Backend Setup
```bash
cd app
pipenv install
flask db upgrade
flask seed all
flask run
```

### Frontend Setup
```bash
cd react-vite
npm install
npm run build
```

### Environment Variables
Create a `.flaskenv` and `.env` file with:
```
FLASK_APP=app
FLASK_ENV=development
SCHEMA=car_sales_schema
DATABASE_URL=your_postgres_url
VITE_API_URL=http://localhost:5000
```

---

## Deployment (Render.com)

1. Build frontend:
   ```bash
   cd react-vite
   npm run build
   ```
2. Push changes to GitHub
3. Create a new Web Service on [Render.com](https://render.com)
4. Set Runtime to **Docker**, Branch to `main`, and leave Root Directory blank
5. Add environment variables:
   - `SECRET_KEY`
   - `FLASK_ENV=production`
   - `FLASK_APP=app`
   - `SCHEMA=car_sales_schema`
   - `DATABASE_URL` (from Render Postgres)

Once deployed, your site will auto-update with each push to `main`.

---

## Author

**Laquisha Raye** — Full-stack Software Engineer  
[LinkedIn](https://www.linkedin.com/in/laquisha-raye) | [GitHub](https://github.com/laquisha-ayee)


