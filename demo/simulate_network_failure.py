from src.recovery_controller import RecoveryController

controller = RecoveryController()

session_id = "demo_session"

controller.start_session(
    session_id,
    total_steps=10
)

for step in range(1, 6):
    controller.save_progress(
        session_id,
        step
    )

controller.mark_partial_chunk(
    session_id,
    5
)

controller.save_stream_checkpoint(
    session_id,
    50
)

controller.pause_session(
    session_id
)

print("Network Failure Simulated")