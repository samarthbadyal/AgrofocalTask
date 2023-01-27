import cv2

vid = cv2.VideoCapture('/Users/samarthbadyal/Downloads/IMG_0532.MOV')        # reads original video
aud = vid.get()

vidFPS = vid.get(cv2.CAP_PROP_FPS)                  # pulls fps
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)         # pulls frame height
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)           # pulls frame width

ret, frame = vid.read()             # reads each frame of the video
fourcc = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')         # fourcc code
writer = cv2.VideoWriter('/Users/samarthbadyal/Downloads/NewMov.mov', apiPreference = 0, 
fourcc = fourcc, fps = vidFPS, frameSize=(640,480))            # videoWriter object to write new vid
frames = []        

while True:
    ret, frame = vid.read()
    if not ret:
        break
    frame = cv2.resize(frame,(640,480),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)     # resizes the frame
    frames.append(frame)        # adds frame to the list

    if cv2.waitKey(1) & 0xFF == ord('q'):       # kills the loop and ends the video
        break

frames = frames[::-1]
aud = aud[::-1]

for f in frames[::-1]:          # reverses the video
    writer.write(frame)
    writer.write(aud)

writer.release()
vid.release()
cv2.destroyAllWindows()
