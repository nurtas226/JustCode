class Feedback:
    def __init__(self):
        self.feedbacks = []

    def collect_feedback(self, room_number, rating, comment):
        if not (1 <= rating <= 5):
            print("Rating should be between 1 and 5.")
            return

        feedback = {
            'room_number': room_number,
            'rating': rating,
            'comment': comment
        }
        self.feedbacks.append(feedback)
        print("Thank you for your feedback!")

    def display_feedback(self):
        if not self.feedbacks:
            print('----------------------')
            print("No feedback available yet.")
            return
        
        print('----------------------')
        print("Guest Feedbacks:")
        for feedback in self.feedbacks:
            print(f"Room {feedback['room_number']}: Rating - {feedback['rating']}[1-5], Comment - {feedback['comment']}")