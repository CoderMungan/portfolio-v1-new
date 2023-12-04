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

- Home Page Photo
<img width="900" alt="homepage" src="https://github.com/CoderMungan/portfolio-v1-new/assets/126997544/919ca886-5cd1-483d-93c4-14dd36b79595">


- Blog Page Photo
<img width="900" alt="blogpage" src="https://github.com/CoderMungan/portfolio-v1-new/assets/126997544/94b0e162-2198-4382-b75d-978df0e54215">


- Article Page Photo
<img width="900" alt="articlepage" src="https://github.com/CoderMungan/portfolio-v1-new/assets/126997544/6559504f-a7bd-4c5d-8e9e-cb4eb743d509">


- Single Page Blog & Article Photo
<img width="900" alt="single" src="https://github.com/CoderMungan/portfolio-v1-new/assets/126997544/aaea4996-e6dd-4ea9-8270-c671a4e93e34">


- Contact Page Photo
<img width="900" alt="contactpage" src="https://github.com/CoderMungan/portfolio-v1-new/assets/126997544/d93861ac-386a-48e1-9c64-c1ad947dbddd">


- Contact Succes Page
<img width="900" alt="contactsucces" src="https://github.com/CoderMungan/portfolio-v1-new/assets/126997544/a2be4212-aed8-4eb5-8438-93a5993fc56a">


- 404 Not Found Page
<img width="900" alt="notfound" src="https://github.com/CoderMungan/portfolio-v1-new/assets/126997544/27017966-6990-4b9f-8a29-b18ec2256b65">


## Mobil View

- Side
<img width="544" alt="mobile" src="https://github.com/CoderMungan/portfolio-v1-new/assets/126997544/1f08d12b-01c6-4197-ad9c-c1070053995a">


- Navbar
<img width="541" alt="navbar" src="https://github.com/CoderMungan/portfolio-v1-new/assets/126997544/944ffc4a-93c5-47f4-8a58-ff122baf5197">

## Api View

<img width="900" alt="api1" src="https://github.com/CoderMungan/portfolio-v1-new/assets/126997544/19952381-f573-4f28-a675-5cf40d507fe5">
<img width="900" alt="api2" src="https://github.com/CoderMungan/portfolio-v1-new/assets/126997544/1b994006-756c-4e1d-8c46-18b4614aae45">

## Admin Panel

<img width="900" alt="adminpanel" src="https://github.com/CoderMungan/portfolio-v1-new/assets/126997544/4b7c895b-b55f-4c29-8cf9-2a2b0552465d">



