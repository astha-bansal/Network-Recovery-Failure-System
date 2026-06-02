from src.models import SessionState
from src.session_recovery.state_store import StateStore


def test_save_load_state():

    store = StateStore()

    session = SessionState(
        session_id="store_test",
        current_step=10
    )

    store.save_state(session)

    loaded = store.load_state(
        "store_test"
    )

    assert loaded.session_id == "store_test"
    assert loaded.current_step == 10


def test_session_exists():

    store = StateStore()

    session = SessionState(
        session_id="exists_test"
    )

    store.save_state(session)

    assert store.session_exists(
        "exists_test"
    )