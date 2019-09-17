import pytest


@pytest.mark.usefixtures('init_notes_page')
@pytest.mark.usefixtures('invoke')
class TestNotes:

    def test_notes_add(self):
        self.notespage.go_to_home()
        self.notespage.navigate_to_notes()
        self.notespage.open_add_notes()
        self.notespage.fill_notes_info("new name", "new short body text")
        self.notespage.save_modal()

    def test_wait(self):
        pass