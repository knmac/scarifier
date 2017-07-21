# Movie Genie
This is a project for [IBM's BlueHack 2017](http://www.bluehack.org).

- Challenge: #VideoComprehensionSolutions
- Team Name: Connected Cognition
- Location: #Yorktown / #Poughkeepsie
- Members:
  - Vaisakhi Mishra - vaisakhi.mishra@ibm.com
  - Charlotte Wright - Charlotte.Wright@ibm.com
  - Khoi-Nguyen Mac - Khoi-Nguyen.Mac@ibm.com
  - Pat Pataranutaporn - Pat.Pataranutaporn@ibm.com
  - German Abrevaya - german.abrevaya@ibm.com
- Hack Dash: https://hackdash.org/projects/5970c0c97a30a4526a1fe9a7
- Video Link: https://drive.google.com/open?id=0B_INX3BifvJoUV92SGNFN0Z2VGs
  
![interface](res/interface.png?raw=true "Interface")

# Description
An emotion analysis based real time movie scene modifying video player. The current prototype would enhance audience experience of any horror movie or video by manipulating effects in the video according to the facial mood gestures of the audience.

Link to Presentation: Coming soon

Link to 3 minute pitch video: https://drive.google.com/open?id=0B_INX3BifvJoUV92SGNFN0Z2VGs

Link to Demo: https://www.youtube.com/watch?v=GNbztukrhgo

GitHub: https://github.com/knmac/scarifier 

# Workflow
![workflow](res/movie_genie_workflow.png?raw=true "Worl Flow")


While the film is playing, the emotion of the watcher is recognized by the Watson Facial Recognition API and categorized as either a negative or positive emotions. The movie player uses this data to change to content of the video. The film is pre-examined with the Watson Visual Recognition API to tag the content of the video to improve the quality of the changes. It uses the augmentation library to change the mood of the film using music and visual effects. The final product is a video which atmosphere changes based on the user data and content of the video. 


![candidate](res/candidate_appearance.png?raw=true "Candidate")

This graph tracks the appearance of the candidate (the scary monster in this case). It uses the Watson Recognition API to analyze the content on the screen to make it easier to pin point where the editor could quickly increase the fear factor. 
