<p align="center">
  <img src="assets/logo.png" width="500" alt="The Intiface Game Haptics Controller (TIGHC)">
</p>

# TIGHC Profiles

> **18+ only.** These are game profiles for TIGHC, software that connects to
> and controls adult haptic/sex toy devices. Intended for use only by adults
> aged 18 or older.

**Version 1.3.8** — see [CHANGELOG.md](CHANGELOG.md) for release history.

Game profiles for [The Intiface Game Haptics Controller (TIGHC)](https://github.com/TIGHC/Engine).
On first launch, TIGHC downloads profiles from this repo automatically. Use
"Update profiles from GitHub" in the Profiles tab to pick up new additions,
or "Restore from GitHub..." to reset a profile to its original version.

Website: https://tighc.stuxie.dev  
Repository: https://github.com/TIGHC/Profiles

## Structure

Each top-level folder is one profile - one game - with a single file:

```
<profile-id>/
  profile.json    # everything: name, window titles, bindings, ranges, priority
```

`profile.json` contains:
- `name` — display name shown in the GUI
- `window_titles` — lowercase substrings matched against the focused window's
  title to auto-select this profile
- `priority` — binding ids in highest-to-lowest priority order; a
  higher-priority binding running on a channel blocks lower-priority ones
- `bindings` — list of `{id, keys, mode, enabled, devices, vibe}` objects.
  `mode` is `"continuous"` (sustained vibration while held) or `"pulse"`
  (one-shot buzz per press). `devices` is a list of channel nicknames from
  the main app's `devices.json`, or `["all"]`. `vibe` is a `[low, high]`
  0.0–1.0 intensity band rolled independently per channel on each activation.
- `background` — idle `vibe` band used when no binding is active

Full schema details and validation rules live in the main TIGHC repo's
README, since the engine (not this repo) is what parses and enforces them.

## Included profiles

- **`minecraft/`** - Minecraft's default keybinds (WASD movement, sprint,
  sneak, attack/use, jump, drop, offhand, inventory, hotbar).
- **`grounded/`** - built from Grounded's standard default keybinds
  (movement/sprint/crouch/attack/aim-block as continuous, jump/interact/
  inventory/hotbar as pulses). Not confirmed against Grounded specifically -
  adjust to match if it differs.
- **`grounded_2/`** - same base bindings as `grounded/`, for Grounded 2. Not
  confirmed against Grounded 2 specifically - adjust to match if it differs.
  Its `window_titles` is `"grounded 2"` (not just `"grounded"`) so it doesn't
  also match the original Grounded's window.
- **`waterpark_simulator/`** - built from typical first-person building/
  management sim controls (movement/sprint as continuous, jump/interact/
  place/rotate/build-menu/hotbar as pulses). Not confirmed against Waterpark
  Simulator specifically - adjust to match if it differs.
- **`cult_of_the_lamb/`** - confirmed default keybinds (movement, attack as
  continuous, dodge/curse/interact/inventory as pulses). No dedicated sprint
  - dodge (shift) is momentary, not sustained.
- **`stardew_valley/`** - confirmed default keybinds (movement/tool-use as
  continuous, secondary-action/menu/hotbar as pulses).
- **`powerwash_simulator/`** - confirmed default keybinds (movement/sprint/
  wash as continuous, jump/stance/interact/nozzle as pulses).
- **`powerwash_simulator_2/`** - confirmed default keybinds for the "Modern"
  control preset (wash is right-click here, vs. left-click in the first
  game); the game doesn't support rebinding, only preset switching. Its
  `window_titles` is `"powerwash simulator 2"` so it doesn't collide with
  `powerwash_simulator/`, though the reverse (the first game's profile
  matching this game's window) isn't ruled out - same caveat as
  grounded/grounded2.
- **`supermarket_simulator/`** - confirmed default keybinds (movement/sprint
  as continuous, jump/interact/open-box/rotate as pulses). Not rebindable.
- **`supermarket_together/`** - confirmed default keybinds, the co-op
  spinoff of Supermarket Simulator (movement/sprint as continuous,
  interact/place/open-box/deliveries as pulses). Not rebindable.
- **`megastore_simulator/`** - inferred from the Supermarket Simulator-style
  genre convention, not confirmed - no keybind documentation was found for
  this game specifically. Adjust to match if it differs.
- **`retro_rewind/`** - Retro Rewind: Video Store Simulator (a first-person
  video rental store sim - not the Mario Kart Wii mod of the same name).
  Inferred from the Supermarket Simulator-style genre convention, not
  confirmed - no keybind documentation was found for this game
  specifically. Adjust to match if it differs.
- **`spirit_valley/`** - inferred from its Stardew Valley-like genre, not
  confirmed - no keybind documentation was found for this game
  specifically. Adjust to match if it differs.
- **`tailbound/`** - confirmed via the official Steam manual (movement/run
  as continuous, action/cancel/map as pulses). No jump binding - the
  context-sensitive "action" key covers grapple/tail interactions.

## Adding a new profile

1. Copy an existing folder (`minecraft/` is the most complete example) and
   rename it to a short lowercase id for the new game.
2. Edit `profile.json`: set `name`, `window_titles` to match that game's
   window title, and adjust `bindings` and `vibe` ranges to that game's controls.
3. Validate it loads correctly by pointing a TIGHC checkout's `profiles/` at
   this repo (or copying the folder in) and running `python cli.py` or
   `python gui.py` - a structurally invalid profile fails fast with a clear
   error at startup rather than crashing mid-session.

This can also be done interactively from TIGHC's GUI (Profiles tab ->
"New profile...", which starts from a copy of `minecraft/`).

## Validation

Every `profile.json` in this repo is checked against
[`schema/profile.schema.json`](schema/profile.schema.json), a JSON Schema
derived from how TIGHC/Engine's `src/profiles.py` and `src/ranges.py`
actually parse and enforce a profile at load time. A pytest suite in
[`tests/`](tests/) validates all profiles against that schema, plus a few
semantic checks (unique binding ids, `vibe` low <= high, `priority` entries
referencing real binding ids) that plain JSON Schema can't express on its
own.

Run it locally:

```
pip install -r requirements-test.txt
pytest
```

This also runs automatically in CI (`.github/workflows/ci.yml`) on every
push and pull request.

## Versioning and contact

Follows [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`),
independently of the main TIGHC engine's own version - see
[CHANGELOG.md](CHANGELOG.md) for what changed in each release. Questions,
issues, or contributions: https://github.com/TIGHC/Profiles

## License

See [LICENSE.md](LICENSE.md).

---

*Built & Maintained by <img src="https://github.com/StuxieDev.png" height="14" alt="StuxieDev" valign="middle"> [StuxieDev](https://github.com/StuxieDev).*
