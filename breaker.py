import mss
import pyautogui
from PIL import Image
import time


#Game link:http://tanksw.com/piano-tiles/

def finder():
	x1=40
	x2=120
	x3=220
	x4=310
	#pyautogui.click(670,530)
	#time.sleep(0.5)
	with mss.mss() as sct:

		monitor={
			"top":280,
			"left":555,
			"width":345,
			"height":420
		}
	
	while True:
			sct_img=sct.grab(monitor)

			img = Image.new("RGB", sct_img.size)
			pixels = zip(sct_img.raw[2::4], sct_img.raw[1::4], sct_img.raw[0::4])
			img.putdata(list(pixels))

			for ylocal in range(60,320):
				if(img.getpixel((x1,ylocal))[0]==0):
					pyautogui.click(x1+monitor['left'],ylocal+monitor['top']+20,clicks=5)
					break
				
				if(img.getpixel((x2,ylocal))[0]==0):
					pyautogui.click(x2+monitor['left'],ylocal+monitor['top']+20,clicks=5)
					break
				
				if(img.getpixel((x3,ylocal))[0]==0):
					pyautogui.click(x3+monitor['left'],ylocal+monitor['top']+20,clicks=5)
					break
				
				if(img.getpixel((x4,ylocal))[0]==0):
					pyautogui.click(x4+monitor['left'],ylocal+monitor['top']+20,clicks=5)
					break				


finder()