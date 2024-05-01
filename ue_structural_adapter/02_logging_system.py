# Integrate a new logging system into an existing application that uses a different logging interface.
# Create an adapter that allows the old system to use the new logger without changing the existing codebase.

# In many applications, logging is a critical functionality for monitoring and debugging. If an organization decides
# to switch to a more advanced logging system, adapting all the old logging calls to the new system can be daunting
# and error-prone. An adapter can be created to interface the new logging methods with the old system's calls,
# allowing seamless integration without altering existing code.







if __name__ == '__main__':
    old_logger = OldLogger()
    new_logger = NewLogger()
    logger_adapter = LoggerAdapter(new_logger)  # Adapts NewLogger to OldLogger interface

    # Old code using the adapter with new logger
    old_logger.log("This is a log message.")
    logger_adapter.log("This is a log message using the new logger.")
