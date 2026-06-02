# This is the central data model for entire session recovery module.

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class SessionState:
    """
    Stores session progress information.
    """

    session_id: str
    current_step: int = 0
    status: str = "active"  # active, paused, completed

    partial_chunks: List[int] = field(default_factory=list)

    last_stream_position: int = 0

    total_steps: Optional[int] = None

    def to_dict(self) -> dict:
        return {
            "session_id": self.session_id,
            "current_step": self.current_step,
            "status": self.status,
            "partial_chunks": self.partial_chunks,
            "last_stream_position": self.last_stream_position,
            "total_steps": self.total_steps,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            session_id=data["session_id"],
            current_step=data.get("current_step", 0),
            status=data.get("status", "active"),
            partial_chunks=data.get("partial_chunks", []),
            last_stream_position=data.get("last_stream_position", 0),
            total_steps=data.get("total_steps"),
        )