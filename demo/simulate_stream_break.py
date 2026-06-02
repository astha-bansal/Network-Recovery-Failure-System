from src.recovery_controller import RecoveryController

controller = RecoveryController()

session_id = "stream_demo"

controller.start_session(session_id)

controller.save_stream_checkpoint(
    session_id,
    50
)

print(
    "Resume From:",
    controller.resume_stream(session_id)
)