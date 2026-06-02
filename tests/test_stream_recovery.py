from src.session_recovery.session_manager import SessionManager
from src.session_recovery.stream_recovery import StreamRecovery


def test_save_checkpoint():

    manager = SessionManager()
    stream = StreamRecovery()

    manager.create_session("stream_test")

    stream.save_checkpoint(
        "stream_test",
        25
    )

    assert (
        stream.get_last_checkpoint(
            "stream_test"
        ) == 25
    )


def test_resume_stream():

    manager = SessionManager()
    stream = StreamRecovery()

    manager.create_session("resume_stream")

    stream.save_checkpoint(
        "resume_stream",
        100
    )

    assert (
        stream.resume_stream(
            "resume_stream"
        ) == 100
    )