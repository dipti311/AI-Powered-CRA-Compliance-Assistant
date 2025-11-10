import json

def parse_sbom(sbom_path):
    with open(sbom_path) as f:
        sbom = json.load(f)
    return [(comp['name'], comp['version']) for comp in sbom.get('components', [])]

if __name__ == "__main__":
    sbom_path = "data/sample_sbom.json"  # ✅ Correct relative path
    components = parse_sbom(sbom_path)
    print("Parsed components:", components)