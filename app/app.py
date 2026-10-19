import http.server
import json
import os
import socket
import time

PORT = 8080
START_TIME = time.time()
VERSION = os.environ.get("APP_VERSION", "1.0.0")
FEATURE_PINNED = os.environ.get("FEATURE_PINNED", "false").lower() == "true"


class NoticeBoardHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):
    if self.path == "/healthz":
      # Version 1.2.0-broken never returns 200 to simulate a failed rollout
      if VERSION == "1.2.0-broken":
        self.send_response(500)
        self.end_headers()
        self.wfile.write(b"Broken health check")
        return

      # Warmup: return 500 for the first 5 seconds after startup
      elapsed = time.time() - START_TIME
      if elapsed < 5:
        self.send_response(500)
        self.end_headers()
        self.wfile.write(b"Warming up...")
      else:
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    elif self.path == "/version":
      self.send_response(200)
      self.send_header("Content-Type", "application/json")
      self.end_headers()
      data = {
          "version": VERSION,
          "student": "02230128",
          "pod": socket.gethostname(),
      }
      self.wfile.write(json.dumps(data).encode("utf-8"))

    elif self.path == "/notices":
      self.send_response(200)
      self.send_header("Content-Type", "application/json")
      self.end_headers()
      notices = [
          {"id": 1, "title": "Welcome to CST", "content": "Lab session active."},
          {
              "id": 2,
              "title": "Cluster Maintenance",
              "content": "Scheduled tonight.",
          },
          {
              "id": 3,
              "title": "Notice Board v2",
              "content": "New features online.",
          },
      ]
      # Versions 1.1.0 and 1.2.0 add category and pinned fields
      if VERSION in ["1.1.0", "1.2.0-broken"]:
        for n in notices:
          n["category"] = "general"
          n["pinned"] = FEATURE_PINNED if n["id"] == 1 else False
      self.wfile.write(json.dumps(notices).encode("utf-8"))
    else:
      self.send_response(404)
      self.end_headers()


if __name__ == "__main__":
  server = http.server.HTTPServer(("0.0.0.0", PORT), NoticeBoardHandler)
  print(f"Server started for version {VERSION} on port {PORT}")
  server.serve_forever()