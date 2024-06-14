FROM dockerhub.timeweb.cloud/library/node:latest

WORKDIR /app

RUN apt-get update

COPY package*.json .
RUN npm i

COPY . .

RUN npm run build

EXPOSE 4173

CMD ["npm", "run", "preview"] 
