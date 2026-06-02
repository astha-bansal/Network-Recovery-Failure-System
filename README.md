# Network Failure Recovery System

## Overview

The Network Failure Recovery System is a Python-based reliability module designed to recover gracefully from network interruptions. It provides mechanisms for automatic recovery, session continuation, partial upload recovery, and stream checkpoint restoration.

This project was developed as part of an internship task focused on building reliable systems capable of handling network failures without losing progress.

---

## Objectives

* Recover from network interruptions
* Support retry workflows
* Resume interrupted sessions
* Handle partial uploads
* Recover broken streams
* Maintain operation state across failures

---

## Features

### Session Recovery Module

* Persistent session storage
* Session continuation after interruption
* Progress tracking
* Pause and resume functionality
* Session completion tracking

### Partial Upload Recovery

* Detect incomplete uploads
* Track failed chunks
* Reprocess only affected chunks
* Avoid restarting entire operations

### Stream Recovery

* Stream checkpointing
* Restore stream position after interruption
* Resume processing from last checkpoint

### Network Recovery Module

>Implemented Features

Connection Monitoring
- Detects network connectivity status.
- Identifies network failures and connection interruptions.

Automatic Reconnection
- Attempts to restore connectivity after network failure.
- Supports configurable reconnection attempts.

Retry Workflows
- Retries failed operations automatically.
- Prevents immediate failure of transient network issues.

Exponential Backoff
- Increases retry delay exponentially after each failed attempt.
- Reduces unnecessary network load during outages.

Recovery Logging
- Logs network failures, retry attempts, and recovery events.
- Helps in debugging and monitoring recovery operations.

---

# Project Structure

```text
network-failure-recovery-system/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── sessions/
│   └── .gitkeep
│
├── logs/
│   └── .gitkeep
│
├── src/
│   │
│   ├── __init__.py
│   ├── models.py
│   ├── config.py
│   ├── recovery_controller.py
│   │
│   ├── network_recovery/
│   │   ├── __init__.py
│   │   ├── connection_monitor.py
│   │   ├── retry_manager.py
│   │   ├── reconnect_manager.py
│   │   └── recovery_logger.py
│   │
│   └── session_recovery/
│       ├── __init__.py
│       ├── state_store.py
│       ├── session_manager.py
│       ├── partial_recovery.py
│       └── stream_recovery.py
│
├── demo/
│   ├── simulate_network_failure.py
│   ├── simulate_partial_upload.py
│   └── simulate_stream_break.py
│
├── tests/
│   ├── test_state_store.py
│   ├── test_session_manager.py
│   ├── test_partial_recovery.py
│   ├── test_stream_recovery.py
│   ├── test_connection_monitor.py
│   ├── test_retry_manager.py
│   └── test_reconnect_manager.py
│
└── docs/
    ├── architecture.md
    ├── workflow.md
    └── screenshots/
```

---

# Installation

## Clone Repository

```bash
git clone <https://github.com/astha-bansal/Network-Recovery-Failure-System>
cd network-failure-recovery-system
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Session Recovery Module

## Components

### State Store

Responsible for:

* Saving session state
* Loading session state
* Deleting session state
* Session existence checks

### Session Manager

Responsible for:

* Session creation
* Progress updates
* Pause/Resume functionality
* Session completion

### Partial Recovery

Responsible for:

* Tracking incomplete chunks
* Chunk recovery
* Recovery state management

### Stream Recovery

Responsible for:

* Stream checkpoints
* Resume position tracking
* Stream restoration

---

# Network Recovery Module

> **Section Reserved for Team Member 2**

## Components

### Connection Monitor

Description:

*Add implementation details here.*

### Retry Manager

Description:

*Add implementation details here.*

### Reconnect Manager

Description:

*Add implementation details here.*

### Recovery Logger

Description:

*Add implementation details here.*

---

# Workflow

## Session Recovery Flow

```text
Start Session
      │
      ▼
Save Progress
      │
      ▼
Network Failure
      │
      ▼
Load Saved State
      │
      ▼
Resume Session
```

## Network Recovery Flow

> **To be completed by Team Member 2**

```text
Connection Active
      │
      ▼
Network Failure
      │
      ▼
Detect Failure
      │
      ▼
Reconnect
      │
      ▼
Resume Session
```

---

# Usage Examples

## Create Session

```python
from src.recovery_controller import RecoveryController

controller = RecoveryController()

controller.start_session(
    "session_1",
    total_steps=10
)
```

## Save Progress

```python
controller.save_progress(
    "session_1",
    5
)
```

## Recover Session

```python
data = controller.recover_session(
    "session_1"
)

print(data)
```

---

# Demo Scripts

## Simulate Network Failure

```bash
python demo/simulate_network_failure.py
```

## Simulate Partial Upload

```bash
python demo/simulate_partial_upload.py
```

## Simulate Stream Break

```bash
python demo/simulate_stream_break.py
```

---

# Testing

Run all tests:

```bash
pytest
```

Expected output:

```text
8 passed
```

---

# Edge Cases Handled

## Partial Uploads

Scenario:

```text
Chunk 10 Upload Failed
```

Recovery:

```text
Only Chunk 10 Reprocessed
```

---

## Broken Streams

Scenario:

```text
Processed 50 Messages
Network Failure
```

Recovery:

```text
Resume From Message 51
```

---

## Session Continuation

Scenario:

```text
Progress Saved At Step 5
Application Interrupted
```

Recovery:

```text
Resume From Step 6
```

---

# Architecture

## High-Level Architecture

```text
Application
      │
      ▼
Recovery Controller
      │
 ┌────┴────┐
 │         │
 ▼         ▼
Network    Session
Recovery   Recovery
Module     Module
```

---

# Future Improvements

* Database-backed session storage
* Distributed recovery support
* Real-time monitoring dashboard
* Web API integration
* Recovery analytics and metrics
* Cloud deployment support

---

# Contributors

## Team Member 1:Astha Bansal – Session Recovery Module

### Responsibilities

* Session persistence
* Session continuation
* Partial upload recovery
* Stream recovery
* Testing and documentation

---

## Team Member 2 – Network Recovery Module

### Responsibilities

* Connection monitoring
* Retry workflows
* Reconnection logic
* Exponential backoff
* Recovery logging

### Implementation Details

*Add implementation details here.*

### Challenges Faced

*Add challenges and solutions here.*

### Screenshots / Results

*Add screenshots here.*

---

# License

This project is developed for educational and internship purposes.
