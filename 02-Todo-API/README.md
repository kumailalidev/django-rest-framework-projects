# 📃 Todo REST API

## Description

A Todo REST API is a web-based service that facilitates the management of a todo list

## Features

- Ability to retrieve list of todos
- Ability to add a new item to their list
- Ability to access details of a specific todo list
- Ability to filter todo items based on their completion status by specifying URL parameter (e.g. completed=true or completed=false)
- Ability to sort todo list based on updated date by specifying sort_by=updated_date URL parameter.

## Endpoints

| Endpoint            | Description                                                                             | Allowed HTTP Methods | Parameters         | Permissions |
| ------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------ | ----------- |
| `api/todos/`        | This endpoint allows users to retrieve list of todos and add a new todo object.         | GET, POST            | completed, sort_by | AllowAny    |
| `api/todo/<int:pk>` | This endpoint provides detail view of todo object also ability to modify a todo object. | GET, PATCH           |                    | Allow Any   |
