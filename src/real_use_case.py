import dill
from uuid import uuid4, UUID
from typing import Generator

class DB:
    """A template for the database class that will be used to store the generator bytes."""
    runners: dict[UUID, bytes] = {}

    @staticmethod
    def insert(runner_id: UUID, gen_bytes: bytes) -> None:
        """Insert the generator bytes into the database with the runner_id as the key."""
        DB.runners[runner_id] = gen_bytes

    @staticmethod
    def select(runner_id: UUID) -> bytes | None:
        """Select the generator bytes from the database using the runner_id as the key."""
        return DB.runners.get(runner_id, None)

def request_os(runner_id: UUID) -> None:
    """Send a request to the host to tell its OS."""
    pass

def request_new_file_linux(runner_id: UUID) -> None:
    """Send a request to the host to create a new file in the Linux way."""
    pass

def request_new_file_windows(runner_id: UUID) -> None:
    """Send a request to the host to create a new file in the Windows way."""
    pass

def create_file() -> Generator[UUID, str, None]:
    """Generator function that creates a new file on the host."""
    runner_id = uuid4()
    request_os(runner_id)
    os = yield runner_id
    if os == "linux":
        request_new_file_linux(runner_id)
    else:
        request_new_file_windows(runner_id)

def start_algo() -> None:
    """Run the algorithm until the first yield and store the generator bytes."""
    gen = create_file()
    runner_id = next(gen)
    gen_bytes = dill.dumps(gen)
    DB.insert(runner_id, gen_bytes)

def continue_algo(runner_id, result) -> None:
    """Continue the algorithm by loading the generator bytes from the database."""
    gen_bytes = DB.select(runner_id)
    if gen_bytes is not None:
        gen = dill.loads(gen_bytes)
        gen.send(result)

if __name__ == "__main__":
    try:
        start_algo()
        continue_algo("12345678-1234-1234-1234-123456789012", "linux")
    except TypeError as e:
        # generator object is not serializable
        print(f"Processing error: {e}")
