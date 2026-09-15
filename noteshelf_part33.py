# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: NoteShelf
DEFAULT_SETTINGS = {
    'theme': 'light',
    'font_size': 14,
    'auto_save': True,
    'search_case_sensitive': False,
    'max_notes_display': 10,
    'enable_notifications': False,
    'backup_enabled': False,
    'backup_path': 'backups/',
}


def get_setting(key, default=None):
    settings = _load_settings()
    return settings.get(key, default) if default is not None else settings.get(key, DEFAULT_SETTINGS.get(key))


def set_setting(key, value):
    settings = _load_settings()
    settings[key] = value
    _save_settings(settings)


def reset_settings():
    settings = dict(DEFAULT_SETTINGS)
    _save_settings(settings)


def _load_settings():
    settings_path = 'settings.json'
    try:
        with open(settings_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _save_settings(data):
    settings_path = 'settings.json'
    with open(settings_path, 'w') as f:
        json.dump(data, f, indent=2)
