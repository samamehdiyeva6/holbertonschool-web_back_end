def indef_range(page, page_size):
    """Returns a list of page numbers to display in pagination."""
    start = (page - 1) * page_size
    end = start + page_size
    return list(range(start, end))
