def generate_justification(component, vuln, metadata):
    return f"{component} is affected by {vuln}. Architecture uses {metadata.get('auth_method')} which mitigates risk."