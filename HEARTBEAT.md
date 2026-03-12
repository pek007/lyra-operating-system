# HEARTBEAT.md

Check interim product inboxes for pending cross-product coordination requests.

Use:
- `python3 tools/check_product_inboxes.py`

If there are open requests:
- surface the pending request IDs, products, and statuses,
- mention only items that are still open (`status != closed`),
- keep the summary compact,
- if there is no change since the last mention and nothing is urgent, reply `HEARTBEAT_OK`.

Do not treat the inbox as canonical execution state.
It is only an intake/coordination surface during the interim phase.
