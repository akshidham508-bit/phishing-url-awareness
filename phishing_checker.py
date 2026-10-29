
from urllib.parse import urlparse
import ipaddress


def check_url(url):
    """Check a URL for basic phishing warning signs."""
    warnings = []

    # Check 1: @ symbol
    if "@" in url:
        warnings.append("URL contains an @ symbol")

    # Check 2: Unusually long URL
    if len(url) > 75:
        warnings.append("URL is unusually long")

    # Parse URL and get hostname
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    # Check 3: IP address as hostname
    if hostname:
        try:
            ipaddress.ip_address(hostname)
            warnings.append("URL uses an IP address as the hostname")
        except ValueError:
            pass

    # Check 4: Too many hostname segments
    if hostname and len(hostname.split(".")) >= 5:
        warnings.append("URL has too many hostname segments")

    # Check 5: Punycode marker
    if hostname and "xn--" in hostname.lower():
        warnings.append("Hostname contains a Punycode marker")

    # Check 6: HTTP instead of HTTPS
    if parsed_url.scheme.lower() == "http":
        warnings.append("URL uses HTTP instead of HTTPS")

    return warnings


def main():
    url = input("Enter a URL to check: ").strip()
    warnings = check_url(url)

    print("\n--- URL Awareness Checker ---")

    if warnings:
        print("Warning signs found:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("No warning signs detected by these checks.")

    print("\nNote: This tool cannot prove whether a URL is safe.")


if __name__ == "__main__":
    main()
