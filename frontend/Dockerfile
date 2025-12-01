FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
RUN apk add --no-cache dos2unix
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/dist /usr/share/nginx/html
COPY inject-api-url.sh /docker-entrypoint.d/40-inject-api-url.sh
RUN dos2unix /docker-entrypoint.d/40-inject-api-url.sh && chmod +x /docker-entrypoint.d/40-inject-api-url.sh
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
