import pyautogui
import pywinauto
import pytesseract
import camelot
import ghostscript
import pandas as pd
import pyperclip


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

size = pyautogui.size()
width, height = size[0], size[1]

# 글자를 찾을 영역 (클래스팅 또는 카톡)
find_area = [980,225,830,805] # 왼쪽위좌표, 가로, 세로

pyautogui.mouseInfo()

# pyautogui.sleep(4)
#shot_1 = pyautogui.screenshot(region=(980,225,830,805))

tables = camelot.read_pdf("class_personal_numbers.pdf")
#tables[0].df
df = tables[0].df        # pdf문서 내 표만 추출
df_ = tables[0].df[0]    # 표의 왼쪽 학번 열

#학번만 추출하여 리스트에 담기
num_list = []
for k in list(df_.iloc) :
    k = int(k)
    num_list.append(k)

time = 0
# 107**이 있는 셀의 열넘버 뽑기
for i in list(num_list)[0:24] :
    time += 1
    # df_에서 num_list에 있는 학번을 포함하고 있는 셀의 index를 리스트에 담기
    cell_index = df_.index[df_.str.find(str(i)) != -1].tolist()
    k = int(cell_index[0]) # 해당 cell의 행넘버
    new_cell = df.iloc[k][2]  # copy하고자 하는 셀
    print(i,'의 번호는', new_cell, '입니다')
    pyperclip.copy(str(new_cell))  # new_cell의 문자열을 클립보드에 복사

    # 마우스자동화
    pyautogui.moveTo(1415, 270 + 100*(time-1))
    print(pyautogui.position())
    pyautogui.click()
    pyautogui.sleep(5)
    pyautogui.moveTo(1760,215)
    pyautogui.click()
    pyautogui.sleep(5)
    pyautogui.moveTo(1258,870)
    pyautogui.click()
    pyautogui.sleep(5)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.moveTo(1611,873)
    pyautogui.click()
    pyautogui.sleep(5)
    pyautogui.moveTo(1625,120)
    pyautogui.click()
    pyautogui.sleep(5)
    pyautogui.moveTo(1811,135)
    pyautogui.click()
    pyautogui.sleep(5)
    if time in [8] :
        time = 0
        pyautogui.moveTo(1838,948)
        pyautogui.click()
        pyautogui.sleep(2)
    else : pass








#print(df)








