import socket


class ConnectionMonitor:

    @staticmethod
    def is_connected(host="8.8.8.8", port=53, timeout=3):
        try:
            socket.create_connection((host, port), timeout=timeout)
            return True
        except OSError:
            return False