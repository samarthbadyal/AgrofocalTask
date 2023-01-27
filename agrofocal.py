import cv2

def agrofocal(fileName, newFile):
    vid = cv2.VideoCapture(fileName)        # reads original video

    vidFPS = vid.get(cv2.CAP_PROP_FPS)                  # pulls fps
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)         # pulls frame height
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)           # pulls frame width

    ret, frame = vid.read()             # reads each frame of the video
    fourcc = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')         # fourcc code
    writer = cv2.VideoWriter(newFile, apiPreference = 0, 
    fourcc = fourcc, fps = vidFPS, frameSize=(1280,720))            # videoWriter object to write new vid
    frames = []        

    while True:
        ret, frame = vid.read()
        if not ret:
            break
        frame = cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)     # resizes the frame
        frames.append(frame)        # adds frame to the list

        if cv2.waitKey(1) & 0xFF == ord('q'):       # kills the loop and ends the video
            break

    for i in frames[::-1]:          # reverses the video
        writer.write(i) 

    writer.release()
    vid.release()
    cv2.destroyAllWindows()

