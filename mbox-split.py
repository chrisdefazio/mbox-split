import mailbox
import os
import time

INPUT_MBOX = "/path/to/mail.mbox"
OUTPUT_DIR = "mbox_chunks"
MESSAGES_PER_CHUNK = 5000
PROGRESS_EVERY = 1000

os.makedirs(OUTPUT_DIR, exist_ok=True)

start_time = time.time()

print(f"Opening mbox: {INPUT_MBOX}")
mbox = mailbox.mbox(INPUT_MBOX)
mbox.lock()

chunk_count = 0
message_count = 0
total_messages = 0
out_mbox = None

try:
    for i, message in enumerate(mbox, 1):
        if message_count == 0:
            if out_mbox:
                out_mbox.flush()
            chunk_filename = os.path.join(OUTPUT_DIR, f"chunk_{chunk_count:03}.mbox")
            out_mbox = mailbox.mbox(chunk_filename)
            print(f"\n[+] Creating new chunk: {chunk_filename}")

        out_mbox.add(message)
        message_count += 1
        total_messages += 1

        if total_messages % PROGRESS_EVERY == 0:
            elapsed = time.time() - start_time
            print(f"[{total_messages} messages processed in {elapsed:.1f} seconds]")

        if message_count >= MESSAGES_PER_CHUNK:
            out_mbox.flush()
            message_count = 0
            chunk_count += 1

    # Final flush
    if out_mbox:
        out_mbox.flush()

finally:
    mbox.unlock()

elapsed = time.time() - start_time
print(f"\n✅ Done. {total_messages} messages processed into {chunk_count + 1} chunks in {elapsed:.1f} seconds.")
