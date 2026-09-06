"""Shared fixtures for validating profile.json against schema/profile.schema.json.

The schema captures what TIGHC/Engine's src/profiles.py and src/ranges.py
actually parse and enforce at load time (see that repo's tests/test_profiles.py
and tests/test_ranges.py) - a profile that fails this schema would either
raise ValueError/RuntimeError in the Engine, or violate a repo-convention
rule this suite checks separately (see test_profile_semantics.py).
"""

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schema" / "profile.schema.json"

# Every top-level folder that contains a profile.json is a profile - "assets"
# and dotfiles/dirs (.git, schema/, tests/, etc.) are not.
PROFILE_DIRS = sorted(
    p.parent for p in REPO_ROOT.glob("*/profile.json")
)
PROFILE_IDS = [p.name for p in PROFILE_DIRS]


@pytest.fixture(scope="session")
def schema():
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def validator(schema):
    from jsonschema import Draft202012Validator

    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def load_profile(profile_dir: Path) -> dict:
    return json.loads((profile_dir / "profile.json").read_text(encoding="utf-8"))
