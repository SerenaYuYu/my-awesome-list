#!/usr/bin/env python3
"""
Sync awesome repository sources with upstream repositories.
Maintains attribution while allowing custom additions.
"""

import json
import subprocess
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

class AwesomeSourceSync:
    def __init__(self, config_file: str = "SOURCES.json"):
        self.config_file = config_file
        self.config = self._load_config()
        self.repo_root = Path(__file__).parent

    def _load_config(self) -> Dict:
        """Load source configuration from SOURCES.json"""
        with open(self.config_file, 'r') as f:
            return json.load(f)

    def _save_config(self):
        """Save updated configuration back to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def _run_git(self, args: List[str], cwd: Optional[Path] = None) -> str:
        """Run git command and return output"""
        cmd = ['git'] + args
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"Error running {' '.join(cmd)}: {result.stderr}")
        return result.stdout.strip()

    def add_upstream_remote(self, collection: Dict) -> bool:
        """Add upstream remote to collection folder"""
        folder_path = self.repo_root / collection['folder']
        remote_name = 'upstream'
        original_url = collection['original_url']

        # Check if remote already exists
        existing_remotes = self._run_git(['remote'], cwd=folder_path)

        if remote_name not in existing_remotes.split('\n'):
            try:
                self._run_git(['remote', 'add', remote_name, original_url], cwd=folder_path)
                print(f"✓ Added upstream remote to {collection['folder']}")
                return True
            except Exception as e:
                print(f"✗ Failed to add upstream to {collection['folder']}: {e}")
                return False
        else:
            print(f"⚠ Upstream remote already exists for {collection['folder']}")
            return True

    def fetch_upstream(self, collection: Dict) -> bool:
        """Fetch from upstream repository"""
        folder_path = self.repo_root / collection['folder']

        try:
            print(f"Fetching from {collection['original_url']}...")
            self._run_git(['fetch', 'upstream'], cwd=folder_path)
            print(f"✓ Fetched upstream for {collection['folder']}")
            return True
        except Exception as e:
            print(f"✗ Failed to fetch upstream for {collection['folder']}: {e}")
            return False

    def check_upstream_changes(self, collection: Dict) -> Dict:
        """Check for changes from upstream"""
        folder_path = self.repo_root / collection['folder']

        try:
            # Check if upstream exists
            existing = self._run_git(['remote'], cwd=folder_path)
            if 'upstream' not in existing:
                return {'status': 'no_upstream', 'ahead': 0, 'behind': 0}

            # Get commit counts
            behind_count = self._run_git(
                ['rev-list', '--count', 'HEAD..upstream/main'],
                cwd=folder_path
            )
            ahead_count = self._run_git(
                ['rev-list', '--count', 'upstream/main..HEAD'],
                cwd=folder_path
            )

            return {
                'status': 'ok',
                'behind': int(behind_count) if behind_count else 0,
                'ahead': int(ahead_count) if ahead_count else 0
            }
        except Exception as e:
            print(f"Error checking changes for {collection['folder']}: {e}")
            return {'status': 'error', 'ahead': 0, 'behind': 0}

    def setup_all_sources(self):
        """Set up upstream tracking for all collections"""
        print("Setting up upstream tracking for all collections...")
        print("=" * 60)

        for collection in self.config['collections']:
            if collection.get('tracking_enabled', True):
                self.add_upstream_remote(collection)

        print("=" * 60)
        print("Setup complete!")

    def check_all_sources(self):
        """Check status of all upstream repositories"""
        print("Checking upstream status for all collections...")
        print("=" * 60)

        status_report = []

        for collection in self.config['collections']:
            if not collection.get('tracking_enabled', True):
                print(f"⊘ {collection['folder']}: Tracking disabled")
                continue

            changes = self.check_upstream_changes(collection)

            if changes['status'] == 'no_upstream':
                print(f"⚠ {collection['folder']}: No upstream remote")
            elif changes['status'] == 'error':
                print(f"✗ {collection['folder']}: Error checking status")
            else:
                if changes['behind'] > 0:
                    print(f"↓ {collection['folder']}: {changes['behind']} commits behind upstream")
                elif changes['ahead'] > 0:
                    print(f"↑ {collection['folder']}: {changes['ahead']} commits ahead of upstream")
                else:
                    print(f"✓ {collection['folder']}: In sync with upstream")

                status_report.append({
                    'folder': collection['folder'],
                    'title': collection['title'],
                    'behind': changes['behind'],
                    'ahead': changes['ahead']
                })

        print("=" * 60)

        # Summary
        behind_count = sum(s['behind'] for s in status_report)
        ahead_count = sum(s['ahead'] for s in status_report)

        print(f"\nSummary:")
        print(f"  Total collections behind upstream: {behind_count}")
        print(f"  Total collections ahead of upstream: {ahead_count}")

        if behind_count > 0:
            print(f"\n⚡ Run 'python sync_sources.py sync-upstream' to merge changes")

    def sync_upstream(self, collection_folder: Optional[str] = None):
        """Sync with upstream (merge strategy: prefer local customizations)"""
        print("Syncing with upstream repositories...")
        print("=" * 60)

        for collection in self.config['collections']:
            if collection_folder and collection['folder'] != collection_folder:
                continue

            if not collection.get('tracking_enabled', True):
                print(f"⊘ {collection['folder']}: Tracking disabled")
                continue

            folder_path = self.repo_root / collection['folder']

            try:
                # Fetch latest
                self._run_git(['fetch', 'upstream'], cwd=folder_path)

                # Check for conflicts (we'll use ours strategy for customizations)
                status = self.check_upstream_changes(collection)

                if status['behind'] > 0:
                    print(f"\nMerging {status['behind']} upstream commits to {collection['folder']}...")

                    # Strategy: prefer local changes (ours) to protect customizations
                    merge_result = self._run_git(
                        ['merge', '-X', 'ours', 'upstream/main', '-m',
                         f'Sync with upstream: {datetime.now().isoformat()}'],
                        cwd=folder_path
                    )

                    print(f"✓ Synced {collection['folder']}")
                else:
                    print(f"✓ {collection['folder']}: Already up to date")

            except Exception as e:
                print(f"✗ Error syncing {collection['folder']}: {e}")

        # Update sync timestamp
        for collection in self.config['collections']:
            collection['last_sync'] = datetime.now().isoformat()

        self._save_config()
        print("=" * 60)
        print("Sync complete!")

    def generate_report(self) -> str:
        """Generate a markdown report of all sources"""
        report = "# Source Tracking Report\n\n"
        report += f"Generated: {datetime.now().isoformat()}\n\n"

        report += "## All Collections\n\n"

        for collection in self.config['collections']:
            report += f"### {collection['title']}\n\n"
            report += f"- **Original Author**: @{collection['original_author']}\n"
            report += f"- **Original URL**: [{collection['original_url']}]({collection['original_url']})\n"
            report += f"- **Tracking Enabled**: {'✓ Yes' if collection.get('tracking_enabled', True) else '✗ No'}\n"
            report += f"- **Last Synced**: {collection.get('last_sync', 'Never')}\n"
            report += f"- **Folder**: `{collection['folder']}`\n\n"

        return report

def main():
    import sys

    syncer = AwesomeSourceSync()

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == 'setup':
            syncer.setup_all_sources()
        elif command == 'check':
            syncer.check_all_sources()
        elif command == 'sync':
            target = sys.argv[2] if len(sys.argv) > 2 else None
            syncer.sync_upstream(target)
        elif command == 'report':
            report = syncer.generate_report()
            print(report)
            with open('SOURCES_REPORT.md', 'w') as f:
                f.write(report)
            print("\n✓ Report saved to SOURCES_REPORT.md")
        else:
            print(f"Unknown command: {command}")
            print("\nAvailable commands:")
            print("  setup   - Set up upstream tracking for all collections")
            print("  check   - Check status of all upstream repositories")
            print("  sync    - Sync with upstream (merge strategy: prefer local)")
            print("  report  - Generate source tracking report")
    else:
        syncer.check_all_sources()

if __name__ == '__main__':
    main()
