FROM python:3.9-alpine
WORKDIR /opencart
COPY requirements.txt .
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["pytest", "--browser", "chrome", "--url", "https://demo.opencart.com"]