def calculate_ticket_price():
    print("Enter your age & showtime below to know the ticket price.")
    print("Note: There is a 10% discount available for all shows before 5:00 PM (1700).\n")
    
    while True:
        try:
            # Get user input for age
            while True:
                try:
                    age = int(input("Type your age (only in numbers): "))
                    if age <= 0 or age > 200:
                        raise ValueError("Age must be a positive integer and less than or equal to 200.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")
                    print("Please try again.\n")
            
            # Get user input for showtime with an example
            while True:
                try:
                    showtime = input("Enter the showtime (in HHMM format, Example- 1645 for 4:45 PM): ")
                    if len(showtime) != 4 or not showtime.isdigit():
                        raise ValueError("Please provide the showtime in the correct format (HHMM).")
                    
                    # Split the showtime into hours and minutes
                    hours = int(showtime[:2])
                    minutes = int(showtime[2:])
                    
                    # Validate hours and minutes
                    if not (0 <= hours <= 23) or not (0 <= minutes <= 59):
                        raise ValueError("Please provide the showtime in the correct format (HHMM).")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")
                    print("Please try again.\n")
            
            # Convert 24-hour format to 12-hour format with AM/PM
            period = "AM" if hours < 12 else "PM"
            hours_12 = hours % 12
            if hours_12 == 0:
                hours_12 = 12
            
            showtime_12h = f"{hours_12}:{minutes:02d} {period}"
            
            # Display the user's inputs
            print(f"\nYou have entered:\nAge: {age}\nShowtime: {showtime} ({showtime_12h})\n")
            
            # Determine base price based on age
            if age <= 10:
                base_price = 300
            elif 11 <= age <= 25:
                base_price = 500
            elif 26 <= age <= 60:
                base_price = 800
            else:
                base_price = 400
            
            # Determine discount based on showtime
            if hours < 17:
                discount = base_price * 0.10
                discounted_price = base_price - discount
                # Print the output with discount
                print(f"Ticket price: {base_price} BDT\nDiscount: {discount:.2f} BDT\nDiscounted price: {discounted_price:.2f} BDT")
            else:
                # Print the output without discount
                print(f"Ticket price: {base_price} BDT")
            break
        
        except ValueError as e:
            print(f"\nInvalid input: {e}")
            print("Please try again.\n")

# Run the function
calculate_ticket_price()
