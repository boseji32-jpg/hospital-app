#!/bin/sh
find /usr/share/nginx/html -type f -name "*.js" -exec sed -i 's|http://api:8000|http://localhost:8000|g' {} +
find /usr/share/nginx/html -type f -name "*.js" -exec sed -i 's|api:8000|localhost:8000|g' {} +
