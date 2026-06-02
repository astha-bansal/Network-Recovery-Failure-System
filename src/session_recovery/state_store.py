import json
from pathlib import Path

from src.models import SessionState


class StateStore:
    """
    Handles persistence of session states.
    Stores each session as a JSON file.
    """

    def __init__(self, storage_dir="sessions"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(exist_ok=True)

    def _get_file_path(self, session_id: str) -> Path:
        return self.storage_dir / f"{session_id}.json"

    def save_state(self, session: SessionState) -> None:
        """
        Save session state to disk.
        """
        file_path = self._get_file_path(session.session_id)

        with open(file_path, "w") as file:
            json.dump(session.to_dict(), file, indent=4)

    def load_state(self, session_id: str) -> SessionState:
        """
        Load session state from disk.
        """
        file_path = self._get_file_path(session_id)

        if not file_path.exists():
            raise FileNotFoundError(
                f"Session '{session_id}' not found."
            )

        with open(file_path, "r") as file:
            data = json.load(file)

        return SessionState.from_dict(data)

    def delete_state(self, session_id: str) -> None:
        """
        Delete session state file.
        """
        file_path = self._get_file_path(session_id)

        if file_path.exists():
            file_path.unlink()

    def session_exists(self, session_id: str) -> bool:
        """
        Check whether session exists.
        """
        return self._get_file_path(session_id).exists()