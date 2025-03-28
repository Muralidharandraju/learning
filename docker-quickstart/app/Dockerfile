FROM python:3.12
COPY . .
RUN pip install -r requirement.txt
EXPOSE 80
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]