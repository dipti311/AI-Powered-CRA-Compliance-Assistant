import yaml

def parse_metadata(metadata_path):
    with open(metadata_path) as f:
        return yaml.safe_load(f)