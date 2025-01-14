TIMELINE_ITEM_BY_QAID = ('xpath', '//div[contains(@qa-id, "timeline-{}")]')
TIMELINE_ITEM_BY_TEXT = ('xpath', '//div[text()="{}"]')
TIMELINE_ITEM_EVERY = ('xpath', '//div[contains(@class, "timeline-item")]')

TIMELINE_QA_ID = ('xpath', '//div[@qa-id="{}"]')
TIMELINE_DATE_TIME = ('xpath', '//div[contains(@qa-id, "timeline-{}")]//descendant::div[@class="{}"]')


# TIMELINE_EVENT_DATE = ('xpath', '//div[contains(@qa-id, "timeline-event")]//descendant::div[@class="date"]')
# TIMELINE_EVENT_TIME = ('xpath', '//div[contains(@qa-id, "timeline-event")]//descendant::div[@class="time"]')
#
# TIMELINE_REPORT_DATE = ('xpath', '//div[contains(@qa-id, "timeline-report")]//descendant::div[@class="date"]')
# TIMELINE_REPORT_TIME = ('xpath', '//div[contains(@qa-id, "timeline-report")]//descendant::div[@class="time"]')


LAST_ADDED_EVENT = ('xpath', '(//div[contains(@qa-id, "timeline-event")])[1]')
LAST_ADDED_REPORT = ('xpath', '(//div[contains(@qa-id, "timeline-report")])[1]')


