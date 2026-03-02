FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install Qdrant
RUN curl -L https://github.com/qdrant/qdrant/releases/download/v1.8.4/qdrant-x86_64-unknown-linux-gnu.tar.gz \
    | tar -xz -C /usr/local/bin

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501
EXPOSE 6333

CMD qdrant & streamlit run main.py --server.port=8501 --server.address=0.0.0.0