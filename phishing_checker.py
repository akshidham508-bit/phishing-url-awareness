
from urllib.parse import urlparse
import ipaddress


def check_url(url):
    """Check a URL for basic phishing warning signs."""
    warnings = []

    if "@" in url:
        warnings.append("URL contains an @ symbol")

    if len(url) > 100:
        warnings.append("URL is unusually long")

    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    if hostname:
        try:
            ipaddress.ip_address(hostname)
            warnings.append("URL uses an IP address as the hostname")
        except ValueError:
            pass

    if hostname and len(hostname.split(".")) >= 5:
        warnings.append("URL has too many hostname segments")

    if hostname and "xn--" in hostname.lower():
        warnings.append("Hostname contains a Punycode marker")

    if parsed_url.scheme.lower() == "http":
        warnings.append("URL uses HTTP instead of HTTPS")

    return warnings


def main():
    explanations = {
        "URL contains an @ symbol":
            "The @ symbol can sometimes hide the real website address.",
        "URL is unusually long":
            "Very long URLs can make suspicious parts harder to notice.",
        "URL uses an IP address as the hostname":
            "The website uses a numerical address instead of a domain name.",
        "URL has too many hostname segments":
            "Many subdomains can make a website address confusing.",
        "Hostname contains a Punycode marker":
            "Some international characters can be used to imitate other domains.",
        "URL uses HTTP instead of HTTPS":
            "The connection does not use HTTPS encryption."
    }

    print("--- URL Awareness Checker ---")
    print("Type 'quit' to exit.")

    while True:
        url = input("\nEnter a URL to check: ").strip()

        if url.lower() == "quit":
            print("Thank you for using URL Awareness Checker!")
            break

        if not url:
            print("Please enter a URL.")
            continue

        warnings = check_url(url)

        if warnings:
            print("\nWarning signs found:")
            for warning in warnings:
                print(f"- {warning}")
                print(f"  Explanation: {explanations[warning]}")
        else:
            print("No warning signs detected by these checks.")

        print("\nNote: This tool cannot prove whether a URL is safe.")


if __name__ == "__main__":
    main()
