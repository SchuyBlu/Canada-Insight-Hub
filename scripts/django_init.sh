#!/usr/bin/env sh
set -e

cd backend

DB_HOST="${POSTGRES_HOST:-postgres}"
DB_PORT="${POSTGRES_PORT:-5432}"
TIMEOUT=1800

echo "Waiting for DB $DB_HOST:$DB_PORT..."
start_time=$(date +%s)

while true; do
  if nc -z "$DB_HOST" "$DB_PORT" >/dev/null 2>&1; then
	  echo "Database is up!"
	  break
  fi

  now=$(date +%s)
  elapsed=$(( now - start_time ))

  if [ "$elapsed" -ge "$TIMEOUT" ]; then
	  echo "Timed out waiting for DB at $DB_HOST:$DB_PORT"
	  exit 1
  fi

  sleep 1
done

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
