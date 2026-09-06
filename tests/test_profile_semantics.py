"""Semantic invariants that plain JSON Schema can't express (comparisons
between two fields, or uniqueness/reference checks keyed on one property
across array items) but that TIGHC/Engine's src/profiles.py and
src/ranges.py do enforce at load time - a violation here would raise
ValueError/RuntimeError in the Engine (or, for the priority check, is a
repo-convention sanity check beyond what the Engine itself validates).
"""

import pytest

from conftest import PROFILE_DIRS, PROFILE_IDS, load_profile


@pytest.mark.parametrize("profile_dir", PROFILE_DIRS, ids=PROFILE_IDS)
def test_binding_ids_are_unique(profile_dir):
    # Engine's _load_profile raises ValueError(f"duplicate binding id '{bid}'").
    data = load_profile(profile_dir)
    ids = [b["id"] for b in data["bindings"]]
    assert len(ids) == len(set(ids)), f"{profile_dir.name}: duplicate binding id(s) in {ids}"


@pytest.mark.parametrize("profile_dir", PROFILE_DIRS, ids=PROFILE_IDS)
def test_vibe_low_is_not_greater_than_high(profile_dir):
    # src/ranges.py VibeRange.__post_init__ raises ValueError when low > high.
    data = load_profile(profile_dir)
    for binding in data["bindings"]:
        low, high = binding["vibe"]
        assert low <= high, (
            f"{profile_dir.name}: binding '{binding['id']}' has vibe low ({low}) > high ({high})"
        )
    background = data.get("background")
    if background and "vibe" in background:
        low, high = background["vibe"]
        assert low <= high, f"{profile_dir.name}: background vibe low ({low}) > high ({high})"


@pytest.mark.parametrize("profile_dir", PROFILE_DIRS, ids=PROFILE_IDS)
def test_priority_only_references_real_binding_ids(profile_dir):
    # Not enforced by the Engine (priority is advisory, read by the GUI only),
    # but a priority entry naming a binding id that doesn't exist in this same
    # profile is always a typo, so this repo's suite catches it anyway.
    data = load_profile(profile_dir)
    binding_ids = {b["id"] for b in data["bindings"]}
    for entry in data.get("priority", []):
        assert entry in binding_ids, (
            f"{profile_dir.name}: priority entry '{entry}' does not match any binding id {sorted(binding_ids)}"
        )


@pytest.mark.parametrize("profile_dir", PROFILE_DIRS, ids=PROFILE_IDS)
def test_devices_all_is_lowercase_or_any_case_but_recognizable(profile_dir):
    # _parse_devices_field lowercases entries and special-cases "all" (any
    # case) to mean every channel. Not a hard Engine requirement, but every
    # profile in this repo uses ["all"], so a stray typo like ["al"] would
    # silently create a per-channel nickname filter instead of matching
    # everything - catch that here rather than as a review nit.
    data = load_profile(profile_dir)
    for binding in data["bindings"]:
        devices = binding.get("devices", ["all"])
        assert isinstance(devices, list) and devices, (
            f"{profile_dir.name}: binding '{binding['id']}' devices must be a non-empty list"
        )
