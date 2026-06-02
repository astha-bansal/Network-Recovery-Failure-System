from src.session_recovery.state_store import StateStore


class StreamRecovery:
    """
    Handles stream checkpointing and recovery.
    """

    def __init__(self):
        self.store = StateStore()

    def save_checkpoint(
        self,
        session_id: str,
        stream_position: int
    ) -> None:
        """
        Save current stream position.
        """

        session = self.store.load_state(session_id)

        session.last_stream_position = stream_position

        self.store.save_state(session)

    def get_last_checkpoint(
        self,
        session_id: str
    ) -> int:
        """
        Get last saved stream position.
        """

        session = self.store.load_state(session_id)

        return session.last_stream_position

    def resume_stream(
        self,
        session_id: str
    ) -> int:
        """
        Return position from which stream should resume.
        """

        session = self.store.load_state(session_id)

        return session.last_stream_position

    def reset_stream(
        self,
        session_id: str
    ) -> None:
        """
        Reset stream checkpoint.
        """

        session = self.store.load_state(session_id)

        session.last_stream_position = 0

        self.store.save_state(session)