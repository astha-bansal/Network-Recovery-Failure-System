from src.recovery_controller import RecoveryController

controller = RecoveryController()

data = controller.recover_session(
    "demo_session"
)

print("\nRecovered Session:\n")
print(data)