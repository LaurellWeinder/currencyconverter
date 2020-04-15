FROM python:3-onbuild
RUN pip install -r requirements.txt
EXPOSE 5000
RUN chmod +x ./cgi-bin
CMD python3 main.py