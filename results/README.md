# Collection results

`python3 collect.py` writes each run here, next to the three source
submodules — not inside `blade/paper/data/raw/`.

```text
results/
  <timestamp>-<host>/              timing matrix (the study)
  <timestamp>-<host>-validation/   correctness + sync validation
  <timestamp>-<host>-profile/      optional perf profiles
  <timestamp>-<host>-captures/     optional RenderDoc captures
```

These directories are gitignored: they are machine-local and can be large.
Keep the folder you care about, or pass `--output /path/you/choose`.
