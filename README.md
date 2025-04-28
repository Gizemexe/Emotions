# Moodify 🎵 - Song Recommendation Based on Emotion Recognition
<p> <b> Music meets AI: Real-time facial emotion recognition combined with Spotify-powered personalized music recommendations. </b></p>

### Installation & Setup
<b>1. Clone the Repository</b>
   ```
   git clone https://github.com/your-username/moodify.git
   cd moodify
   ```
<b>2. Install Required Libraries</b>
   - Ensure you have Python installed (preferably 3.8+).
   - Install the dependencies:
     
   ```
   pip install -r requirements.txt
   ```

<b><i>Main libraries used:</i></b>
  - *TensorFlow* / *Keras*  - For deep learning model 
  - *OpenCV* - For real-time webcam access 
  - *Spotipy (Spotify Web API Python Library)* - Spotify Web API Python client 
  - *Flask (for Web Interface)* - For web-based user interface 

<b>3. Set Up Spotify Credentials</b>
 - You must create a Spotify Developer account and obtain:
     - *Client ID*
     - *Client Secret*
 - Then create a .env file in the root directory and add:
   
   ```
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret

   ```

<b> 4. Run the Application </b>

```
python app.py
```
<b> 5. Access the web application via:</b>

```
http://localhost:5000
```

📁 Project Structure
```
moodify/
├── models/
│   └── emotion_model.h5    # Trained CNN model
├── static/
│   ├── css/
│   │   └── styles.css      # Styling for UI
│   └── img/
│       └── logo.png        # (Optional) project logo
├── templates/
│   └── index.html          # Frontend page
├── app.py                  # Main Flask application
├── utils.py                # Helper functions (Spotify connection, prediction)
├── requirements.txt        # Python dependencies
└── README.md               # Project description
```
## Project Overview
<p> Moodify is a smart music recommendation system that recognizes user emotions from facial expressions and recommends songs accordingly using Spotify's vast music library. </p>

# ✨ Features
- **Real-Time Emotion Detection:** Webcam captures emotions live.
- **Spotify Playlist Integration:** Songs matched to emotions.
- **User-Friendly Interface:** Lightweight and intuitive frontend.
- **Emotion Categories:**
     - Happy
     - Sad
     - Angry
     - Fear
     - Disgust
     - Neutral
     - Surprised

# 🧠 How it Works
   - **Capture user's facial expression via webcam**
   - **Predict emotional state using CNN model**
   - **Fetch playlists using Spotify Search API**
   - **Recommend a curated list of songs**

# 🧪 Technical Details
**Model:**
   - 4 convolutional layers (32 → 64 → 128 → 128 filters)
   - MaxPooling (2x2)
   - Dropout layers (25% and 50%)
   - Fully Connected Dense layers

**Training Settings:**
   - *Optimizer:* Adam (learning rate: 0.0001)
   - *Loss:* Categorical Crossentropy
   - *Epochs:* 100
   - *Batch Size:* 64
   - *Spotify API:* Used Spotipy to search playlists and retrieve track information based on emotional state.
     ![Her hücre için tabloSatırı hücre aramaMetnini içeriyor](https://github.com/user-attachments/assets/61e8565e-9a3e-4926-9e25-719ae6d65803)
   - **Data:** FER-2013 Dataset
   - **Libraries:** TensorFlow, OpenCV, Spotipy, Flask, Bootstrap

# 📸 Screenshots
  *Real-Time Emotion Detection*
  ![image](https://github.com/user-attachments/assets/36b523e1-c6c8-4cd9-a52a-884f96b7cc30)

  *Music Recommendation*
  ![image](https://github.com/user-attachments/assets/33480b3f-d150-4897-81ef-76e3c4ed67ba)

  
# 🖥️ User Interface
  - Built using *HTML*, *CSS*, *Bootstrap*
  - Real-time video stream displaying facial emotion detection
  - "**Show Song**" button triggers dynamic playlist update based on emotion

# 📈 Model Performance
**Final chosen model achieved balanced accuracy:**
  - *Training Accuracy: ~55%*
  - *Validation Accuracy: ~57%*
![image](https://github.com/user-attachments/assets/ca0ec39f-13a6-4715-9f85-2b81dd0e057c)
  - Minimal overfitting observed after tuning with dropout layers.

# ⚡ Challenges Faced
- Overfitting issues during model training ➔ Solved by data augmentation and dropout regularization.
  ![image](https://github.com/user-attachments/assets/669229e3-7621-4b1c-9d4e-d722c27a343e)
- Spotify API Authorization issues ➔ Changed approach to use /search endpoint.
  ![image](https://github.com/user-attachments/assets/6e722ea0-e63c-466f-97b9-7134f3e10d85)
- Mapping emotions to suitable music genres manually due to Spotify's limitations.

# 📰 Conclusion
  <p> The "Moodify" project successfully integrated facial emotion recognition with personalized music recommendations.
During model training, overfitting was a concern. We addressed this by using data augmentation and adding dropout layers to the CNN. However, 
a noticeable gap between training and validation accuracy suggests further tuning of hyperparameters and model adjustments are needed for better generalization.
While the system achieved its goal, further optimization of the model and API integration will enhance performance and user experience.</p>

# 🔮 Future Work
  - Improve model robustness with larger, diverse datasets
  - Incorporate user feedback for smarter recommendations
  - Direct integration with Spotify for seamless experience
  - Enhance real-time performance with lightweight models

# 📚 References
  - [Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api)
  - [Keras Layers Documentation](https://keras.io/api/layers/)
  - [FER2013 Dataset on Kaggle](https://www.kaggle.com/datasets/msambare/fer2013)

## ✨ Team
| Name | URL |
|------|------|
|Gizem EROL| [GitHub](https://github.com/Gizemexe)|
|Selvinaz Zeynep KIYIKCI| [GitHub](https://github.com/selvikiyikci)|
|Zeynep Sude KIRMACI| [GitHub](https://github.com/zeynepkrmc)|

