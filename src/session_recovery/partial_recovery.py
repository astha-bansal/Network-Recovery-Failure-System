from src.session_recovery.state_store import StateStore


class PartialRecovery:
    """
    Handles recovery of partially processed chunks.
    """

    def __init__(self):
        self.store = StateStore()

    def mark_partial_chunk(
        self,
        session_id: str,
        chunk_id: int
    ) -> None:
        """
        Mark a chunk as partially uploaded/processed.
        """

        session = self.store.load_state(session_id)

        if chunk_id not in session.partial_chunks:
            session.partial_chunks.append(chunk_id)

        self.store.save_state(session)

    def recover_partial_chunks(
        self,
        session_id: str
    ) -> list[int]:
        """
        Return all chunks needing recovery.
        """

        session = self.store.load_state(session_id)

        return session.partial_chunks

    def mark_chunk_recovered(
        self,
        session_id: str,
        chunk_id: int
    ) -> None:
        """
        Remove chunk after successful recovery.
        """

        session = self.store.load_state(session_id)

        if chunk_id in session.partial_chunks:
            session.partial_chunks.remove(chunk_id)

        self.store.save_state(session)

    def clear_partial_chunks(
        self,
        session_id: str
    ) -> None:
        """
        Clear all partial chunks.
        """

        session = self.store.load_state(session_id)

        session.partial_chunks.clear()

        self.store.save_state(session)