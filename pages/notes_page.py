from driver import WebDriver

class Notes_Page:

    def __init__(self, invoke):
        self.driver = WebDriver(driver=invoke)
        self.navigation_notes = "//span[@id='nav-notes']"
        self.notes_logo = "//p[@id='notes-logo']"
        self.home_logo = "//p[@id='home-logo']"
        self.add_notes_button = "//button[@id='add-notes-button']"
        self.add_notes_modal_header = "//p[@id='add-notes-modal-header' and text()='Add New Note']"
        self.input_universal = "//input[@name='{}']"
        self.save_button_modal = "//button[@id='save-modal']"


    def go_to_home(self):
        self.driver.go_to_url("http://127.0.0.1:3000")
        self.driver.wait_for_visibility_of_web_element(self.home_logo)

    def navigate_to_notes(self):
        self.driver.wait_for_visibility_of_web_element(self.navigation_notes)
        self.driver.click_web_element(self.navigation_notes)
        self.driver.wait_for_presence_of_element_located(self.notes_logo)

    def open_add_notes(self):
        self.driver.wait_for_presence_of_element_located(self.add_notes_button)
        self.driver.wait_for_web_element_to_be_clickable(self.add_notes_button)
        self.driver.click_web_element(self.add_notes_button)
        self.driver.wait_for_visibility_of_web_element(self.add_notes_modal_header)

    def fill_notes_info(self, note_name, note_body):
        name_selector = self.input_universal.format('name')
        note_selector = self.input_universal.format('note')
        self.driver.wait_for_presence_of_element_located(name_selector)
        self.driver.set_web_element_text(name_selector, note_name)
        self.driver.wait_for_presence_of_element_located(note_selector)
        self.driver.set_web_element_text(note_selector, note_body)

    def save_modal(self):
        self.driver.wait_for_web_element_to_be_clickable(self.save_button_modal)
        self.driver.click_web_element(self.save_button_modal)
        self.driver.wait_for_visibility_of_web_element(self.notes_logo)
