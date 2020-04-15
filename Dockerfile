FROM python:3-onbuild
EXPOSE 5000
CMD ["python", "./main.py"]
COPY requirements.txt ./
RUN pip install -r requirements.txt
