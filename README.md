# Inventory API

A simple FastAPI CRUD application for managing inventory items ("barang") with authentication.
This project uses Supabase for authentication and data storage.

## Features

- **User Registration & Login** (JWT-based, via Supabase)
- **CRUD for Inventory Items** (Barang)
  - Create, Read, Update, Delete items
  - Each item belongs to a user
  - Price validation and duplicate checks
- **Custom Error Handling & Logging**
- **Modular Structure** (API, services, repositories, models)

## Tech Stack

- Python, FastAPI
- Supabase (as backend database & auth)
- Pydantic (data validation)
- Docker-ready (optional)

## Getting Started

1. **Clone the repo**
2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
3. **Set environment variables**  
   Create a `.env` file with:
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   ```
4. **Run the app**
   ```
   uvicorn app.main:app --reload
   ```

## API Endpoints

- `POST /auth/register` — Register new user
- `POST /auth/login` — Login and get JWT token
- `GET /barang/` — List all items (user only)
- `POST /barang/` — Add new item
- `GET /barang/{item_id}` — Get item details
- `PATCH /barang/{item_id}` — Update item
- `DELETE /barang/{item_id}` — Delete item

## License

MIT
