# Getting Started with My Awesome List

Welcome! This guide walks you through using this consolidated awesome list collection.

## What is This?

This is a **curated fork** of 14 different awesome lists, consolidated into one place with:
- **Live sync** capability to track original repositories
- **Custom additions** that won't be lost during updates
- **Full attribution** to original authors
- **Transparent sourcing** for all content

## For Users

### 1. Browse Collections

All 14 collections are listed in the main [README.md](./README.md):
- Click any collection to explore its content
- Each has full attribution to the original author
- Collections are regularly synced with upstream

### 2. Find What You Need

```
Technology → C++ / Rust / Python / JavaScript
Learning → Courses / Interview Questions / For Beginners
Tools → Design Tools / Docker Compose
Soft Skills → Scalability / System Design
Cutting Edge → Bots / Flutter
```

### 3. Understand Customizations

Some collections may have custom additions:

Look for sections marked:
- 🎯 **Custom Additions (This Fork)**
- ⭐ **Community Favorites**
- 📚 **Learning Paths**

These are maintained separately and won't conflict with original content.

### 4. Stay Updated

Original repositories are tracked and can be automatically synced:

```bash
# Check if any upstream changes are available
python sync_sources.py check

# See which collections have new commits
# Output example:
# ↓ awesome-rust: 5 commits behind upstream
# ✓ awesome-python: In sync with upstream
```

## For Repository Maintainers

### 1. Initial Setup

```bash
# Clone the repository
git clone https://github.com/SerenaYuYu/my-awesome-list.git
cd my-awesome-list

# Set up upstream tracking for all collections
python sync_sources.py setup

# Check current status
python sync_sources.py check
```

### 2. Regular Maintenance

**Weekly/Monthly:**

```bash
# Check for upstream updates
python sync_sources.py check

# Review what changed
# If updates available:
python sync_sources.py sync

# Verify your customizations are intact
git status

# Commit and push
git add .
git commit -m "chore: sync upstream changes (YYYY-MM-DD)"
git push
```

### 3. Adding Custom Content

Follow the [CUSTOMIZATION.md](./CUSTOMIZATION.md) guide for best practices:

```markdown
## 🎯 Custom Additions (This Fork)

Your custom entries here...

*Note: These are preserved during sync operations.*
```

### 4. Monitoring Sync Health

Generate a complete report:

```bash
python sync_sources.py report

# Creates SOURCES_REPORT.md with:
# - All upstream URLs
# - Sync status for each collection
# - Last sync timestamps
```

## File Structure

```
my-awesome-list/
├── README.md                    # Main index with collection list
├── GETTING_STARTED.md           # This file
├── SYNC_GUIDE.md                # Detailed sync instructions
├── CUSTOMIZATION.md             # Custom content best practices
├── SOURCES.json                 # Source tracking metadata
├── sync_sources.py              # Sync automation script
│
├── awesome-bots/
│   └── README.md                # Awesome Bots collection
├── awesome-compose/
│   └── README.md                # Awesome Compose collection
├── awesome-courses/
│   └── README.md                # Awesome Courses collection
├── [11 more awesome-* folders]
│
└── .git/                        # Git repository
```

## Key Commands

### For Regular Users

```bash
# Browse collections (just open README.md)
cat README.md

# Verify you're up to date
python sync_sources.py check
```

### For Maintainers

```bash
# Complete setup
python sync_sources.py setup

# Check sync status
python sync_sources.py check

# Sync with all upstream repos
python sync_sources.py sync

# Sync specific collection
python sync_sources.py sync awesome-rust

# Generate report
python sync_sources.py report
```

### For Developers

```bash
# Add custom section to collection
cd awesome-python
# Edit README.md, add custom section

# Back up to main directory
cd ..

# Test sync won't break your changes
python sync_sources.py sync awesome-python

# Commit
git add awesome-python/
git commit -m "Add custom Python selections"
git push
```

## Understanding Sources

### SOURCES.json

Centralized metadata for all collections:

```json
{
  "id": "python",
  "folder": "awesome-python",
  "title": "Awesome Python",
  "original_author": "vinta",
  "original_url": "https://github.com/vinta/awesome-python",
  "tracking_enabled": true,
  "last_sync": "2026-07-18"
}
```

This ensures:
- ✓ Attribution is maintained
- ✓ Original URLs are discoverable
- ✓ Sync status is tracked
- ✓ You can disable tracking if needed

### Source Footers

Each collection README has a footer with:
- Original Author link
- Original Repository URL
- Sync capability explanation
- Contribution guidelines

Example:
```markdown
## 📚 Source Information

**Original Author(s)**: @vinta  
**Original Repository**: https://github.com/vinta/awesome-python  
**Fork Type**: Curated (part of My Awesome List)

### How to Keep in Sync

git remote add upstream https://github.com/vinta/awesome-python
git fetch upstream
git merge upstream/main
```

## Sync Workflow

### Automatic Merge Strategy

The `sync_sources.py` script uses a "prefer ours" merge strategy:

1. **Upstream changes** are fetched
2. **Conflicts** favor your local version
3. **New upstream content** is added automatically
4. **Your customizations** are always protected

This means:
- ✅ Original content updates flow in
- ✅ Your custom sections survive
- ✅ Fewer merge conflicts
- ✅ Safe, predictable syncs

### Example Sync Scenario

```bash
# Before sync
awesome-python/
├── [Original content]
├── [New upstream entries: 5 commits behind]
└── [Your custom section]

# After: python sync_sources.py sync awesome-python
awesome-python/
├── [Original content + upstream updates]
├── [New entries merged in]
└── [Your custom section - PRESERVED]
```

## Common Tasks

### Add a Custom Entry

1. Edit the collection README.md
2. Add to custom section at the end:
   ```markdown
   ## 🎯 Custom Additions
   - [Your Project](url) - Your description
   ```
3. Commit: `git commit -m "Add custom entry: [project]"`
4. Don't worry: this section is protected during sync

### Update from Upstream

1. Check: `python sync_sources.py check`
2. Sync: `python sync_sources.py sync`
3. Review: `git diff HEAD~1`
4. Commit: `git commit -m "chore: sync upstream"`

### Contribute Back to Original

If you make improvements that benefit the original:

1. Create PR in original repository (link in SOURCES.json)
2. Original maintainers review and merge
3. Your changes flow back via next sync

### Disable Tracking for Collection

If a collection is abandoned or outdated:

1. Edit SOURCES.json
2. Set `"tracking_enabled": false`
3. Sync operations will skip it
4. Content remains for reference

## Troubleshooting

### "ModuleNotFoundError: No module named 'json'"

Python json module is built-in. Try:
```bash
python3 sync_sources.py check
```

### Merge Conflicts During Sync

```bash
cd awesome-{category}

# See conflicts
git status

# Edit conflicted files
# Then complete merge
git add .
git commit -m "resolve merge conflicts"

cd ..
```

### Upstream Remote Not Found

```bash
# Re-run setup
python sync_sources.py setup

# Or manual add
cd awesome-{category}
git remote add upstream [original-url]
cd ..
```

### Want to See Original Repository

Each collection footer has the original URL:

```bash
# Example: view Awesome Python original
# See: SOURCES.json - "original_url": "https://github.com/vinta/awesome-python"
```

## Tips & Tricks

### Create Aliases

```bash
# In your shell config (~/.bashrc or ~/.zshrc)
alias awesome-check='python sync_sources.py check'
alias awesome-sync='python sync_sources.py sync'
alias awesome-report='python sync_sources.py report'
```

### Monitor Sync Status

```bash
# Check weekly
0 9 * * 1 cd ~/my-awesome-list && python sync_sources.py check

# Auto-sync monthly  
0 9 1 * * cd ~/my-awesome-list && python sync_sources.py sync
```

### Export for Other Tools

```bash
# Convert to JSON for your app
python sync_sources.py report

# Parse SOURCES.json programmatically
python3 -c "import json; print(json.load(open('SOURCES.json'))['collections'])"
```

### Contribute Upstream Improvements

Found a great resource? Add it to original awesome list:
1. Fork original repository
2. Add entry
3. Submit PR to original
4. It flows into this fork via next sync

## Support & Contributing

### Using This Repository

- Issues: Open GitHub issues for problems
- Discussions: Use discussions for questions
- PRs: Submit PRs for improvements

### Contributing to Originals

Original repositories are listed in SOURCES.json:
- Find what you want to improve
- Go to original repository
- Submit PR there
- Changes will flow back via sync

## Next Steps

1. **Explore**: Browse the [collections](./README.md)
2. **Understand**: Read [SYNC_GUIDE.md](./SYNC_GUIDE.md)
3. **Customize**: See [CUSTOMIZATION.md](./CUSTOMIZATION.md)
4. **Contribute**: Submit to originals or this fork

## FAQ

**Q: Will my changes be lost during sync?**
A: No! Custom sections in your local fork are protected by the "prefer ours" merge strategy.

**Q: Can I edit original content?**
A: You can, but it's recommended to use a Custom section instead so it persists through syncs.

**Q: How often should I sync?**
A: Weekly or monthly is typical. Use `python sync_sources.py check` to see if updates are available.

**Q: What if I want to stop tracking an upstream?**
A: Edit SOURCES.json and set `"tracking_enabled": false`.

**Q: Can I use this for a private fork?**
A: Yes! Just update SOURCES.json to point to your private repositories.

**Q: How do I contribute improvements?**
A: Submit PRs to original repositories (they're tracked), or to this fork for fork-specific improvements.

---

**Happy exploring! 🚀**

Need help? See [SYNC_GUIDE.md](./SYNC_GUIDE.md) or [CUSTOMIZATION.md](./CUSTOMIZATION.md).
