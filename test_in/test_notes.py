from pages import notes_page

class Test_Notes():

    def test_notes_add(self, invoke):
        notespage = notes_page.Notes_Page(invoke)
        notespage.go_to_home()
        notespage.navigate_to_notes()
        notespage.open_add_notes()
        notespage.fill_notes_info("new name", "new short body text")
        notespage.save_modal()
        