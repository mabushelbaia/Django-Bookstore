# Django Bookstore
A simple Library that showcases the use of Django and Django Rest Framework, with a simple frontend Tailwind CSS.
The project is shipped in multiple docker containers, running an Nginx server, a Django server running WSGI, and a Postgres database.

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
3. Visit `http://localhost:8000` in your browser

## Future Improvements
- [ ] Add search functionality
- [ ] Add pagination

 
