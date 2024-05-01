# Goal: Implement a Logger class that ensures only one instance of the logger is ever created, preserving the
# sequence and content of log messages throughout the application lifecycle.
#
# Explanation: This exercise demonstrates the use of the Singleton pattern in scenarios where consistent access to a
# single resource (in this case, a log buffer) is crucial across different parts of an application. By making the
# Logger a Singleton, all parts of the application append to the same log, which helps in debugging and monitoring
# application behavior in a consistent manner.







if __name__ == '__main__':
    logger1 = Logger()
    logger2 = Logger()
    logger1.log("Starting system...")
    logger2.log("System started.")

    print(logger1 == logger2)  # Should output: True
    print(logger1.show_logs())  # Should include messages from both logger1 and logger2
