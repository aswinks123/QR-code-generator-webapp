FROM python:3.7
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN apt update -y && apt install zbar-tools -y && apt install libgl1 -y
RUN pip install -r requirements.txt
EXPOSE 8501
COPY ./* /app/
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
