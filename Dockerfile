FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN useradd --create-home --shell /bin/bash myuser
USER myuser
WORKDIR /home/myuser
COPY --chown=myuser:myuser install.sh install.sh
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser . .
RUN bash install.sh
CMD ["bash"]