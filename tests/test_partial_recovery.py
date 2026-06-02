from src.session_recovery.session_manager import SessionManager
from src.session_recovery.partial_recovery import PartialRecovery


def test_mark_partial_chunk():

    manager = SessionManager()
    recovery = PartialRecovery()

    manager.create_session("partial_test")

    recovery.mark_partial_chunk(
        "partial_test",
        5
    )

    chunks = recovery.recover_partial_chunks(
        "partial_test"
    )

    assert 5 in chunks


def test_recover_chunk():

    manager = SessionManager()
    recovery = PartialRecovery()

    manager.create_session("recover_test")

    recovery.mark_partial_chunk(
        "recover_test",
        7
    )

    recovery.mark_chunk_recovered(
        "recover_test",
        7
    )

    chunks = recovery.recover_partial_chunks(
        "recover_test"
    )

    assert 7 not in chunks