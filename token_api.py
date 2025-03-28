from flask import Flask, jsonify
from google.oauth2 import service_account
import google.auth.transport.requests

app = Flask(__name__)

# Load credentials
SERVICE_ACCOUNT_FILE = "tensile-courier-454917-t6-e1e6496ec6ba.json"
SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]  # Modify scope as needed

@app.route("/token", methods=["GET"])
def get_token():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        request = google.auth.transport.requests.Request()
        credentials.refresh(request)
        return jsonify({"access_token": credentials.token})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
