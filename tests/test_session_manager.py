from src.session_recovery.session_manager import SessionManager


def test_create_session():
    manager = SessionManager()

    session = manager.create_session(
        "test_session",
        total_steps=10
    )

    assert session.session_id == "test_session"
    assert session.current_step == 0
    assert session.status == "active"


def test_update_progress():
    manager = SessionManager()

    manager.create_session("progress_test")

    session = manager.update_progress(
        "progress_test",
        5
    )

    assert session.current_step == 5


def test_pause_resume():
    manager = SessionManager()

    manager.create_session("pause_test")

    manager.pause_session("pause_test")

    session = manager.get_session("pause_test")

    assert session.status == "paused"

    manager.resume_session("pause_test")

    session = manager.get_session("pause_test")

    assert session.status == "active"


def test_complete_session():
    manager = SessionManager()

    manager.create_session("complete_test")

    session = manager.complete_session(
        "complete_test"
    )

    assert session.status == "completed"