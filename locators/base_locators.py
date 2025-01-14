NOTIFICATION = ('xpath', '//div[@class="row alert-notification"]')  # нотификашка
BUTTON_NOTIFICATION_CLOSE = ('xpath', '//anchor-icon[@qa-id="notification-close-btn"]') # закрыть нотификашку

BUTTON_CLOSE = ('xpath', '//anchor-icon[@qa-id="modal-close-button"]')

BUTTON_SUCCESS = ('xpath', '//anchor-button[@qa-id="modal-success-button"]')
BUTTON_NEGATIVE = ('xpath', '//anchor-button[@qa-id="cancel-button"]')

BUTTON_SAVE = ('xpath', '//anchor-button[@qa-id="btn-save"]')
BUTTON_SEND = ('xpath', '//anchor-button[@qa-id="btn-send"]')

BUTTON_PREFILL_MENU_ITEM = ('xpath', '//anchor-button[@qa-id="menu-item-prefill"]')
BUTTON_DELETE_MENU_ITEM = ('xpath', '//anchor-button[@qa-id="menu-item-delete"]')
BUTTON_SAVE_MENU_ITEM = ('xpath', '//anchor-button[@qa-id="menu-item-save"]')

BUTTON_BACK = ('xpath', '//anchor-button[@qa-id="back-button"]')
BUTTON_NEXT = ('xpath', '//anchor-button[@qa-id="next-button"]')

# Включение/выключение создания репорта
TOGGLE_MODAL_WINDOW= ('xpath', '//div[@class="modal-window"]//descendant::anchor-toggle[@role="switch"]')

#Статусы
STATUS_SYNCED = ('xpath', '//div[@data-status="synced"]')
STATUS_READY_TO_SYNC = ('xpath', '//div[@data-status="ready_to_sync"]')
STATUS_REQUIRES_REVIEW = ('xpath', '//div[@data-status="requires_review"]')