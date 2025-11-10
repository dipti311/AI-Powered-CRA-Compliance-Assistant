def test_parse_sbom():
    result = parse_sbom("data/sample_sbom.json")
    assert isinstance(result, list)