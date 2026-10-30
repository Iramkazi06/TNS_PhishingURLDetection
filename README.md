\# Phishing URL Detector



A machine learning-based web application designed to detect potentially malicious and phishing URLs. The project analyzes URL features and uses a trained machine learning model to classify URLs as legitimate or phishing.



\## Features



\- Detect potentially phishing URLs.

\- Extract URL-based features for analysis.

\- Use a trained machine learning model for prediction.

\- Web-based frontend for user interaction.

\- Display model evaluation metrics.



\## Tech Stack



\- \*\*Programming Language:\*\* Python

\- \*\*Machine Learning:\*\* Scikit-learn

\- \*\*Frontend:\*\* HTML, CSS, JavaScript

\- \*\*Backend:\*\* Python

\- \*\*Model Storage:\*\* Pickle



\## Project Structure



```text

phishing\_project/

│

├── artifacts/

│   ├── model.pkl

│   └── metrics.json

│

├── backend/

│   ├── \_\_init\_\_.py

│   ├── dataset.py

│   └── features.py

│

├── frontend/

│   ├── index.html

│   ├── script.js

│   └── style.css

│

├── app.py

├── train\_model.py

├── requirements.txt

└── .gitignore

```



\## Installation and Setup



\### 1. Clone the repository



```bash

git clone https://github.com/Iramkazi06/TNS\_Project\_PhishingURLDetector.git

```



\### 2. Navigate to the project directory



```bash

cd TNS\_Project\_PhishingURLDetector

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Run the application



```bash

python app.py

```



Follow the application output to access the web interface.



\## Model Training



To train the machine learning model, run:



```bash

python train\_model.py

```



The trained model and evaluation metrics are stored in the `artifacts/` directory.



\## Future Improvements



\- Improve model accuracy and generalization.

\- Add additional URL security features.

\- Enhance the user interface.

\- Integrate real-time phishing URL intelligence.

\- Improve prediction explanations.



\## Author



\*\*Iram Kazi\*\*



GitHub: \[@Iramkazi06](https://github.com/Iramkazi06)



\## Repository



\[Phishing URL Detector – GitHub](https://github.com/Iramkazi06/TNS\_Project\_PhishingURLDetector)



