# Open Source Tracking & Sync Guide

This guide explains how to keep synchronized with original awesome repositories while maintaining your customizations.

## Overview

This is a **curated fork** model that:
- Maintains attribution to original authors
- Enables live tracking of upstream changes
- Protects your custom additions during sync
- Provides transparent source information

## Quick Start

### 1. Check Current Status

See which collections have upstream updates available:

```bash
python sync_sources.py check
```

Output example:
```
↓ awesome-rust: 5 commits behind upstream
✓ awesome-python: In sync with upstream
⚠ awesome-nodejs: No upstream remote
```

### 2. Set Up Tracking

Configure upstream remotes for all collections:

```bash
python sync_sources.py setup
```

This adds the original repository as a remote named `upstream` in each collection folder.

### 3. Sync with Upstream

Merge the latest changes from original repositories:

```bash
# Sync all collections
python sync_sources.py sync

# Sync specific collection
python sync_sources.py sync awesome-rust
```

The sync uses a **"prefer ours" strategy** to protect your custom additions.

## How It Works

### Source Tracking

Each collection has metadata in `SOURCES.json`:
- Original author and repository URL
- Tracking status
- Last sync timestamp

### Merge Strategy

When syncing, the system uses the `-X ours` strategy:
- **Upstream changes are applied** unless they conflict
- **Your customizations are preserved** in case of conflicts
- **Manual review** recommended for important changes

### Custom Additions

You can add your own entries to any collection:
1. Edit the collection's README.md
2. Add your custom entries clearly marked or in a dedicated section
3. These will be preserved during sync operations

## File Structure

```
my-awesome-list/
├── README.md                 # Main index with source info
├── SOURCES.json             # Source tracking configuration
├── sync_sources.py          # Sync automation script
├── SYNC_GUIDE.md            # This file
└── awesome-{category}/
    ├── README.md            # Collection content + source footer
    └── [other files]
```

## Detailed Workflow

### For First-Time Setup

```bash
# 1. Clone the repository
git clone https://github.com/SerenaYuYu/my-awesome-list.git
cd my-awesome-list

# 2. Set up upstream tracking
python sync_sources.py setup

# 3. Check for updates
python sync_sources.py check
```

### For Regular Updates

```bash
# Check for new upstream changes weekly/monthly
python sync_sources.py check

# When updates are available, review then sync
python sync_sources.py sync

# Create a PR to track these changes
git add .
git commit -m "chore: sync upstream changes"
git push origin main
```

### For Custom Additions

1. **Mark clearly** that additions are custom:
   ```markdown
   ## Custom Additions (This Fork)
   
   - [Your Project](link) - Your description
   ```

2. **Keep them separate** from original content to avoid merge conflicts

3. **During sync**, these sections won't be affected

## SOURCES.json Schema

Each collection entry includes:

```json
{
  "id": "rust",
  "folder": "awesome-rust",
  "title": "Awesome Rust",
  "original_author": "rust-unofficial",
  "original_url": "https://github.com/rust-unofficial/awesome-rust",
  "description": "Rust crates and resources",
  "last_sync": "2026-07-18T10:30:00",
  "tracking_enabled": true
}
```

## Reporting

Generate a comprehensive source report:

```bash
python sync_sources.py report
```

This creates `SOURCES_REPORT.md` with:
- All upstream URLs
- Current sync status
- Last sync timestamps
- Tracking configuration

## Manual Sync (If Script Fails)

For any collection, you can manually sync:

```bash
cd awesome-{category}

# Add upstream if not present
git remote add upstream https://github.com/original-author/awesome-{category}

# Fetch latest
git fetch upstream

# Merge with "prefer ours" to protect customizations
git merge -X ours upstream/main

# Back in main directory
cd ..
git add awesome-{category}
git commit -m "chore: sync upstream"
```

## Troubleshooting

### No upstream remote found

```bash
python sync_sources.py setup
```

### Merge conflicts

The script uses "prefer ours" strategy to minimize conflicts. If conflicts occur:

```bash
# Resolve conflicts manually
cd awesome-{category}
git status  # See conflicted files
# Edit files to resolve
git add .
git commit -m "resolve merge conflicts"
cd ..
```

### Upstream URL changed

Update SOURCES.json with new URL:

```json
"original_url": "https://new-url/awesome-rust"
```

Then re-run setup:

```bash
python sync_sources.py setup
```

## Attribution

All content respects original authors:
- **Each collection links to original repository**
- **Footer credits are maintained**
- **License is inherited from originals**
- **Contributions go to both upstream and this fork**

## Contributing Back

### To Original Project

If you find issues or make improvements:
1. Fork and fix in the original repository
2. Submit PR to original awesome list
3. Updates will flow back through sync

### To This Fork

For customizations specific to this aggregation:
1. Create a PR with clear description
2. Maintain attribution to originals
3. Keep custom sections clearly marked

## Best Practices

1. **Review changes** before syncing
   ```bash
   python sync_sources.py check  # See what's coming
   ```

2. **Keep custom additions separate** from original content

3. **Commit sync updates** regularly
   ```bash
   python sync_sources.py sync
   git add .
   git commit -m "chore: sync upstream ($(date +%Y-%m-%d))"
   ```

4. **Document customizations** in collection README footer

5. **Link back to originals** always maintained

## Advanced Usage

### Sync Specific Commits

```bash
cd awesome-{category}
git log upstream/main --oneline -10  # See upstream commits
git cherry-pick <commit-hash>  # Apply specific commit
```

### Check Diff Before Merge

```bash
cd awesome-{category}
git diff HEAD..upstream/main | head -100
```

### Disable Tracking (If Needed)

In SOURCES.json:
```json
"tracking_enabled": false
```

Then skip in sync:
```bash
python sync_sources.py check  # Won't check this collection
```

## Questions?

- See SOURCES.json for complete source information
- Review each collection's README for license details
- Check original repositories for specific contribution guidelines

---

**Last Updated**: 2026-07-18  
**Sync Status**: Active tracking enabled
