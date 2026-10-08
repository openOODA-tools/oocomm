# oocomm: Sovereign LINE COMPARATOR

<div align="center">

```
================================================================================
                                oocomm
               Sovereign openOODA LINE COMPARATOR
================================================================================
```

**Sovereign LINE COMPARATOR**  
*Compares two sorted files line by line to produce unique and common lines.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oocomm/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oocomm-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oocomm/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oocomm/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oocomm-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oocomm/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oocomm [options] FILE1 FILE2

Compare sorted files FILE1 and FILE2 line by line.

With no options, produce three-column output. Column one contains
lines unique to FILE1, column two contains lines unique to FILE2,
and column three contains lines common to both files.

Options:
  -1                     suppress column 1 (lines unique to FILE1)
  -2                     suppress column 2 (lines unique to FILE2)
  -3                     suppress column 3 (lines that appear in both files)
  --check-order          check that the input is correctly sorted [default]
  --nocheck-order        do not check that the input is correctly sorted
  --output-delimiter=STR separate columns with STR [default: TAB]
  --total                output a summary at the end
  -z, --zero-terminated  line delimiter is NUL, not newline
      --inspect          display comparison summary breakdown
      --demo             run demonstration with synthetic sorted fruit datasets
      --json             output formatted as JSON telemetry
  -h, --help             display this help and exit
  -V, --version          output version information and exit
      --mcp              run as Model Context Protocol stdio server
```

### Examples

```bash
# Compare two sorted files producing standard 3-column output
oocomm file1.txt file2.txt

# Extract lines common to both files (suppress columns 1 and 2)
oocomm -12 file1.txt file2.txt

# Extract lines unique to file1 (suppress columns 2 and 3)
oocomm -23 file1.txt file2.txt

# Display symmetric differences only (suppress common column 3)
oocomm -3 file1.txt file2.txt

# Compare with comma delimiter and summary totals
oocomm --output-delimiter="," --total file1.txt file2.txt

# Run demonstration with telemetry
oocomm --demo --json
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oocomm` operates as a JSON-RPC 2.0 stdio server providing sovereign line comparison tools for AI agents without network authority:

```bash
oocomm --mcp
```

### Exposed MCP Tools

1. **`comm_compare`**: Compare two sorted multiline text streams producing 3-column diff output.
2. **`comm_unique_file1`**: Extract lines unique to the first stream.
3. **`comm_unique_file2`**: Extract lines unique to the second stream.
4. **`comm_intersection`**: Extract common lines present in both streams.
5. **`comm_check_sort`**: Verify if a multiline text stream is in lexicographical sorted order.
6. **`comm_stats`**: Compute comparison metrics and unique line statistics in structured JSON.

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Zero ambient authority or network egress.
* **Negative-Trust Architecture:** Strict boundary validation on file descriptors, sort orders, and column delimiters.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
