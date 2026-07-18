# My Awesome List

🌟 A consolidated collection of awesome lists covering various topics in technology and development.

**What makes this special:**
- ✓ **Live tracking** of original repositories  
- ✓ **Curated selections** with custom additions  
- ✓ **Full attribution** to original authors  
- ✓ **Automated sync** to keep current with originals  
- ✓ **Transparent sources** visible in metadata  

📖 **Quick Links**: [Using & Syncing](./SYNC_GUIDE.md) • [Adding Custom Content](./CUSTOMIZATION.md) • [All Sources](./SOURCES.json)

## 🚀 Quick Start

### View Collections

Browse any of the 14 topic collections in the table below. Each contains curated resources with attribution to the original awesome list.

### Keep in Sync

```bash
# Check for upstream updates
python sync_sources.py check

# Sync all collections with originals
python sync_sources.py sync

# Get detailed report
python sync_sources.py report
```

See [SYNC_GUIDE.md](./SYNC_GUIDE.md) for detailed instructions.

### Add Custom Content

Mark your additions clearly to protect them during sync operations:

```markdown
## 🎯 Custom Additions (This Fork)

- [Your Project](url) - Your description

[See CUSTOMIZATION.md for detailed guide]
```

See [CUSTOMIZATION.md](./CUSTOMIZATION.md) for best practices.

## 📚 Collections

| Collection | Original Author | Status |
|---|---|---|
| [Bots](./awesome-bots/) | [@itsthekids](https://github.com/itsthekids) | ✓ Tracking |
| [Compose](./awesome-compose/) | [@docker](https://github.com/docker) | ✓ Tracking |
| [Courses](./awesome-courses/) | [@prakhar1989](https://github.com/prakhar1989) | ✓ Tracking |
| [C++](./awesome-cpp/) | [@fffaraz](https://github.com/fffaraz) | ✓ Tracking |
| [Design Tools](./awesome-design-tools/) | [@goabstract](https://github.com/goabstract) | ✓ Tracking |
| [Flutter](./awesome-flutter/) | [@Solido](https://github.com/Solido) | ✓ Tracking |
| [For Beginners](./awesome-for-beginners/) | [@MunGell](https://github.com/MunGell) | ✓ Tracking |
| [Interview Questions](./awesome-interview-questions/) | [@DopplerHQ](https://github.com/DopplerHQ) | ✓ Tracking |
| [Node.js](./awesome-nodejs/) | [@sindresorhus](https://github.com/sindresorhus) | ✓ Tracking |
| [Python](./awesome-python/) | [@vinta](https://github.com/vinta) | ✓ Tracking |
| [React](./awesome-react/) | [@enaqx](https://github.com/enaqx) | ✓ Tracking |
| [React Components](./awesome-react-components/) | [@brillout](https://github.com/brillout) | ✓ Tracking |
| [Rust](./awesome-rust/) | [@rust-unofficial](https://github.com/rust-unofficial) | ✓ Tracking |
| [Scalability](./awesome-scalability/) | [@binhnguyennus](https://github.com/binhnguyennus) | ✓ Tracking |

## 🎯 Quick Links

- Browse individual collections using the table above
- Each collection contains a comprehensive list of resources in its category
- Original repositories maintain their own content and contribute guidelines

## 🔄 Open Source Tracking

This project maintains live links to all original awesome repositories. Each collection:
- **Preserves attribution** to original authors
- **Tracks upstream changes** via SOURCES.json
- **Supports customization** while maintaining sync capability

### Original Sources

See [SOURCES.json](./SOURCES.json) for complete source tracking information including:
- Original author and repository URLs
- Last sync timestamp
- Tracking status for each collection

## 🎯 Customization Guide

This is a curated fork model. You can:

1. **Keep synchronized**: Pull updates from original repositories
2. **Add custom entries**: Extend collections with your own picks
3. **Maintain attribution**: Always link back to original sources
4. **Sync workflow**: Use the sync script to update from upstream

### How to Sync with Originals

```bash
# View all configured sources
cat SOURCES.json

# Manual sync (fetch from original source)
git remote add upstream [original-url]
git fetch upstream
git merge upstream/main  # or appropriate branch
```

## 📝 Contributing

Each sub-collection follows its own contribution guidelines. Refer to the individual README files for specific submission requirements.

For this consolidated project:
- **Original content changes**: Submit to original repositories
- **Customizations**: Make pull requests to this repository
- **New entries**: Follow guidelines in individual collection READMEs

---

**Project Type**: Curated Fork (Open Source Aggregation)  
**Last Updated**: 2026-07-18  
**Sync Status**: ✓ Active tracking enabled
