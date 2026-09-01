class Notification:
    def send(self, message):
        print(f"General Notification: {message}")

class EmailNotification(Notification):
    # Override send()
    def send(self, message):
        print(f"Email Notification: {message}")

# Take input
message = input("Enter your message: ").strip()

# Create both objects and call send()
general = Notification()
general.send(message)

email = EmailNotification()
email.send(message)
