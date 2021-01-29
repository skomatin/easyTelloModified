from tello import Tello
import time
import threading
import cv2

# def fly():
#     print("Attempting to fly...")
#     my_drone.takeoff()
#     # print("Take off complete")
#     time.sleep(2)

#     for _ in range(2):
#         # my_drone.forward(50)
#         # print("Forward complete")
#         # time.sleep(2)
#         my_drone.cw(360)
#         # print("CW complete")
#         # time.sleep(2)
#     my_drone.land()

# def getStats():
#     while(True):
#         print(my_drone.get_speed())
#         print(my_drone.get_battery())
#         print(my_drone.get_time())
#         print(my_drone.get_height())
#         time.sleep(5)

if __name__ == "__main__":
    my_drone = Tello(debug=True)
    print(my_drone.get_battery())
    
    # t1 = threading.Thread(target=fly)
    # t2 = threading.Thread(target=getStats)
    my_drone.streamon()
    time.sleep(5)

    start_time = time.time()
    fly_complete = False
    while(True):

        if not fly_complete:
            # t1.start()
            # t2.start()
            my_drone.takeoff()
            my_drone.cw(360)
            my_drone.land()
            fly_complete = True

        # Capture frame-by-frame
        frame = my_drone.last_frame
        if frame is None: continue
        frame = cv2.resize(frame, (360, 240))

        # # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    my_drone.streamoff()