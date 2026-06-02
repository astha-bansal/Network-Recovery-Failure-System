from src.network_recovery.reconnect_manager import ReconnectManager
from src.network_recovery.connection_monitor import ConnectionMonitor


def test_reconnect():

    reconnect = ReconnectManager()

    result = reconnect.reconnect(
        ConnectionMonitor(),
        max_attempts=1
    )

    assert isinstance(result, bool)