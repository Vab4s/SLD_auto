MODAL_WINDOW = ('xpath', '//div[@qa-id="modal-window"]')
MODAL_TITLE = ('xpath', '(//div[@qa-id="modal-window"]//div[@class="modal-window__header"]//div)[1]')


MODAL_LABEL_DATE_TIME = ('xpath', '//div[@class="modal-window"]//label')

# value="2025-01-09"
MODAL_DATE_PICKER = ('xpath', '//div[@class="modal-window"]//anchor-date-picker')
# value="16:47:00-0100"
MODAL_TIME_PICKER = ('xpath', '//div[@class="modal-window"]//anchor-time-picker')

MODAL_RADIO_NEW_VOYAGE = ('xpath', '//div[@class="modal-window"]//anchor-radio[@label="New voyage"]')
MODAL_RADIO_CURRENT_VOYAGE = ('xpath', '//div[@class="modal-window"]//anchor-radio[@label="Current voyage"]')

MODAL_RADIO_CURRENT_CHARTERPARTY = ('xpath', '//div[@class="modal-window"]//anchor-radio[@label="Current charterparty"]')
MODAL_RADIO_NO_CHARTERPARTY = ('xpath', '//div[@class="modal-window"]//anchor-radio[@label="No charterparty"]')
MODAL_RADIO_NEW_CHARTERPARTY = ('xpath', '//div[@class="modal-window"]//anchor-radio[@label="New charterparty"]')

MODAL_TOGGLE = ('xpath', '//div[@class="modal-window"]//anchor-toggle')