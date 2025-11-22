## 1. Problem Statement
The goal is to create a basic, functional prototype of a booking system to simulate the core logic of a real-world reservation application. The primary problem addressed is the need for a mechanism to **search available inventory** (flights) and **manage seat availability** during the booking process. This project serves as a practical application to demonstrate understanding of fundamental data structures, loops, and conditional logic in Python.

## 2. Scope of the Project
The scope of this project is limited to a command-line interface (CLI) application that operates using **in-memory data**.
* **In-Scope:** Implementing search logic based on origin, destination, and date; managing seat availability by decrementing counts upon successful booking; recording booking details (ID, flight code, name); and displaying simple menu navigation.
* **Out-of-Scope:** Integration with external databases, network communication, payment processing, user authentication, advanced error handling, date/time validation, or graphical user interface (GUI).

## 3. Target Users
The primary target users are those who wish to quickly simulate or test basic flight booking transactions in a non-production environment.
* **Engineering Students/Developers:** For learning, practicing, and demonstrating mastery of fundamental programming constructs (lists, dictionaries, loops, and conditionals).
* **System Testers:** To manually verify the core business logic of seat allocation and booking confirmation without needing a complex backend.

## 4. High-Level Features
1.  **Search Flights:** Allow users to filter the available flight inventory based on route and travel date.
2.  **Book Reservation:** Process a booking request, assign a unique booking ID, and update the flight inventory in memory.
3.  **Inventory Check:** Enforce seat limitations by ensuring a flight cannot be booked if the seat count is zero.
4.  **View History:** Provide a simple readout of all tickets successfully booked during the current session.
