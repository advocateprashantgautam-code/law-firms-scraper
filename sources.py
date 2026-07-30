"""
sources.py

Public sources used for collecting Delhi law firms.
Only publicly available sources should be added here.
"""

SOURCES = [

    {
        "name": "Legal Firms Directory",
        "url": "https://directory.legalfirms.in/"
    },

    {
        "name": "The Indian Legal Directory",
        "url": "https://www.theindianlegaldirectory.com/"
    },

    {
        "name": "Legal500 India",
        "url": "https://www.legal500.com/"
    }

]


def get_sources():
    """
    Returns all configured public sources.
    """
    return SOURCES