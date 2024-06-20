FROM python:3

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code
COPY ./django_project /app
WORKDIR /app
COPY ./entrypoint.sh /
ENTRYPOINT [ "sh" , "/entrypoint.sh"]


