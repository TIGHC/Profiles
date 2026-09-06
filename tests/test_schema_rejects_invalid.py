"""Proves the schema isn't a no-op: takes a real, valid profile and breaks it
in ways that mirror actual failure modes TIGHC/Engine's src/profiles.py and
src/ranges.py raise on (see Engine's tests/test_profiles.py and
tests/test_ranges.py), then asserts schema validation correctly rejects each
mutation.
"""

import copy
import json

import pytest

from conftest import PROFILE_DIRS, load_profile

# minecraft/ is the most complete real profile in the repo (per README.md's
# "Adding a new profile" section), so it's used as the base for mutation.
_BASE_DIR = next(d for d in PROFILE_DIRS if d.name == "minecraft")


def _base():
    return copy.deepcopy(load_profile(_BASE_DIR))


def _is_valid(validator, data) -> bool:
    return validator.is_valid(data)


def test_base_profile_is_valid(validator):
    # Sanity check: if this fails, every "broken" case below is meaningless.
    assert _is_valid(validator, _base())


def test_rejects_missing_window_titles(validator):
    data = _base()
    del data["window_titles"]
    assert not _is_valid(validator, data)


def test_rejects_empty_window_titles(validator):
    data = _base()
    data["window_titles"] = []
    assert not _is_valid(validator, data)


def test_rejects_missing_bindings(validator):
    data = _base()
    del data["bindings"]
    assert not _is_valid(validator, data)


def test_rejects_empty_bindings(validator):
    data = _base()
    data["bindings"] = []
    assert not _is_valid(validator, data)


def test_rejects_binding_missing_id(validator):
    data = _base()
    del data["bindings"][0]["id"]
    assert not _is_valid(validator, data)


def test_rejects_binding_missing_vibe(validator):
    data = _base()
    del data["bindings"][0]["vibe"]
    assert not _is_valid(validator, data)


def test_rejects_binding_with_no_keys(validator):
    data = _base()
    data["bindings"][0]["keys"] = []
    assert not _is_valid(validator, data)


@pytest.mark.parametrize("vibe", [
    [-0.1, 0.5],   # low below 0.0
    [0.5, 1.1],    # high above 1.0
    [-0.1, 1.1],   # both out of bounds
])
def test_rejects_out_of_range_vibe(validator, vibe):
    data = _base()
    data["bindings"][0]["vibe"] = vibe
    assert not _is_valid(validator, data)


def test_rejects_vibe_with_wrong_arity(validator):
    data = _base()
    data["bindings"][0]["vibe"] = [0.5]
    assert not _is_valid(validator, data)


def test_rejects_devices_as_empty_list(validator):
    data = _base()
    data["bindings"][0]["devices"] = []
    assert not _is_valid(validator, data)


def test_rejects_wrong_type_for_window_title_exact(validator):
    data = _base()
    data["window_title_exact"] = "true"  # string, not boolean
    assert not _is_valid(validator, data)


def test_rejects_non_object_profile(validator):
    assert not _is_valid(validator, ["not", "an", "object"])


def test_error_message_names_the_offending_field(validator):
    data = _base()
    del data["bindings"][0]["vibe"]
    errors = list(validator.iter_errors(data))
    assert any("vibe" in e.message for e in errors)
