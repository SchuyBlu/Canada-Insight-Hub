#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

SERVICE="django"
MANAGE_CMD=(docker compose exec "$SERVICE" python backend/manage.py)

usage() {
  cat <<'EOF'
Usage: scripts/manage.sh <command> [args...]

Commands:
  makemigrations [app]  Run Django makemigrations inside the docker stack.
  migrate [target]      Run Django migrate inside the docker stack.
  dbshell               Open Django dbshell inside the docker stack.
EOF
}

if [[ $# -lt 1 ]]; then
  usage
  exit 1
fi

command="$1"
shift

case "$command" in
  makemigrations)
    exec "${MANAGE_CMD[@]}" makemigrations "$@"
    ;;
  migrate)
    exec "${MANAGE_CMD[@]}" migrate "$@"
    ;;
  dbshell)
    exec "${MANAGE_CMD[@]}" dbshell
    ;;
  *)
    usage
    exit 1
    ;;
esac
