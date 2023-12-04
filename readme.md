## Getting started

### 1. Cloning the project

- Fork `CoderMungan/portfolio-v1-new` under your personal account.
  - eg: `@YourAccount/portfolio-v1-new`
- Clone the project to your local computer:

```sh
# Download Repository
git clone https://github.com/CoderMungan/portfolio-v1-new.git
# Move into repository
cd portfolio-v1-new
```

### 2. Setting up `.env` files

- Go to directory `backend`.
- Create `.env`
```sh
SECRET_KEY = "SomeKey"
```

### 3. Setting up Docker & Migrations & Create Super User 

- You must the be directory `backend`

```sh
docker-compose build
```

- Migration from Docker

```sh
docker-compose run django-app python manage.py migrate
```

- Create Super User

```sh
docker-compose run django-app python manage.py createsuperuser
```

- Run the Docker

```sh
docker-compose up
```

- Now you can go to [127.0.0.1:8000](127.0.0.1:8000) to see it live. 🚀
- Admin panel [127.0.0.1:8000/admin](127.0.0.1:8000/admin)
- You can create what u want!

### 4. Setting Up Client Side

- You must the be directory `client`

- For the dependencies

```sh
npm install
```

- Now you can go to [localhost:5173](localhost:5173) to see it live. 🚀

```sh
npm run dev
```

### 5. Setting Up The Your Official Files

- You must the be directory `client`
- Go to the `src/assets/` directory upload your Resume with `resume.pdf` name

# Now you in Fire 🔥