# === Stage 44: Add backup creation for the data file ===
# Project: NoteShelf
def backup_datafile(filepath, backup_dir=None):
    if backup_dir is None:
        backup_dir = filepath.rsplit('/', 1)[0] + '_backups'
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'note_shelf_backup_{timestamp}.json')
    with open(filepath, 'r') as f:
        data = f.read()
    with open(backup_path, 'w') as f:
        f.write(data)
    print(f'Backup saved to {backup_path}')
    return backup_path
