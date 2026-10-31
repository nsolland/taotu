import hashlib, json, pathlib, tempfile, unittest
from scripts.validate_publication import run

class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)
        (self.root / "chapters").mkdir()
        (self.root / "releases").mkdir()
        (self.root / "chapters" / "sample.md").write_text("Sample original chapter\n")
        self.d = {
            "chapter_id": "chapter-001", "edition_id": "edition-001",
            "language": "en", "original_language": "en",
            "title": "Sample", "source_commit": "a" * 40,
            "path": "chapters/sample.md",
            "sha256": hashlib.sha256((self.root / "chapters" / "sample.md").read_bytes()).hexdigest(),
            "rights_status": "cleared", "evidence_status": "bounded", "author_approved": True
        }
        self.save()
    def tearDown(self): self.tmp.cleanup()
    def save(self):
        (self.root / "chapters" / "sample.chapter.json").write_text(json.dumps(self.d))
    def test_valid(self): run(self.root)
    def test_digest_mismatch(self):
        self.d["sha256"] = "0" * 64; self.save()
        with self.assertRaisesRegex(ValueError, "digest"): run(self.root)
    def test_no_author_approval(self):
        self.d["author_approved"] = False; self.save()
        with self.assertRaisesRegex(ValueError, "approval"): run(self.root)
    def test_no_rights(self):
        self.d["rights_status"] = "pending"; self.save()
        with self.assertRaisesRegex(ValueError, "rights"): run(self.root)
    def test_path_traversal(self):
        self.d["path"] = "chapters/../../outside.md"; self.save()
        with self.assertRaisesRegex(ValueError, "unsafe"): run(self.root)
    def test_translation_requires_provenance(self):
        self.d["language"] = "no"; self.save()
        with self.assertRaisesRegex(ValueError, "translation"): run(self.root)
    def test_release_unknown_chapter(self):
        self.save()
        (self.root / "releases" / "first.release.json").write_text(json.dumps({
            "release_id": "release-001", "author_approved": True, "rights_status": "cleared",
            "chapters": [{"chapter_id": "unknown", "edition_id": "edition-001", "language": "en"}]
        }))
        with self.assertRaisesRegex(ValueError, "unknown"): run(self.root)
    def test_valid_release(self):
        (self.root / "releases" / "first.release.json").write_text(json.dumps({
            "release_id": "release-001", "author_approved": True, "rights_status": "cleared",
            "chapters": [{"chapter_id": "chapter-001", "edition_id": "edition-001", "language": "en"}]
        }))
        run(self.root)

if __name__ == "__main__": unittest.main()
