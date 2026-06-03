import time


class RetryManager:

    def retry(self, func, retries=3):

        for attempt in range(retries):
            try:
                return func()

            except Exception as e:

                wait_time = 2 ** attempt
                print(
                    f"Retry {attempt + 1}/{retries} "
                    f"after {wait_time}s"
                )

                time.sleep(wait_time)

        raise Exception("Maximum retries reached")