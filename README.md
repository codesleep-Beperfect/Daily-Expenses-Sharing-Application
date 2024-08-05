# Daily Expenses Sharing Application

## Overview

The Daily Expenses Sharing Application is a robust backend service designed to manage and split daily expenses among users. The application allows users to add expenses and split them based on three methods: exact amounts, percentages, and equal splits. It provides comprehensive expense management features, including user details validation and the generation of downloadable balance sheets.

## Features

- **User Management**
  - Create and manage user profiles.
  - Each user has a unique email, name, and mobile number.

- **Expense Management**
  - Add expenses with descriptions and amounts.
  - Split expenses using three methods:
    - **Equal Split**: Divide expenses equally among all participants.
    - **Exact Amount**: Specify the exact amount each participant owes.
    - **Percentage**: Specify the percentage each participant owes, ensuring the total equals 100%.

- **Balance Sheet**
  - Generate individual balance sheets.
  - Generate overall balance sheets for all users.
  - Download balance sheets in PDF format.

## Technologies Used

- **Backend Framework**: Django
- **Database**: SQLite (can be switched to any other relational database)
- **API**: Django REST Framework (DRF)
- **PDF Generation**: ReportLab 

## Installation
1. Fork this repository to your github account.
2. Clone the forked repository and go to root directory.

   ```sh
   git clone https://github.com/yourusername/daily-expenses-sharing-app.git
   cd daily-expenses-sharing-app
3. Create and Activate Virtual Environment
    ```sh
    python -m venv venv
    venv\Scripts\activate
4. Install Dependencies
    ```sh
    pip install -r requirements.txt
5. Apply Migrations
    ```sh
    python manage.py migrate
6. Run the Development Server
    ```sh
    python manage.py runserver

## Available APIs

### POST /create/
- **Create an User**
    ```sh
    payload:
    {
        "username":"Deepak",
        "email":"deepak@gmail.com",
        "phone_number":"9935327382"
        "password":"12345"
    }
    response:
    {
        "id": "3",
        "username": "Deepak",
        "email": "deepak@gmail.com",
        "phone_number": "9935327382"
    }

### POST /login/
- **Login an User** 
    : Notedown the obtained csrf_token and seesion_id from the cookie section from response side
    ```sh
    payload:
    {
        "username":"Deepak",
        "password":"12345"
    }
    response:
    {
        "message":"Login successful"
    }

### POST /logout/
- **Logout an User**
    ```sh
    headers:
    X-CSRFToken: obtained csrf_token
    Cookie: sessionid=obtained session_id
    response:
    {
        "message":"Logout succcessful"
    }

### GET /retrieve_all/
- **List all users**
    ```sh
    headers:
    X-CSRFToken: obtained csrf_token
    Cookie: sessionid=obtained session_id
    response:
    {
        "data":[
        {
            "id": "3",
            "name": "Deepak Agarwal",
            "email": "deepak@gmail.com",
            "phone_number": "9935327382"
        },
        {
            "id": "4",
            "username": "Lucky",
            "email": "lucky@gmail.com",
            "phone_number": "9734874398"
        }
        ]
    }

### GET /retrieve/user_id/
- **Returns an User if present**
    ```sh
    headers:
    X-CSRFToken: obtained csrf_token
    Cookie: sessionid=obtained session_id
    response{
        "id": "3",
        "name": "Deepak Agarwal",
        "email": "deepak@gmail.com",
        "phone_number": "9935327382"
    }

### POST /add-expenses/
- **Create an Expense**
    ```sh
    headers:
    X-CSRFToken: obtained csrf_token
    Cookie: sessionid=obtained session_id
    payload:
    {
      "user": "1",
      "title": "Room",
      "description": "Room at Manali",
      "amount": "900.00",
      "date": "2024-08-05",
      "shares": [
        {
          "user": "1",
          "amount": "400.00",
          "share_type": "exact",
          "percentage": null
        },
        {
          "user": "2",
          "amount": "300.00",
          "share_type": "exact",
          "percentage": null
        },
        {
          "user": "3",
          "amount": "200.00",
          "share_type": "exact",
          "percentage": null
        }
      ]
    }
    response:
    { "data":{
        "user": "1",
        "title": "Room",
        "description": "Room at Manali",
        "amount": "900.00",
        "date": "2024-07-28",
        "shares": [
        {
            "user": "1",
            "amount": "400.00",
            "share_type": "exact",
            "percentage": null
        },
        {
            "user": "2",
            "amount": "300.00",
            "share_type": "exact",
            "percentage": null
        },
        {
            "user": "3",
            "amount": "200.00",
            "share_type": "exact",
            "percentage": null
        }
        ]
        }
  }

### GET /user/user_id/expenses/
- **Return an Expenses of an user**
    ```sh
    headers:
    X-CSRFToken: obtained csrf_token
    Cookie: sessionid=obtained session_id
    response{
        "data":[
        {
        "user": "1",
        "title": "Room",
        "description": "Room at Manali",
        "amount": "900.00",
        "date": "2024-07-28",
        "shares": [
        {
            "user": "1",
            "amount": "400.00",
            "share_type": "exact",
            "percentage": null
        },
        {
            "user": "2",
            "amount": "300.00",
            "share_type": "exact",
            "percentage": null
        },
        {
            "user": "3",
            "amount": "200.00",
            "share_type": "exact",
            "percentage": null
        }
        ]
        },
        {
        "user": 1,
        "title": "Office Supplies",
        "description": "Purchased office supplies",
        "amount": "100.00",
        "date": "2024-08-05",
        "shares": [
        {
            "user": 2,
            "amount": "50.00",
            "share_type": "exact",
            "percentage": null
        },
        {
            "user": 3,
            "amount": "50.00",
            "share_type": "exact",
            "percentage": null
        }
        ]
    }
    ]
    }

### GET /expenses/overall/
- **List all expenses**
    ```sh
    headers:
    X-CSRFToken: obtained csrf_token
    Cookie: sessionid=obtained session_id
    response:{
    "total_expense_amount": 1000.0,
  "expenses": [
    {
      "user": 1,
      "title": "Room",
      "description": "Room at Manali",
      "amount": "900.00",
      "date": "2024-08-05",
      "shares": [
        {
          "user": 1,
          "amount": "400.00",
          "share_type": "exact",
          "percentage": null
        },
        {
          "user": 2,
          "amount": "300.00",
          "share_type": "exact",
          "percentage": null
        },
        {
          "user": 3,
          "amount": "200.00",
          "share_type": "exact",
          "percentage": null
        }
      ]
    },
    {
      "user": 1,
      "title": "Office Supplies",
      "description": "Purchased office supplies",
      "amount": "100.00",
      "date": "2024-08-05",
      "shares": [
        {
          "user": 2,
          "amount": "50.00",
          "share_type": "exact",
          "percentage": null
        },
        {
          "user": 3,
          "amount": "50.00",
          "share_type": "exact",
          "percentage": null
        }
      ]
    }
  ]
}

### GET /balance-sheet/download/
- **Download Balance-Sheet**
    

