#!/bin/bash
# Only supported on linux (recommended on runtime docker)
# Please run `app.py` directly on Windows
## source venv/bin/activate &&

# For production
cd /app/api && gunicorn app:app -c gunicorn.py --access-logfile -

# For development
#cd /app/api && flask run --host=0.0.0.0 --port=8030