#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
registry="$project_root/studies/repos.txt"
destination="$(dirname "$project_root")/ancillary-studies"

usage() {
    cat <<'EOF'
Usage: clone-studies.sh [STUDY ...]
       clone-studies.sh --list

With no names, clone every repository in studies/repos.txt.
Names may be short (experience-selection) or qualified
(alignment-farm/experience-selection).

Clones go into ancillary-studies beside construct-2, regardless of the
current directory. Existing paths are skipped; no pulls or resets occur.
Requires Git and an authenticated GitHub CLI with repository access.
EOF
}

if [[ $# -eq 1 && ( "$1" == "--help" || "$1" == "-h" ) ]]; then
    usage
    exit 0
fi
if [[ $# -eq 1 && "$1" == "--list" ]]; then
    cat "$registry"
    exit 0
fi

repositories=()
while IFS= read -r repository || [[ -n "$repository" ]]; do
    [[ -z "$repository" ]] && continue
    repositories+=("$repository")
done < "$registry"

selected=()
if [[ $# -eq 0 ]]; then
    selected=("${repositories[@]}")
else
    # Validate the entire selection before creating directories or cloning.
    for name in "$@"; do
        found=false
        for repository in "${repositories[@]}"; do
            if [[ "$name" == "$repository" || "$name" == "${repository##*/}" ]]; then
                selected+=("$repository")
                found=true
                break
            fi
        done
        if [[ "$found" == false ]]; then
            printf 'Unknown study: %s. Use --list for available repositories.\n' "$name" >&2
            exit 2
        fi
    done
fi

command -v git >/dev/null || { printf 'Git is required.\n' >&2; exit 1; }
command -v gh >/dev/null || { printf 'GitHub CLI (gh) is required.\n' >&2; exit 1; }
mkdir -p "$destination"
for repository in "${selected[@]}"; do
    target="$destination/${repository##*/}"
    if [[ -e "$target" || -L "$target" ]]; then
        printf 'Skipping existing path: %s\n' "$target"
        continue
    fi
    gh repo clone "$repository" "$target"
done
