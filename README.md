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
        "name":"Deepak Agarwal",
        "email":"deepak@gmail.com",
        "phone_number":"8346278198"
    }
    response:
    {
        "id": "c2721618-6cc2-4494-831c-5f86e4802eb0",
        "name": "Deepak Agarwal",
        "email": "deepak@gmail.com",
        "phone_number": "8346278198"
    }
### GET /retrieve_all/
- **List all users**
    ```sh
    response:
    {
        "data":[
        {
            "id": "c2721618-6cc2-4494-831c-5f86e4802eb0",
            "name": "Deepak Agarwal",
            "email": "deepak@gmail.com",
            "phone_number": "8346278198"
        },
        {
            "id": "2ffcb87f-2451-4805-942c-3c8d6578356b",
            "name": "Prateek Pal",
            "email": "prateek@gmail.com",
            "phone_number": "9695627369"
        }
        ]
    }

### GET /retrieve/user_id
- **Return an User if present**
    ```sh
    response{
        "id": "c2721618-6cc2-4494-831c-5f86e4802eb0",
        "name": "Deepak Agarwal",
        "email": "deepak@gmail.com",
        "phone_number": "8346278198"
    }

### POST /add-expenses/
- **Create an Expense**
    ```sh
    payload:
    {
      "user": "ff256f70-2d9d-4559-bb66-557e8efd4e69",
      "title": "Room",
      "description": "Room at Manali",
      "amount": "900.00",
      "date": "2024-07-28",
      "shares": [
        {
          "user": "ff256f70-2d9d-4559-bb66-557e8efd4e69",
          "amount": "400.00",
          "share_type": "exact",
          "percentage": null
        },
        {
          "user": "fa977a20-688b-4dc0-8e54-4f825c64567e",
          "amount": "300.00",
          "share_type": "exact",
          "percentage": null
        },
        {
          "user": "c2721618-6cc2-4494-831c-5f86e4802eb0",
          "amount": "200.00",
          "share_type": "exact",
          "percentage": null
        }
      ]
    }
    response:
    { "data":{
        "user": "ff256f70-2d9d-4559-bb66-557e8efd4e69",
        "title": "Room",
        "description": "Room at Manali",
        "amount": "900.00",
        "date": "2024-07-28",
        "shares": [
        {
            "user": "ff256f70-2d9d-4559-bb66-557e8efd4e69",
            "amount": "400.00",
            "share_type": "exact",
            "percentage": null
        },
        {
            "user": "fa977a20-688b-4dc0-8e54-4f825c64567e",
            "amount": "300.00",
            "share_type": "exact",
            "percentage": null
        },
        {
            "user": "c2721618-6cc2-4494-831c-5f86e4802eb0",
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
    response{
        "data":[
        {
        "user": "ff256f70-2d9d-4559-bb66-557e8efd4e69",
        "title": "Dinner",
        "description": "Dinner at restaurant",
        "amount": "100.00",
        "date": "2024-07-28",
        "shares": [
        {
            "user": "ff256f70-2d9d-4559-bb66-557e8efd4e69",
            "amount": "33.33",
            "share_type": "equal",
            "percentage": null
        },
        {
            "user": "fa977a20-688b-4dc0-8e54-4f825c64567e",
            "amount": "33.33",
            "share_type": "equal",
            "percentage": null
        },
        {
            "user": "622a80ae-48a8-48ce-bb91-584f4fd28ffb",
            "amount": "33.33",
            "share_type": "equal",
            "percentage": null
        }
        ]
        },
        {
        "user": "ff256f70-2d9d-4559-bb66-557e8efd4e69",
        "title": "Room",
        "description": "Room at Manali",
        "amount": "900.00",
        "date": "2024-07-28",
        "shares": [
        {
            "user": "ff256f70-2d9d-4559-bb66-557e8efd4e69",
            "amount": "400.00",
            "share_type": "exact",
            "percentage": null
        },
        {
            "user": "fa977a20-688b-4dc0-8e54-4f825c64567e",
            "amount": "300.00",
            "share_type": "exact",
            "percentage": null
        },
        {
            "user": "c2721618-6cc2-4494-831c-5f86e4802eb0",
            "amount": "200.00",
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
    response:{
    "total_expense_amount": 1500.0,
    "expenses": [
        {
        "user": "ff256f70-2d9d-4559-bb66-557e8efd4e69",
        "title": "Dinner",
        "description": "Dinner at restaurant",
        "amount": "100.00",
        "date": "2024-07-28",
        "shares": [
            {
            "user": "ff256f70-2d9d-4559-bb66-557e8efd4e69",
            "amount": "33.33",
            "share_type": "equal",
            "percentage": null
            },
            {
            "user": "fa977a20-688b-4dc0-8e54-4f825c64567e",
            "amount": "33.33",
            "share_type": "equal",
            "percentage": null
            },
            {
            "user": "622a80ae-48a8-48ce-bb91-584f4fd28ffb",
            "amount": "33.33",
            "share_type": "equal",
            "percentage": null
            }
        ]
        },
        {
        "user": "ff256f70-2d9d-4559-bb66-557e8efd4e69",
        "title": "Room",
        "description": "Room at Manali",
        "amount": "900.00",
        "date": "2024-07-28",
        "shares": [
            {
            "user": "ff256f70-2d9d-4559-bb66-557e8efd4e69",
            "amount": "400.00",
            "share_type": "exact",
            "percentage": null
            },
            {
            "user": "fa977a20-688b-4dc0-8e54-4f825c64567e",
            "amount": "300.00",
            "share_type": "exact",
            "percentage": null
            },
            {
            "user": "c2721618-6cc2-4494-831c-5f86e4802eb0",
            "amount": "200.00",
            "share_type": "exact",
            "percentage": null
            }
        ]
        },
        {
        "user": "fa977a20-688b-4dc0-8e54-4f825c64567e",
        "title": "Part",
        "description": "Birthday Party",
        "amount": "500.00",
        "date": "2024-07-28",
        "shares": [
            {
            "user": "fa977a20-688b-4dc0-8e54-4f825c64567e",
            "amount": "350.00",
            "share_type": "percentage",
            "percentage": "70.00"
            },
            {
            "user": "c2721618-6cc2-4494-831c-5f86e4802eb0",
            "amount": "150.00",
            "share_type": "percentage",
            "percentage": "30.00"
            }
        ]
        }
    ]
    }
    }

### GET /balance-sheet/download/
- **Download Balance-Sheet**
    

