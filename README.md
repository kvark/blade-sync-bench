# blade-sync-bench

One clone, one command, for the Blade / wgpu-core / Bevy barrier-host
protocol (JCGT companion to arXiv 2607.26506).

```sh
git clone --recursive https://github.com/kvark/blade-sync-bench
cd blade-sync-bench
python3 collect.py
```

That is `blade/paper/collect.py` with the three trees already in the
right sibling layout:

```text
blade-sync-bench/
  collect.py
  results/   # timing + validation land here, not in the Blade submodule
  blade/     # kvark/blade  @ jcgt-extension
  wgpu/      # kvark/wgpu   @ jcgt-extension
  bevy/      # kvark/bevy   @ jcgt-extension
```

The collector prints `Results: results/<timestamp>-<host>` at start. Pass
`--output /somewhere/else` to override.

Extra arguments pass through (clock pin first; see
`blade/paper/COLLECTING.md`):

```sh
python3 collect.py --skip-profile --skip-captures \
  --repetitions 1 --warmups 8 --samples 5 --passes 4
```

Do not pass `--allow-dirty` for numbers you will quote. The collector
refuses to reuse an output directory.

If you cloned without `--recursive`:

```sh
git submodule update --init --recursive
```
