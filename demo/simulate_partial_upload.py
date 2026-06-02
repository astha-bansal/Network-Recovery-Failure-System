from src.recovery_controller import RecoveryController

controller = RecoveryController()

session_id = "upload_demo"

controller.start_session(session_id)

controller.mark_partial_chunk(
    session_id,
    10
)

controller.mark_partial_chunk(
    session_id,
    11
)

print(
    controller.recover_partial_chunks(
        session_id
    )
)