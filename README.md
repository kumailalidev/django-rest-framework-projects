<p align="center">
    <img src="assets/images/Django-REST-Framework-Logo.png" alt="Django REST Framework Logo" width="324px" />
    <h1 align="center">Django REST Framework Projects</h1>
</p>

# 📕 01. Books REST API

## Description

A Books REST API is a web-based service that provides read-only access to a collection of books and their associated authors. This API restricts HTTP methods to only allow `GET` requests on specific endpoints

## Endpoints

| Endpoint            | Description                                                                                                                                      | Allowed HTTP Method | Permissions |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | ----------- |
| `api/`              | This endpoint allows users to retrieve a list of all available books.                                                                            | GET                 | Any         |
| `api/book/<int:pk>` | The API provides a detailed view of individual books. Users can request specific book details by sending a GET request to the book's unique URL. | GET                 | Any         |
| `api/authors/ `     | This endpoint allows users to retrieve a list of all authors.                                                                                    | GET                 | Any         |

<hr>

# 📃 02. Todo REST API

## Description

A Todo REST API is a web-based service that facilitates the management of a todo list

## Features

- Ability to retrieve list of todos
- Ability to add a new item to their list
- Ability to access details of a specific todo list
- Ability to filter todo items based on their completion status by specifying URL parameter (e.g. `completed=true` or `completed=false`)
- Ability to sort todo list based on updated date by specifying `sort_by=updated_date` URL parameter.

## Endpoints

| Endpoint            | Description                                                                             | Allowed HTTP Methods | Parameters         | Permissions |
| ------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------ | ----------- |
| `api/todos/`        | This endpoint allows users to retrieve list of todos and add a new todo object.         | GET, POST            | completed, sort_by | AllowAny    |
| `api/todo/<int:pk>` | This endpoint provides detail view of todo object also ability to modify a todo object. | GET, PATCH           |                    | Allow Any   |
