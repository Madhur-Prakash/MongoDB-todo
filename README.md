# Practice Todo App
**A Simple Todo App Built with MongoDB and FastAPI**

---

## Overview
This repository implements a basic Todo App using FastAPI and MongoDB, allowing users to practice CRUD (Create, Read, Update, Delete) operations.

---

## Features
* **Create Todo**: Create new todo items
* **Read Todo**: Read all todo items
* **Update Todo**: Update existing todo items
* **Delete Todo**: Delete todo items
* **Fast and Scalable**: Built with FastAPI for high performance and scalability
* **MongoDB Integration**: Stores todo items in a reliable NoSQL database

---

## Technology Stack
* **Backend Framework**: FastAPI
* **Database**: MongoDB
* **Programming Language**: Python

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Madhur-Prakash/MongoDB-todo.git
   ```
2. Navigate to the project directory:
   ```bash
   cd MongoDB-todo
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up MongoDB:
   - Install MongoDB and start the service.
   - Configure the MongoDB URI in the `config/db.py` file.

---

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
2. Access the API documentation at:
   ```
   http://127.0.0.1:8000/docs
   ```
3. Use the API to create, read, update, and delete todo items.

---

## API Endpoints

### Todo Endpoints
- **POST /note**: Create a new todo item
- **GET /note**: Read all todo items
- **POST /note/{id}**: Update an existing todo item
- **POST /note/{id}**: Delete a todo item

---

## Project Structure

```plaintext
MongoDB-todo/
├── .gitignore  # gitignore file for GitHub
├── app.py  # main FastAPI app
├── config
│   └── db.py
├── models
│   └── model.py
├── requirements.txt
├── routes
│   └── note.py
└── templates
    ├── index.html
    └── update.html
```

---

## Future Enhancements
- Add support for user authentication
- Implement filtering and sorting for todo items
- Enhance error handling and logging

---

## Contribution Guidelines

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.


---

## Author
**Madhur-Prakash**  
[GitHub](https://github.com/Madhur-Prakash)