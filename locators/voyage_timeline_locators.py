TIMELINE_ITEM_EVERY = ('xpath', '//div[contains(@class, "timeline-item")]')

TIMELINE_REPORT = ('xpath', '//div[contains(@qa-id, "timeline-report")]')
TIMELINE_EVENT = ('xpath', '//div[contains(@qa-id, "timeline-event")]')

TIMELINE_REPORT_TITLE = ('xpath', '//div[contains(@qa-id, "timeline-report")]//div[@qa-id="timeline-title"]')
TIMELINE_EVENT_TITLE = ('xpath', '//div[contains(@qa-id, "timeline-event")]//div[@qa-id="timeline-title"]')

TIMELINE_REPORT_DATE = ('xpath', '//div[contains(@qa-id, "timeline-report")]//div[@qa-id="timeline-date"]')
TIMELINE_EVENT_DATE = ('xpath', '//div[contains(@qa-id, "timeline-event")]//div[@qa-id="timeline-date"]')

TIMELINE_REPORT_TIME = ('xpath', '//div[contains(@qa-id, "timeline-report")]//div[@qa-id="timeline-time"]')
TIMELINE_EVENT_TIME = ('xpath', '//div[contains(@qa-id, "timeline-event")]//div[@qa-id="timeline-time"]')

TIMELINE_DEPARTURE_REPORT = ('xpath', '//div[text()="{}"]//ancestor::div[contains(@qa-id, "timeline-report")]')