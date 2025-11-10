def validate_compliance(parsed_sbom, parsed_vulns):
    for _, severity in parsed_vulns:
        if severity == 'critical':
            return False
    return True