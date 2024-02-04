from occupied import Occupied
from feedbacks import Feedback

user_checkin = Occupied()
user_feedback = Feedback()


while True:
            print("----------------------")
            print("Welcome to Pleasure Hotel!")
            print('----------------------')
            print("1. Check-in")
            print("2. Room service")
            print("3. Display Occupied Rooms")
            print("4. Check-out")
            print("5. Collect Feedback")
            print("6. Display Feedback")
            print("7. Exit")
            choice = input("Enter a number [1-7]: ")
            print('----------------------')
            
            if choice == '1':
                name = input("Enter your name: ")
                phone = input("Enter contact number: ")
                user_checkin.check_in(name, phone)
            elif choice == '2':
                room_number = int(input("Enter room number: "))
                user_checkin.room_service(room_number)
            elif choice == '3':
                user_checkin.display_occupied()
            elif choice == '4':
                room_number = int(input("Enter room number: "))
                user_checkin.check_out(room_number)
            elif choice == '5':
                room_number = int(input("Enter your room number: "))
                rating = int(input("Rate your stay (1-5): "))
                comment = input("Please leave your comments: ")
                user_feedback.collect_feedback(room_number, rating, comment)
            elif choice == '6':
                user_feedback.display_feedback()
            elif choice == '7':
                break
            else:
                print("Undefined option. Please try again!")