# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.11-slim

RUN useradd -m -u 1000 devops_user
WORKDIR /app
COPY --from=builder /install /usr/local
COPY --chown=devops_user:devops_user app/ .
USER devops_user
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
