from src.session_recovery.session_manager import SessionManager
from src.session_recovery.partial_recovery import PartialRecovery
from src.session_recovery.stream_recovery import StreamRecovery


class RecoveryController:
    """
    Main controller for session recovery operations.
    """

    def __init__(self):
        self.session_manager = SessionManager()
        self.partial_recovery = PartialRecovery()
        self.stream_recovery = StreamRecovery()

    def start_session(
        self,
        session_id: str,
        total_steps: int | None = None
    ):
        """
        Create a new session.
        """
        return self.session_manager.create_session(
            session_id,
            total_steps
        )

    def save_progress(
        self,
        session_id: str,
        step: int
    ):
        """
        Update session progress.
        """
        return self.session_manager.update_progress(
            session_id,
            step
        )

    def pause_session(
        self,
        session_id: str
    ):
        """
        Pause session.
        """
        return self.session_manager.pause_session(
            session_id
        )

    def resume_session(
        self,
        session_id: str
    ):
        """
        Resume session.
        """
        return self.session_manager.resume_session(
            session_id
        )

    def mark_partial_chunk(
        self,
        session_id: str,
        chunk_id: int
    ):
        """
        Register failed chunk.
        """
        self.partial_recovery.mark_partial_chunk(
            session_id,
            chunk_id
        )

    def recover_partial_chunks(
        self,
        session_id: str
    ):
        """
        Get chunks needing recovery.
        """
        return self.partial_recovery.recover_partial_chunks(
            session_id
        )

    def save_stream_checkpoint(
        self,
        session_id: str,
        position: int
    ):
        """
        Save stream position.
        """
        self.stream_recovery.save_checkpoint(
            session_id,
            position
        )

    def resume_stream(
        self,
        session_id: str
    ):
        """
        Get last stream checkpoint.
        """
        return self.stream_recovery.resume_stream(
            session_id
        )

    def recover_session(
        self,
        session_id: str
    ):
        """
        Load complete recovery information.
        """

        session = self.session_manager.get_session(
            session_id
        )

        return {
            "session_id": session.session_id,
            "status": session.status,
            "current_step": session.current_step,
            "partial_chunks": session.partial_chunks,
            "stream_position": session.last_stream_position
        }

    def complete_session(
        self,
        session_id: str
    ):
        """
        Mark session completed.
        """
        return self.session_manager.complete_session(
            session_id
        )