from client.event import StatusUploadEvent

if __name__ == "__main__":
    event_status = StatusUploadEvent(1, 'status_bus', 1)
    event_status.start()
