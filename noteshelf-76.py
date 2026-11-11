# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: NoteShelf
try:
    main()
except KeyboardInterrupt:
    print("\nNoteShelf exited. Goodbye!")
    sys.exit(0)
