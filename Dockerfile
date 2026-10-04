FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Scheduler (cron / platform scheduler) runs: tekbrokr-enterprise ingest, then report
ENTRYPOINT ["tekbrokr-enterprise"]
CMD ["doctor"]
