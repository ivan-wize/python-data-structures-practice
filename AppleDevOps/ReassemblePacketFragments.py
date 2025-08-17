# =============================================================
# 2) Reassemble Packet Fragments
# Problem:
#   Given fragments (msg_id, seq, payload), reassemble into bytes.
#   Must be contiguous 0..n-1 for exactly one message_id.
# Example: [(7,0,b"HEL"), (7,1,b"LO")] -> b"HELLO"
# =============================================================
def reassemble(fragments: list[tuple[int, int, bytes]]) -> bytes | None:
    if not fragments: return b""
    ids = {mid for mid, _, _ in fragments}
    if len(ids) != 1: return None          # more than one msg_id
    parts = {}
    for _, seq, payload in fragments:
        if seq in parts: return None       # duplicate sequence
        parts[seq] = payload
    n = len(parts)
    if set(parts.keys()) != set(range(n)): # must be contiguous
        return None
    return b"".join(parts[i] for i in range(n))  # join in order
