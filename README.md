# Simplistic Flight Booker v1 (Python Console Application) ✈️

## 1. Project Title
**Simplistic Flight Booker v1**

## 2. Overview of the Project
This is a basic and a simple single line project made using numpy module where the project is of how to simply book flight tickets in python. The project demonstrates simple fundamentals skills used in python including **data handling using lists**, **menu-driven interaction using a `while` loop**, and **conditional logic (`if/elif/else` statements) and loops (`for` loops)** for searching and booking flights. All data gets stored in (RAM) and can be automatically regained after saving the file.

## 3. Features
* **Flight Database:** Maintains a simple list of available flights with details like codes, routes, prices, and available seats.
* **Search Functionality:** Allows users to search for flights based on **Origin City Code, Destination City Code, and Date**.
* **Booking Module:** Users can book a flight using the flight code, which **decrements the seat count** and records the booking.
* **Seat Availability Check:** Prevents double-booking by checking if seats are greater than zero before processing the transaction.
* **Booking History:** Allows the user to view a list of all successful, recorded bookings.
* **Menu System:** Uses a robust `while True` loop and an `if/elif` chain for easy navigation between modules.

## 4. Technologies/Tools Used
* **Programming Language:** Python (Code is compatible with Python 3.x)
* **Libraries:** `random` and `numpy` are imported.
* **Data Structures:** Python Lists (`flights_database`, `my_bookings`).
* **Tools:** Standard Python interpreter environment.

## 5. Steps to Install & Run the Project
Since this is a single, self-contained Python script, installation is minimal.
1.  **Open Terminal/Command Prompt:** Navigate to the directory where you saved the file.
3.  **Run the Script:** Execute the program using the Python interpreter:
    python flight_booker.py
4.  **Interaction:** The main menu will appear, and you can interact by entering the numbers 1, 2, 3, or 4.

## 6. Instructions for Testing

Test the following scenarios via the command line interface:
1.  **Search (Option 1):**
    * Test a route that **has available seats** (e.g., DEL to BOM on 2026-06-10, expecting **FLY101**).
    * Test a route that **has no seats** (e.g., DEL to BOM on 2026-06-10, but checking the full flight **FLY102** or a combination that yields no results).
2.  **Book (Option 2):**
    * Successfully book an available flight (**FLY101**). Check if the seat count is correctly reduced in the database after booking.
    * Attempt to book a flight that is **already sold out** (**FLY102**) and verify the "Sorry, Flight is sold out!" message appears.
    * Attempt to book a **non-existent** flight code.
3.  **View Bookings (Option 3):**
    * Verify that newly confirmed bookings appear in the history list.
    * Check that the program correctly reports "You haven't booked anything yet!" if no bookings have been made.
4.  **Exit (Option 4):** Verify that the program terminates gracefully using the `break` statement.

