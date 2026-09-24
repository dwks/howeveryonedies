#!/bin/sh
# Wrap content.html (the Claude Artifact page body) in a standalone HTML
# document so the same source serves the published site and the artifact.
# The `<!-- @body -->` sentinel in content.html divides head from body.
set -e
{
  printf '<!doctype html>\n<html lang="en">\n<head>\n'
  printf '<meta charset="utf-8">\n'
  printf '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
  awk '/<!-- @body -->/ { print "</head>\n<body>"; next } { print }' content.html
  printf '</body>\n</html>\n'
} > index.html
echo "built index.html"
