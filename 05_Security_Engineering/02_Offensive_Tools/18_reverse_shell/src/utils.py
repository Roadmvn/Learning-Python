"""
Shared Utilities
Common functions for reverse shell project
"""

def print_binary(data: bytes, max_bytes: int = 16) -> str:
    """
    Format binary data for display
    
    Args:
        data: Binary data to format
        max_bytes: Maximum bytes to display
    
    Returns:
        Formatted hex string
    """
    return ' '.join(f'{b:02x}' for b in data[:max_bytes])


def print_banner():
    """Print warning banner"""
    banner = """
╔═══════════════════════════════════════════════════════════════╗
║                       ⚠️  AVERTISSEMENT  ⚠️                     ║
╠═══════════════════════════════════════════════════════════════╣
║  Cet outil est destiné à des fins éducatives uniquement.     ║
║  Utilisation non autorisée sur des systèmes tiers est        ║
║  ILLÉGALE et peut entraîner des poursuites judiciaires.      ║
║                                                               ║
║  Assurez-vous d'avoir une autorisation écrite avant          ║
║  d'utiliser cet outil sur tout système.                      ║
╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def validate_ip(ip: str) -> bool:
    """
    Validate IP address format
    
    Args:
        ip: IP address string
    
    Returns:
        True if valid, False otherwise
    """
    try:
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        return all(0 <= int(part) <= 255 for part in parts)
    except (ValueError, AttributeError):
        return False


def validate_port(port: int) -> bool:
    """
    Validate port number
    
    Args:
        port: Port number
    
    Returns:
        True if valid, False otherwise
    """
    return 1 <= port <= 65535
