# Develop a notification system that can send notifications via different methods (e.g., email, SMS, push notification).

# Scenario: Notification systems need to deliver messages through various channels depending on user preferences or
# cost considerations, including emails, SMS, or push notifications.
#
# Explanation: Using the Bridge pattern, the notification sending mechanism is decoupled from the implementation of
# each notification method. This setup makes it easy to extend the system with new notification methods without
# changing the core logic, supporting open/closed principle adherence.







if __name__ == '__main__':
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()

    alert_system = AlertSystem(email_notifier)
    alert_system.send_alert("Server down!")

    alert_system.switch_method(sms_notifier)
    alert_system.send_alert("Server still down!")

