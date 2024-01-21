FROM python:3.8-slim
RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user
COPY cp install.sh ./ 
RUN bash install.sh
USER app_user
COPY . .
CMD ["bash"]