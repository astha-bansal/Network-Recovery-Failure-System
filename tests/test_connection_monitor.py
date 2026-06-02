from src.network_recovery.connection_monitor import ConnectionMonitor


def test_connection_check():

    result = ConnectionMonitor.is_connected()

    assert isinstance(result, bool)