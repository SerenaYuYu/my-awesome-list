# Customization Guide

Learn how to add custom content to your awesome collections while maintaining sync capability.

## Table of Contents

1. [Adding Custom Entries](#adding-custom-entries)
2. [Creating Custom Sections](#creating-custom-sections)
3. [Merge Conflict Prevention](#merge-conflict-prevention)
4. [Handling Upstream Changes](#handling-upstream-changes)

## Adding Custom Entries

### Method 1: Custom Section (Recommended)

Add a clearly marked section at the end of the README:

```markdown
← [Back to My Awesome List](https://github.com/SerenaYuYu/my-awesome-list)

# Original Content
[... original awesome list content ...]

## 🎯 Custom Additions (SerenaYuYu Fork)

Projects and resources added in this curated fork:

- [Custom Project A](https://github.com/...) - Description of why added
- [Custom Project B](https://github.com/...) - Additional value provided

**Note**: Custom additions are preserved during upstream sync operations.

---

## 📚 Source Information
[... source footer ...]
```

### Method 2: Tagged Entries

Add a tag to entries you've added:

```markdown
- [Original Project](url) - Original description
- [Your Custom Pick](url) - Your description ⭐ *[custom]*
- [Another Your Pick](url) - Your description ⭐ *[custom]*
```

### Method 3: Inline Comments

Use HTML comments for your additions:

```markdown
<!-- Custom Addition: Reason for including -->
- [Your Project](url) - Your description

<!-- End Custom Addition -->
```

## Creating Custom Sections

### Example: Adding a "Trending Now" Section

```markdown
## 🚀 Trending Now (This Fork)

Hot projects gaining popularity:
- [Project A](url) - Why it matters
- [Project B](url) - Current momentum

*Last updated: 2026-07-18*
```

### Example: Adding "Community Favorites" Section

```markdown
## ⭐ Community Favorites (User Submissions)

Highly recommended by community members:
- [Project](url) - Recommendation by [username](link)
- [Project](url) - Recommendation by [username](link)
```

## Merge Conflict Prevention

### Best Practices

1. **Keep custom content at the end**
   - Original content stays at top
   - Custom sections after original footer
   - No modifications to original entries

2. **Use clear markers**
   ```markdown
   ## [FORK] Custom Additions
   
   Content here won't conflict with upstream
   ```

3. **Maintain consistent formatting**
   - Use same markdown style as original
   - Consistent indentation and spacing
   - Same link format

### Example Structure

```
README.md
├── Backlink (← [Back to My Awesome List])
├── ORIGINAL CONTENT (unchanged from upstream)
│   ├── Introduction
│   ├── Categories
│   ├── All original entries
│   └── Original footer
├── [SEPARATOR: ✏️ CUSTOMIZATIONS]
├── CUSTOM SECTIONS
│   ├── Custom Additions
│   ├── Community Picks
│   ├── Fork-specific Resources
│   └── Your custom content
└── Source Information Footer
```

## Handling Upstream Changes

### Scenario 1: Upstream Adds Similar Content

If original project adds something similar to your custom addition:

**Option A: Keep Both**
```markdown
## Original Content Addition
- [Original Project](url) - Original description

## Custom Additions
- [Your Similar Pick](url) - Why you chose this one differently
```

**Option B: Merge**
Replace custom version with upstream, or enhance upstream version:
```markdown
- [Project](url) - Original description + your additional context ⭐
```

### Scenario 2: Upstream Changes Entry Location

If original moves categories around:

1. Let sync operation handle it (merge will work)
2. Re-verify your custom entries still make sense in new structure
3. Update custom section references if needed

### Scenario 3: Conflict Resolution

If a real merge conflict occurs:

```bash
cd awesome-{category}

# See what's conflicted
git status

# Examine conflict
git diff

# Resolve: keep both versions
# Edit file to include both upstream and your content

# Complete merge
git add .
git commit -m "resolve merge: keep upstream + custom"
```

## Workflow Examples

### Example 1: Adding Curated Filter

**Goal**: Add a "Top 100" curated selection to Python collection

```markdown
## 🏆 Top 100 Curated Picks (This Fork)

The most essential Python libraries, hand-picked from the full list:

### Web Frameworks
- [Django](link) - Full-featured, batteries-included
- [FastAPI](link) - Modern, fast, with auto docs
- [Flask](link) - Minimal, flexible

[Complete list of 100 items...]

---

## Original Awesome Python Content
[... full original content follows ...]
```

### Example 2: Adding Category Overlays

**Goal**: Add project maturity ratings to Rust collection

```markdown
## 🎯 Maturity Ratings (This Fork)

Stability assessment of key projects:

### Production Ready ✅
- [Tokio](link) - Production runtime (Original: Asynchronous runtime)
- [Serde](link) - Production serialization

### Experimental 🧪  
- [Emerging Project](link) - Early stage innovation

---

## Original Content
[... original awesome-rust content ...]
```

### Example 3: Adding Learning Path

**Goal**: Create learning progression in Courses collection

```markdown
## 📚 Learning Paths (This Fork)

Suggested sequence for getting started:

### Beginner Path
1. [Intro Course](link) - Foundation
2. [Practice Course](link) - Hands-on
3. [Project Course](link) - Building

### Advanced Path
1. [Theory Course](link)
2. [Optimization Course](link)

---

## Original Awesome Courses
[... original content ...]
```

## Sync Operations with Customizations

### Automatic Protection

The sync script uses "prefer ours" merge strategy:
- Upstream changes to original content → Applied
- Conflicts with custom sections → Your version kept
- New upstream entries → Automatically added

### Manual Review Recommended

```bash
# Before syncing, check what changed
cd awesome-{category}
git fetch upstream
git diff HEAD..upstream/main | less

# Then sync
cd ..
python sync_sources.py sync awesome-{category}

# Review merged result
cd awesome-{category}
git log --oneline -5
```

### Confirming Customizations Preserved

After sync:

```bash
# Verify custom section is intact
grep "Custom Additions" README.md

# Verify custom entries unchanged
grep "your-custom-project" README.md
```

## Organizing Multiple Customizations

### For Large Custom Sections

Create separate file references:

```markdown
## 🎯 Customizations (This Fork)

- See [CUSTOM_PYTHON.md](./CUSTOM_PYTHON.md) for curated Python picks
- See [LEARNING_PATHS.md](./LEARNING_PATHS.md) for suggested study paths
- See [RATINGS.md](./RATINGS.md) for project maturity ratings
```

### Using Separate Branches

For experimental customizations:

```bash
git checkout -b experiment/new-categorization

# Make your customizations
# Test and validate

# When ready to merge
git checkout main
git merge experiment/new-categorization
```

## Documenting Your Customizations

Always document **why** you added something:

```markdown
## 🎯 Custom Additions

### Why These Additions?

This fork adds selections based on:
- **Practical utility**: Tools used in real projects
- **Learning value**: Great for understanding concepts
- **Community feedback**: Popular requests from users
- **Quality**: Well-maintained, good documentation

### Added Items:

**Practical Tools**
- [Tool](link) - Solves specific problem not in original

**Learning Resources**  
- [Resource](link) - Great for understanding [concept]

**Community Favorites**
- [Project](link) - Requested by 5+ community members
```

## Version Management

Track your customization versions:

```markdown
## Customization Changelog

### v2.0 (2026-07-20)
- Added Learning Paths section
- Reorganized by maturity level
- Added 15 new community favorites

### v1.0 (2026-07-18)
- Initial custom additions
```

## Best Practices Summary

✅ **DO:**
- Keep custom sections clearly marked
- Document why you added things
- Test sync operations regularly
- Version your customizations
- Link to originals prominently
- Preserve all attribution

❌ **DON'T:**
- Edit original entries (mark as modified instead)
- Hide customizations
- Break upstream license
- Remove author attribution
- Conflict with original content
- Assume custom sections survive all syncs (they will, but verify)

## Getting Help

- See [SYNC_GUIDE.md](./SYNC_GUIDE.md) for sync-related questions
- Review each collection's README footer for original source info
- Check SOURCES.json for upstream repository details
- Create an issue on this repository for fork-specific questions

---

**Happy Customizing!** 🎉
