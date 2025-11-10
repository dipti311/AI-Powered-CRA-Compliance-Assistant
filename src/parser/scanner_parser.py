def parse_scanner_output(scanner_path):
    with open(scanner_path) as f:
        data = json.load(f)
    return [(vuln['cve'], vuln['severity']) for vuln in data.get('vulnerabilities', [])]