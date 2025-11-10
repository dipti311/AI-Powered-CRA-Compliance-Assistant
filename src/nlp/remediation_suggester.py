def suggest_remediation(vuln):
    if vuln['severity'] == 'high':
        return "Apply patch immediately and isolate component."
    return "Monitor and schedule patch."