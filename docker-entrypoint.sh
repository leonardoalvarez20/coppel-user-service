#!/bin/bash
set -xe

dbmate -e "DATABASE_URL" -d "./db/migrations" up
exec uvicorn app.main:app --workers 3 --host 0.0.0.0 --http h11 --port 8000
