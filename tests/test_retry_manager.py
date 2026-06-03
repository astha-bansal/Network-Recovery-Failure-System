from src.network_recovery.retry_manager import RetryManager


def test_retry_success():

    retry = RetryManager()

    result = retry.retry(
        lambda: "success"
    )

    assert result == "success"