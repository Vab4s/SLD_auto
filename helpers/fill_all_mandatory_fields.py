from pages.base_page import BasePage

def fill_all_mandatory_fields(driver):
    # олучение всех обязательных элементов (со значением "--mandatory" в классе)
    elements = driver.find_elements('xpath', '//*[contains(@class, "--mandatory")]')
    print()
    # перебор всех найденных элементов
    for element in elements:
        # если в теге присутствует параметр 'placeholder'
        if element.get_attribute('placeholder') is not None:
            # если элемент button
            if element.tag_name == 'button':
                pass
                # Нажать на кнопку
                # выбрать какой-либо элемент
            else:
                print(element.tag_name, element.get_attribute('qa-id'), element.get_attribute('placeholder'))
                # получить placeholder
                # получить верхнюю и нижнюю границы
                # ввести в поле значение в промежутке между верхней и нижней границей
        # иначе если в теге отсутствует параметр 'placeholder'
        else:
            # если элемент - поле ввода даты
            if element.tag_name == 'anchor-date-picker':
                # водим рандомную дату от минимального значения до сегодняшней даты
                print(element.tag_name, element.get_attribute('qa-id'), element.get_attribute('min'))
            # если элемент - поле ввода времени
            # для репортов
            # пока не реализовывалось
            elif element.tag_name == 'anchor-time-picker':
                pass
            # иначе если элемент - какое-либо другое поле ввода
            # пример - ввод MCR оборудования
            else:
                # получаем элемент
                inner_element = element.find_element('xpath', './/*[@placeholder]')
                print(inner_element.tag_name, inner_element.get_attribute('qa-id'),
                      inner_element.get_attribute('placeholder'))
                # вводим значение из диапазона laceholder

# ВНИМАНИЕ!
# Fuel consumption
# Bunkering lot name
#
# Div, не имеет plaxeholder'a (первый else)
# Но нажимать нужно внутренний anchor-dropdown

# Ф-я поиска тегов
# Ф-я заполнения
# Ф-я нажатия на кнопку
# Ф-я выбора из списка