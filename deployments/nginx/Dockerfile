FROM nginx:latest
WORKDIR /etc/nginx/conf.d

RUN rm /etc/nginx/conf.d/default.conf

#COPY nginx.conf /etc/nginx/
COPY default.conf /etc/nginx/conf.d/
COPY /static/ /static/


CMD ["nginx","-g","daemon off;"] 
#CMD ["nginx","-s","reload"]
            




