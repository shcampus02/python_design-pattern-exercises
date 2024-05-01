# Global applications often need to handle date and time data across different time zones. Direct conversion between
# time zones can clutter business logic. An adapter can simplify this by converting times between the source and
# target time zones transparently, allowing the core application to operate in a single, consistent time zone.

# Create an adapter that translates times between different time zones. This could be used in scheduling applications
# that manage events across global offices.








if __name__ == '__main__':
    scheduler = Scheduler()
    timezone_adapter = TimeZoneAdapter(scheduler, "UTC", "PST")

    # Schedule an event in PST using UTC time
    scheduler.schedule_event("Meeting", "2024-06-01 14:00:00", "UTC")
    timezone_adapter.display_event_in_local_time("Meeting", "2024-06-01 14:00:00")


