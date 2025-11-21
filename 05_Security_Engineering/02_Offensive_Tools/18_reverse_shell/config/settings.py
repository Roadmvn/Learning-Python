"""
Configuration Settings
Centralized configuration for reverse shell
"""

# Network Settings
DEFAULT_PORT = 4444
DEFAULT_HOST = "0.0.0.0"
BUFFER_SIZE = 4096

# Timeouts
COMMAND_TIMEOUT = 30  # seconds
CONNECTION_TIMEOUT = 60  # seconds

# Persistence
MAX_RECONNECT_ATTEMPTS = -1  # -1 = infinite
RECONNECT_DELAY_BASE = 1  # seconds
RECONNECT_DELAY_MAX = 60  # seconds

# Obfuscation
USE_BASE64 = False
USE_XOR = False
XOR_KEY = b'\xAA'

# Logging
ENABLE_LOGGING = True
LOG_FILE = "reverse_shell.log"
