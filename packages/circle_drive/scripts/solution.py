
def solution(obs):
    img_gray = cv2.cvtColor(obs, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(obs, cv2.COLOR_BGR2HSV)
    bin_yellow = cv2.inRange(hsv, (20, 80, 80), (110, 255, 255))
    num_yellow = np.count_nonzero(bin_yellow)
    point_yellow = []

    stop_flag = False

    if num_yellow > 40:
         k = 0
         jold = 0
         for i in range((bin_yellow.shape[0] - 1), 100, -10):
              # print(bin_yellow.shape[0]-1)
              if stop_flag == True:
                   break
              for j in range(0, bin_yellow.shape[1] // 2, 10):
                   # print(j)
                   if bin_yellow[i, j] > 0:
                       point_yellow.append([j, i])
                       print(point_yellow)
                       k += 1
                       if abs(jold - j) > 100 and k > 0:
                           point_yellow.pop()
                           stop_flag = True
                       jold = j
                            # print('end')
                       break
     #print(point_yellow)
     error_yel = 0
     i = 1
     h = 0
     for yel in point_yellow:
         print(yel)
         h = yel[1] * 0.001 + 1
         error_yel = h * (118 - yel[0]) + error_yel
         i = i + 1
     error_yel = error_yel / i
            
     pr = error_yel * 0.04
     angle = pr

         vel = 0.4
     return [vel, angle]
