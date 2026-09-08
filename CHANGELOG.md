# Changelog

All notable changes to this project are documented here. Versioning follows
[Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`), independent
of the main [TIGHC](https://github.com/TIGHC/Engine) engine's own version.

## [1.3.7] - 2026-09-08

### Changed
- `CHANGELOG.md` entries now carry a date next to each version (`## [x.y.z] - YYYY-MM-DD`), backfilled from each release's git tag (and one `git blame` lookup for the one untagged early release), matching the Automater project's changelog format
- `README.md` gained a `## License` section and a "Built & Maintained by StuxieDev" footer line at the bottom, matching Automater's layout

## [1.3.6] - 2026-09-01

### Fixed
- **Mojibake in `commit.sh`/`commit.bat` console output** — an em dash in
  the log/echo messages rendered as garbled bytes (e.g. `ÔÇö`) on the
  default Windows console codepage. Replaced with plain ASCII dashes.

## [1.3.5] - 2026-09-01

### Fixed
- **`commit.sh`/`commit.bat` staleness** — they hardcoded the version and
  commit message per release, so a forgotten update would tag the wrong
  version or skip tagging entirely. Both now read the version from
  `VERSION.md` dynamically, skip committing if nothing's staged, and skip
  tagging if the tag already exists.

## [1.3.4] - 2026-08-30

### Added
- **`commit.bat`/`commit.sh`** — pre-written commit+tag scripts, rewritten
  with each commit's exact message/tag before being run.

## [1.3.3] - 2026-08-30

### Added
- **`CONTRIBUTING.md`** — how to add/edit a profile, validate it, and the
  versioning convention for PRs.

## [1.3.2] - 2026-08-30

### Changed
- **`version.txt` renamed to `VERSION.md`** — same single source of truth,
  only the filename changed.

## [1.3.1] - 2026-08-30

### Fixed
- **Grounded 2 window title** — updated `window_titles` from `"Grounded"` to
  `"Grounded 2"` so it no longer matches the original Grounded's window.

### Changed
- **Repo moved to TIGHC org** — all URLs updated from `StuxieDev/TIGHC-Profiles`
  to `TIGHC/Profiles`.

## [1.3.0] - 2026-08-30

### Changed
- **`background_vibe` removed** from all 14 `profile.json` files. The engine
  no longer uses this field (removed in TIGHC v3.8.0); channels idle at 0
  between activations. Requires TIGHC engine v3.8.0 or later.

## [1.2.0] - 2026-08-30

### Changed
- **All profiles migrated to single `profile.json`** — each profile folder
  previously held two files (`keybinds.json` + `ranges.json`). These have been
  merged into one `profile.json` per game, with the `vibe` range inline on each
  binding and `background_vibe` at the top level. Requires TIGHC engine v3.7.0
  or later.

## [1.1.2] - 2026-08-30

### Fixed
- `assets/icon.png`, `icon.ico`, and `logo.png` had an opaque dark
  (`#1E1E1E`) rounded-rect fill baked in instead of a transparent
  background. Replaced with transparent versions (copied from the main
  TIGHC repo after fixing them there via a color-to-alpha un-blend).

## [1.1.1] - 2026-08-30

### Added
- Logo banner and an `assets/` folder (`icon.png`/`icon.ico`/`logo.png`,
  copied from the main TIGHC repo) at the top of README.md, for visual
  consistency with the main repo and the website.
- Author credit section in README.md (StuxieDev, with a GitHub avatar at
  `assets/author.png`), matching the same addition in the main TIGHC repo
  and TIGHC-Website.

## [1.1.0] - 2026-08-30

### Added
- `cult_of_the_lamb/`, `stardew_valley/`, `powerwash_simulator/`,
  `powerwash_simulator_2/`, `supermarket_simulator/`,
  `supermarket_together/`, `megastore_simulator/`, `retro_rewind/`,
  `spirit_valley/`, and `tailbound/` profiles, covering the gameplay-driven
  titles in the local Steam library that weren't already covered.
  Confidence varies by title - see README.md's "Included profiles" section
  for which are confirmed vs. inferred/community-sourced. (`retro_rewind/`
  is Retro Rewind: Video Store Simulator, not the Mario Kart Wii mod
  initially assumed.)

## [1.0.2] - 2026-08-30

### Added
- `grounded/` profile - built from Grounded's standard default keybinds
  (movement, sprint, crouch, attack, aim/block, jump, interact, inventory,
  hotbar switching). Not confirmed against Grounded specifically.

### Changed
- `grounded2/` profile's `window_titles` narrowed to `"grounded 2"` (was
  `"grounded"`) so it no longer also matches the original Grounded's window
  now that both profiles exist.

## [1.0.1] - 2026-08-23

### Added
- `waterpark_simulator/` profile - built from typical first-person
  building/management sim controls (movement, sprint, jump, interact,
  place, rotate, build menu, hotbar switching). Not confirmed against
  Waterpark Simulator specifically.

## [1.0.0] - 2026-08-30

Initial release, split out from the main TIGHC repo into its own submodule.

### Added
- `minecraft/` profile - Minecraft's default keybinds (WASD movement,
  sprint, sneak, attack/use, jump, pick block, drop, offhand, inventory,
  hotbar switching).
- `grounded2/` profile - built from Grounded's standard default keybinds
  (movement, sprint, crouch, attack, aim/block, jump, interact, inventory,
  hotbar switching).
