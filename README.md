# Django Bookstore
a full-stack web application using Django and Tailwind CSS to display a collection of books. Utilized Nginx as a reverse proxy server and Gunicorn as the WSGI server to deploy the application using Docker.
![Bookstore Image](/merged_image.png)
## Installation
1. Clone the repository
```bash
git clone https://github.com/mabushelbaia/django-library
cd django-library
```
2. Create a `.env` file in the root directory and add the following environment variables
```bash
DEBUG=1
SECRET_KEY=your_secret_key
```
2. Run 
```bash
docker-compose up
```
3. Visit `http://localhost` in your browser

## Future Improvements
- [ ] Add search functionality
- [ ] Add pagination

 
