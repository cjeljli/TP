FROM python:3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY api.py .
CMD ["python", "api.py"]

