# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys
import math

if __name__ == '__main__':
    print(__doc__)

    fn = "straight.jpg"

    while True:
        src = cv2.imread(fn)
        dst = cv2.Canny(src, 10, 50)
        row,col,ch=src.shape
        lines = cv2.HoughLinesP(dst, 1, math.pi/180.0, 40, np.array([]), 50, 10)
        if lines is not None:
            a,b,c = lines.shape
            for i in range(a):
                if max(lines[i][0][1],lines[i][0][3])>row/2:
                    cv2.line(src, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
        cv2.imshow("detected lines", src)
        ch = cv2.waitKey(0) & 0xFF
        if ch == ord('a'):
            fn="straight.jpg"
            print('straight')
        if ch == ord('s'):
            fn="left.jpg"
            print('left')
        if ch == ord('d'):
            fn="right.jpg"
            print('right')
        if ch == 27:
            break
    cv2.destroyAllWindows()
