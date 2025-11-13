FROM python:3.9-alpine
WORKDIR /app
RUN apk add --update make automake gcc g++ subversion python3-dev
RUN pip install -U pip
RUN apk add gfortran
RUN apk add cmake
RUN apk add openblas openblas-dev build-base
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]