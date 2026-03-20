# MiCoachBrain 

Backend API for the MiCoachBrain AI Project

## Prerequisites

Before you begin, ensure you have the following installed on your machine:
- **Python 3.12+**[(Download)](https://www.python.org/downloads/) 
- **[uv](https://docs.astral.sh/uv/)** (Fast Python package manager)
  - *macOS/Linux:* `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - *Windows:* `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"` [See installation docs](https://docs.astral.sh/uv/getting-started/installation/)

## Getting Started

Follow these steps to get your local development environment up and running.

### 1. Clone the repository
```bash
git clone https://github.com/IsraPR/mi-coach-brain-backend.git
cd mi-coach-brain-backend
```

### 2. Install dependencies
We use `uv` for dependency management. Running the sync command will automatically create a virtual environment (`.venv`) and install all required packages from the `uv.lock` file.
```bash
uv sync
```

### 3. Set up environment variables
Copy the example environment file and update the values if necessary.
```bash
cp .env.example .env
```
*(Note: The default values in `.env.example` are usually sufficient but ask project owner for values if required).*

### 4. Activate the virtual environment
You must activate the virtual environment to run Django management commands.
```bash
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### 5. Run database migrations
Apply the initial schema to your local SQLite database.
```bash
python manage.py migrate
```

### 6. Start the development server
```bash
python manage.py runserver
```
The API/App should now be running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

