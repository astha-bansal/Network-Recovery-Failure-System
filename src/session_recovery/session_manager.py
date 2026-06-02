from src.models import SessionState
from src.session_recovery.state_store import StateStore


class SessionManager:
    """
    Handles session lifecycle and progress tracking.
    """

    def __init__(self):
        self.store = StateStore()

    def create_session(
        self,
        session_id: str,
        total_steps: int | None = None
    ) -> SessionState:

        session = SessionState(
            session_id=session_id,
            current_step=0,
            status="active",
            total_steps=total_steps
        )

        self.store.save_state(session)

        return session

    def update_progress(
        self,
        session_id: str,
        current_step: int
    ) -> SessionState:

        session = self.store.load_state(session_id)

        session.current_step = current_step

        self.store.save_state(session)

        return session

    def pause_session(self, session_id: str) -> SessionState:

        session = self.store.load_state(session_id)

        session.status = "paused"

        self.store.save_state(session)

        return session

    def resume_session(self, session_id: str) -> SessionState:

        session = self.store.load_state(session_id)

        session.status = "active"

        self.store.save_state(session)

        return session

    def complete_session(self, session_id: str) -> SessionState:

        session = self.store.load_state(session_id)

        session.status = "completed"

        self.store.save_state(session)

        return session

    def get_session(self, session_id: str) -> SessionState:

        return self.store.load_state(session_id)

    def delete_session(self, session_id: str) -> None:

        self.store.delete_state(session_id)