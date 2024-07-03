import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import cv2
from fer import FER

# Initialize the emotion detector
emotion_detector = FER()

# Function to capture and display video
def show_frame():
    ret, frame = cap.read()
    if ret:
        emotion, score = emotion_detector.top_emotion(frame)
        
        if emotion:
            cv2.putText(frame, f'{emotion} ({score*100:.2f}%)', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Convert frame to RGB
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

# Set up GUI
root = tk.Tk()
root.title("Emotion Detector")

# Initialize webcam
cap = cv2.VideoCapture(0)

lmain = Label(root)
lmain.pack()

show_frame()
root.mainloop()

# Release the capture
cap.release()
cv2.destroyAllWindows()
