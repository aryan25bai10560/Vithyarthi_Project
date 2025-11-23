
flights_database = [
    ["FLY101", "DEL", "BOM", "2026-06-10", 5500.00, 20],
    ["IND202", "BOM", "BLR", "2026-06-10", 4100.00, 5],
    ["AIR303", "DEL", "MAA", "2026-06-11", 7200.50, 50],
    ["FLY102", "DEL", "BOM", "2026-06-10", 6000.00, 0] 
]


my_bookings = []
current_booking_id = 9001 


print("\n=== Welcome to the Simplistic Flight Booker v1 ===")


while True:
    print("\n-------------------------------------------")
    print("1. Search Flights")
    print("2. Book a Flight")
    print("3. View My Bookings")
    print("4. Exit")
    print("-------------------------------------------")
    
    choice = input("Enter your choice (1, 2, 3, or 4): ")
    
    
    if choice == '1':
        print("\n--- Search Module ---")
        
        start_city = input("Enter Origin City Code (e.g., DEL): ").upper().strip()
        end_city = input("Enter Destination City Code (e.g., BOM): ").upper().strip()
        travel_date = input("Enter Date (YYYY-MM-DD): ").strip()
        
        found_count = 0
        
        print("\nSearching...")
        
       
        for flight in flights_database:
           
            if (flight[1] == start_city and 
                flight[2] == end_city and 
                flight[3] == travel_date and 
                flight[5] > 0): 
                
                print(f" Found! Code: {flight[0]} | Price: ₹{flight[4]:.2f} | Seats Left: {flight[5]}")
                found_count += 1
        
        
        if found_count == 0:
            print(" No available flights found for this route and date.")
            
    elif choice == '2':
        print("\n--- Booking Module ---")
        book_code = input("Enter Flight Code you want to book: ").upper().strip()
        passenger_name = input("Enter YOUR NAME: ").strip()
        
        is_booked = False
        
        
        for flight in flights_database:
            if flight[0] == book_code:
                
                if flight[5] > 0:
                    flight[5] -= 1 
                    
                    
                    booking_id = f"BK{current_booking_id}"
                    my_bookings.append([booking_id, book_code, passenger_name])
                    current_booking_id += 1
                    
                    print(f"\n Success! Booked {passenger_name} on {book_code}")
                    print(f"Your Booking ID is: {booking_id}")
                    is_booked = True
                    break 
                else:
                    print(f"\n Sorry, Flight {book_code} is sold out!")
                    is_booked = True
                    break
        
       
        if not is_booked:
            print(" Error: That Flight Code was not found in our system.")
            
    elif choice == '3':
        print("\n--- Your Booking History ---")
        if not my_bookings:
            print("You haven't booked anything yet!")
        else:
            
            for record in my_bookings:
                print(f"Ticket ID: {record[0]} | Flight: {record[1]} | Name: {record[2]}")
                
    elif choice == '4':
        print("\nThank you for using the Flight Booker. Program Exiting.")
        break 
        
    else:
        print("\n Invalid input. Please enter 1, 2, 3, or 4.")