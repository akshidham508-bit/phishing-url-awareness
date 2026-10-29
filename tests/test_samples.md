# Phishing URL Awareness Checker — Test Results

## Purpose
These tests check whether the program detects the six warning signs specified in the project workbook.

## Sample Test Results

| Test | Sample URL | Expected result | Status |
|---|---|---|---|
| 1 | `https://www.example.com/login` | No warning signs detected by these checks | Passed |
| 2 | `http://192.0.2.10/account` | IP address hostname and HTTP warnings | Passed |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol and HTTP warnings | Passed |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Too many hostname segments warning | Passed |
| 5 | `https://xn--example.invalid/` | Punycode marker warning | Passed |

## Limitations
- The checker identifies basic warning signs only.
- It does not open URLs or connect to the internet.
- It cannot prove whether a URL is safe or malicious.
- A URL with no detected warning signs may still be unsafe.

## Conclusion
The five sample tests were completed successfully based on the observed test results. The checker provides basic URL awareness and should not replace other security checks.
