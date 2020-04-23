"""
https://docs.pytest.org/en/latest/example/simple.html
https://docs.pytest.org/en/2.7.3/plugins.html?highlight=re
"""
def pytest_report_header(config):
    return "project :spark-api-dev"

def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    print (">>> setting up", item)