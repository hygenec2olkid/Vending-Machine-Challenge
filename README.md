## 🌟 Vending Machine Challenge

A simulation of a simple vending machine that handles product selection, stock management, and currency transactions using **THB (Thai Baht)**.

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
    git clone [YOUR_REPO_URL]
    ```
2.  **Navigate to the Backend Directory:**
    ```bash
    cd backend
    ```
3.  **Build and Run the Containers:**
    ```bash
    docker compose up --build
    ```

---

## 🌐 Live Demo

You can see the result of the backend logic integrated into a frontend application here:

👉 **[https://vending-machine-challenge-n1jk.vercel.app/](https://vending-machine-challenge-n1jk.vercel.app/)**

---

## 🚀 Technologies Used

* **Backend:** [e.g., Go, Python, Java]
* **Containerization:** Docker, Docker Compose
* **Framework/Libraries:** [e.g., Gin Gonic, Spring Boot]

---

## 🗺️ System Design Overview

The system processes transactions through a central controller. The key logic resides in the **Change Calculation Algorithm**, which iterates through available currency denominations (1000, 500, 100, 50, 20, 10, 5, 1 THB) to determine if the exact change can be made using the machine's current cash reserves. If change is possible, the reserves are updated; otherwise, the transaction is rejected, preventing the machine from getting stuck.

---

## ✍️ Author

[Your Name] - [Link to your GitHub Profile or LinkedIn]
