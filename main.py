from flask import Flask, jsonify, request
import datetime


app = Flask(__name__)


@app.route("/api", methods=["GET"])
def hng_stage_one():
    # parameters
    slack_name = str(request.args.get("slack_name"))
    track = str(request.args.get("track"))

    today = datetime.date.today().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    github_file_url = "https://github.com/Lawole/HNG_stage_one/blob/master/main.py"
    github_repo_url = "https://github.com/Lawole/HNG_stage_one"

    response = {
                "slack_name": slack_name,
                "current_day": today,
                "utc_time": utc_time,
                "track": track,
                "github_file_url": github_file_url,
                "github_repo_url": github_repo_url,
                "status_code": 200
            }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
