import pytest
import random
import string
from pages.home_page import HomePage
from pages.daily_scenes import DailyScenes
from pages.saved_searches import SavedSearches
from utilities.base import Base
import pytest_check as check

search_request = 'San Francisco, CA'
rename_search = "San Francisco_renamed_test_" + ''.join(random.choices(string.ascii_lowercase, k=5))
updated_search = "San Francisco_updated_test_" + ''.join(random.choices(string.ascii_lowercase, k=5))


@pytest.mark.webtest
class TestPlanet(Base):

    @classmethod
    def teardown_class(cls):
        saved_searches = SavedSearches(cls.driver)
        home = HomePage(cls.driver)
        home.toggle_saved_searches()

        # Clear all saved searches left by the test
        search_titles = [rename_search, updated_search]
        for title in search_titles:
            saved_searches.filter_saved_searches(title)
            try:
                result = saved_searches.get_search_title()
                if result:
                    saved_searches.delete_saved_search()
            except Exception as e:
                continue
        cls.driver.close()

    def test_search_and_update_planet_express(self):
        """Test - Search and Update search result."""
        log = self.get_logger()
        home = HomePage(self.driver)
        daily_scenes = DailyScenes(self.driver)
        saved_searches = SavedSearches(self.driver)

        # ----------------------Steps--------------------------------------

        # Input search location and click enter
        # TODO: Defect-ID:  PE-4 (see attached .pdf)
        home.search_location(search_request)
        log.info("Entered Search Request")

        # DEFECT-ID: PE-2 - Update assertion to check order scenes and cadence after DE is fixed.(see attached PDF)
        error = daily_scenes.get_error_title()
        check.not_equal(error, "Sorry, no results found",
                        msg=f"Daily catalog is not loaded, got an error: {error}")

        # Save Search
        daily_scenes.click_save_update_search()
        daily_scenes.save_search_result(rename_search)
        log.info("Saved Search Results")

        # Verify that search result was saved
        # TODO: DEFECT-ID: PE-1 - Remove workaround for this DE from the method below when fixed.(see attached PDF)
        home.toggle_saved_searches()

        # Filter Saved Searches
        saved_searches.filter_saved_searches(rename_search)

        # Find Search title and assert it.
        title = saved_searches.get_search_title()
        assert title == rename_search

        # Update the saved Search
        saved_searches.click_saved_search()

        daily_scenes.click_save_update_search()

        daily_scenes.save_search_result(updated_search)

        # Verify the updated search card after the update.
        home.toggle_saved_searches()

        saved_searches.filter_saved_searches(updated_search)
        updated_title = saved_searches.get_search_title()
        assert updated_title == updated_search
        log.info("Saved Search is Updated")

    def test_saved_search_already_exist(self):
        """Test - Save search results with existing name"""
        daily_scenes = DailyScenes(self.driver)
        saved_searches = SavedSearches(self.driver)

        # ----------------------Steps--------------------------------------
        saved_searches.click_saved_search()
        daily_scenes.click_save_update_search()
        daily_scenes.save_search_result(updated_search, save_as_new=True)

        expected_msg = "A saved search already exists with that name"
        error_msg = saved_searches.get_search_already_exist_message()
        assert error_msg == expected_msg

        saved_searches.click_close_save_search_dialog()
