import json
from pathlib import Path
from sync_sources import AwesomeSourceSync


def write_sources(tmp_path, collections):
    data = {"collections": collections}
    path = tmp_path / "SOURCES.json"
    path.write_text(json.dumps(data))
    return path


def test_generate_report(tmp_path):
    collections = [
        {
            "folder": "sample",
            "title": "Sample Collection",
            "original_author": "alice",
            "original_url": "https://example.com",
            "tracking_enabled": True,
        }
    ]
    cfg = write_sources(tmp_path, collections)
    (tmp_path / "sample").mkdir()

    syncer = AwesomeSourceSync(config_file=str(cfg))
    syncer.repo_root = tmp_path

    report = syncer.generate_report()
    assert "Sample Collection" in report
    assert "sample" in report


def test_check_upstream_changes_no_upstream(tmp_path):
    collections = [
        {"folder": "sample", "title": "Sample", "original_author": "a", "original_url": "u"}
    ]
    cfg = write_sources(tmp_path, collections)
    (tmp_path / "sample").mkdir()

    syncer = AwesomeSourceSync(config_file=str(cfg))
    syncer.repo_root = tmp_path

    # Simulate no remotes
    def fake_run_git(args, cwd=None):
        if args == ["remote"]:
            return ""
        return ""

    syncer._run_git = fake_run_git

    result = syncer.check_upstream_changes(collections[0])
    assert result["status"] == "no_upstream"
    assert result["behind"] == 0
    assert result["ahead"] == 0


def test_check_upstream_changes_counts(tmp_path):
    collections = [
        {"folder": "sample", "title": "Sample", "original_author": "a", "original_url": "u"}
    ]
    cfg = write_sources(tmp_path, collections)
    (tmp_path / "sample").mkdir()

    syncer = AwesomeSourceSync(config_file=str(cfg))
    syncer.repo_root = tmp_path

    def fake_run_git(args, cwd=None):
        # remote check
        if args == ["remote"]:
            return "origin\nupstream"
        # behind count
        if args[:3] == ["rev-list", "--count", "HEAD..upstream/main"]:
            return "3"
        # ahead count
        if args[:3] == ["rev-list", "--count", "upstream/main..HEAD"]:
            return "2"
        return ""

    syncer._run_git = fake_run_git

    result = syncer.check_upstream_changes(collections[0])
    assert result["status"] == "ok"
    assert result["behind"] == 3
    assert result["ahead"] == 2


def test_sync_upstream_triggers_merge_when_behind(tmp_path):
    collections = [
        {"folder": "sample", "title": "Sample", "original_author": "a", "original_url": "u", "tracking_enabled": True}
    ]
    cfg = write_sources(tmp_path, collections)
    (tmp_path / "sample").mkdir()

    syncer = AwesomeSourceSync(config_file=str(cfg))
    syncer.repo_root = tmp_path

    calls = []

    def fake_run_git(args, cwd=None):
        calls.append(list(args))
        # fetch
        if args[:2] == ["fetch", "upstream"]:
            return ""
        # remote
        if args == ["remote"]:
            return "origin\nupstream"
        # behind > 0
        if args[:3] == ["rev-list", "--count", "HEAD..upstream/main"]:
            return "1"
        # ahead == 0
        if args[:3] == ["rev-list", "--count", "upstream/main..HEAD"]:
            return "0"
        # merge
        if args and args[0] == "merge":
            return "Merged"
        return ""

    syncer._run_git = fake_run_git

    syncer.sync_upstream()

    # assert merge was invoked
    assert any(call and call[0] == "merge" for call in calls)


def test_add_upstream_remote_adds_when_missing(tmp_path):
    collections = [
        {"folder": "sample", "title": "Sample", "original_author": "a", "original_url": "https://example.com", "tracking_enabled": True}
    ]
    cfg = write_sources(tmp_path, collections)
    (tmp_path / "sample").mkdir()

    syncer = AwesomeSourceSync(config_file=str(cfg))
    syncer.repo_root = tmp_path

    called = {"add": False}

    def fake_run_git(args, cwd=None):
        # list remotes -> none
        if args == ["remote"]:
            return "origin"
        # add remote
        if args[:2] == ["remote", "add"]:
            called["add"] = True
            return ""
        return ""

    syncer._run_git = fake_run_git

    result = syncer.add_upstream_remote(collections[0])
    assert result is True
    assert called["add"] is True
