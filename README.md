# Users-Service

## Requirements
* Docker
* A `.env` file in the root directory with the fields `DB_USER` and `DB_PASSWORD`

## Run Docker Compose
* In the root directory, open a shell and run the command:

```console
root~$ docker compose up --build
```

The default port is `3000`.

## Endpoints

* **GET `/users/ping`**: Check if the service is running

* **POST `/users/reset`**: Clean the database
    * **Headers**:
    ```json
    {
        "Authorization": "Bearer <token>"
    }
    ```

* **POST `/users/`**: Create a new user
    * **Body**:
    ```json
    {
        "firstName": "<USER_FIRST_NAME>",
        "lastName": "<USER_LAST_NAME>",
        "email": "<USER_EMAIL>",
        "password": "<USER_PASSWORD>"
    }
    ```

* **GET `/users/me`**: Obtain the user information associated with the token
    * **Headers**:
    ```json
    {
        "Authorization": "Bearer <token>"
    }
    ```
* **POST `/users/auth`**: Generates a token for the user associated with the email and password.
    * **Body**:
    ```json
    {
        "email": "<USER_EMAIL>",
        "password": "<USER_PASSWORD>"
    }
    ```
