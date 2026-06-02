import time


class ReconnectManager:

    def reconnect(
        self,
        monitor,
        max_attempts=5
    ):

        for attempt in range(max_attempts):

            if monitor.is_connected():
                print("Connection restored")
                return True

            print(
                f"Reconnect attempt "
                f"{attempt + 1}"
            )

            time.sleep(2)

        return False