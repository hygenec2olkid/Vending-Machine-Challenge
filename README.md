## 🌟 Vending Machine Challenge

A simulation of a simple vending machine that handles product selection, stock management, and currency transactions using.

---

## 🎯 The Problem

This project addresses the core functionalities of a standard vending machine, focusing on robust transaction logic and inventory management.

### Key Requirements

* **Currency Acceptance:** The machine must accept the following Thai currency denominations:
    * **Coins:** 1, 5, 10 THB
    * **Banknotes:** 20, 50, 100, 500, 1,000 THB
* **Product Selection:** Users must be able to select items from the available stock.
* **Transaction Logic:** The system must validate a purchase based on three crucial conditions:
    1.  **Sufficient Funds:** The inserted money covers the product cost.
    2.  **Change Availability:** The machine has the necessary coins/banknotes to return the exact change.
    3.  **Stock Availability:** The selected product is in stock.
* **System Update:** Upon a successful transaction, the system must:
    * Return the calculated change to the customer.
    * Adjust the product stock (decrement).
    * Adjust the vending machine's currency stock (increment inserted money, decrement returned change).

---

## 🛠️ How to Run Locally

You can easily set up and run the backend of this project using **Docker Compose**.

### Prerequisites

* [**Git**](https://git-scm.com/)
* [**Docker**](https://www.docker.com/products/docker-desktop)

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/hygenec2olkid/Vending-Machine-Challenge.git
    ```
2.  **Navigate to the Backend Directory:**
    ```bash
    cd backend
    ```
3.  **Build and Run the Containers:**
    ```bash
    docker compose up --build
    ```
4.  **Access the Running Application:** The API will be accessible on your host machine.

---

## 📝 API Documentation

Once the Docker containers are running (see the steps above), you can view the complete API documentation (likely Swagger/OpenAPI) at the following address:

🔗 **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## 🌐 Live Demo

You can see the result of the backend logic integrated into a frontend application here:

👉 **[https://vending-machine-challenge-n1jk.vercel.app/](https://vending-machine-challenge-n1jk.vercel.app/)**
