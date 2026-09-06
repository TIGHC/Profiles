"""Every real profile.json in this repo must validate against schema/profile.schema.json."""

import pytest

from conftest import PROFILE_DIRS, PROFILE_IDS, load_profile


def test_at_least_one_profile_discovered():
    # Guards against a glob typo silently turning this whole suite into a no-op.
    assert len(PROFILE_DIRS) >= 10


@pytest.mark.parametrize("profile_dir", PROFILE_DIRS, ids=PROFILE_IDS)
def test_profile_matches_schema(profile_dir, validator):
    data = load_profile(profile_dir)
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    assert not errors, "\n".join(
        f"{profile_dir.name}: {'/'.join(str(p) for p in e.path)}: {e.message}" for e in errors
    )


@pytest.mark.parametrize("profile_dir", PROFILE_DIRS, ids=PROFILE_IDS)
def test_profile_is_valid_json(profile_dir):
    # Belt-and-braces: load_profile() already does json.loads(), so this just
    # documents/asserts the intent - a parse failure here surfaces as this
    # test's own failure rather than an opaque conftest fixture error.
    data = load_profile(profile_dir)
    assert isinstance(data, dict)
