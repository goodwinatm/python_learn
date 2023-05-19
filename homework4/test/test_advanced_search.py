from homework4.homework4_pages.main_page import MainPage
class TestSearchPO:
    def setup_class(self):
        self.main = MainPage()


    def setup(self):
        self.main.to_login()
        print("setup login")
        self.search = self.main.to_search_advance()
    def teardown(self):
        self.main.to_logout()

    def teardown_class(self):
        self.main.close()

    def test_search(self):
        assert 'selenium' in str(self.search.search('selenium')
                                 .get_search_result()[0]).lower()
    def test_search_advanced_flag(self):
        assert False == self.search.search_advanced_flag()
    # 1. 切换三个话题，在不同类目中搜索
    # 话题/帖子
    def test_dropdown_search_1(self):
        assert 'selenium' in str(self.search.select_search_1('selenium')
                                 .get_search_result()[0]).lower()

    # 1. 切换三个话题，在不同类目中搜索
    # 类别/标签
    def test_dropdown_search_2(self):
        assert 'java' in str(self.search.select_search_2('java')
                                 .get_search_tag_result()[0]).lower()

    # 1. 切换三个话题，在不同类目中搜索
    # 用户
    def test_dropdown_search_3(self):
        assert 'java' in str(self.search.select_search_3('java')
                                 .get_search_user_result()[0]).lower()
    def test_search2(self):
        assert 'chromedriver' in str(self.search.search('selenium chromedriver')
                                     .get_search_result()[0]).lower()
    #2. 筛选条件增加 发帖人、发布时间
    def test_search3(self):
        assert 'api' in str(self.search.posted_by_search(' java','JAVA')
                                     .get_search_post_result()[0]).lower()