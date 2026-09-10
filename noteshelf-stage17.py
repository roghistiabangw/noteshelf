# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: NoteShelf
import json

def dry_run(command):
    """Simulate a state-changing command and return the projected result without modifying state.
    Returns a dict with keys: command, projected_result, dry_run=True, status='ok'.
    For unknown commands, returns status='error' with a generic message.
    """
    projected = {
        'command': command,
        'status': 'ok',
        'dry_run': True,
    }
    cmd = command.get('type', '')
    if cmd == 'create_note':
        projected['projected_result'] = {'title': command.get('title', 'Untitled'), 'tags': []}
    elif cmd == 'delete_note':
        projected['projected_result'] = {'deleted': True}
    elif cmd == 'update_note':
        projected['projected_result'] = {'updated': True, 'title': command.get('title', '')}
    elif cmd == 'create_folder':
        projected['projected_result'] = {'folder': command.get('name', 'New Folder')}
    elif cmd == 'pin_note':
        projected['projected_result'] = {'pinned': True}
    elif cmd == 'unpin_note':
        projected['projected_result'] = {'pinned': False}
    elif cmd == 'add_tag':
        projected['projected_result'] = {'tagged_with': command.get('tag', '')}
    elif cmd == 'search':
        projected['projected_result'] = {'results': [], 'count': 0}
    else:
        projected['status'] = 'error'
        projected['message'] = f'Unknown dry-run command: {cmd}'
    return projected
