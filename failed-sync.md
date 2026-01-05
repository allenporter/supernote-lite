Webserver log:
```
10.10.38.129 [04/Jan/2026:16:13:19 -0800] "POST /api/file/2/files/synchronous/start HTTP/1.1" 200 226 "-" "okhttp/5.1.0"
Trace: POST /api/file/2/files/list_folder (Body: 60 bytes)
10.10.38.129 [04/Jan/2026:16:13:19 -0800] "POST /api/file/2/files/list_folder HTTP/1.1" 200 6466 "-" "okhttp/5.1.0"
Trace: POST /api/file/3/files/query/by/path_v3 (Body: 68 bytes)
10.10.38.129 [04/Jan/2026:16:13:19 -0800] "POST /api/file/3/files/query/by/path_v3 HTTP/1.1" 404 214 "-" "okhttp/5.1.0"
Trace: POST /api/file/2/files/synchronous/end (Body: 43 bytes)
10.10.38.129 [04/Jan/2026:16:13:19 -0800] "POST /api/file/2/files/synchronous/end HTTP/1.1" 200 176 "-" "okhttp/5.1.0"
```

Trace log
```
{"timestamp": 1767571999.261002, "method": "POST", "url": "http://10.10.38.83:8080/api/file/2/files/synchronous/start", "headers": {"x-access-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGxlbi5wb3J0ZXJAZ21haWwuY29tIiwiZXF1aXBtZW50X25vIjoiU04wNzhDMTAwMDE1NTAiLCJpYXQiOjE3Njc1NzE2OTIsImV4cCI6MTc2NzY1ODA5Mn0.NuAbWx30VcRst-RCeZoGVMP_F7crtQTvuiw1aaaoZwA", "channel": "", "Content-Type": "application/json; charset=UTF-8", "Content-Length": "32", "Host": "10.10.38.83:8080", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/5.1.0"}, "body": "{\"equipmentNo\":\"SN078C10001550\"}"}
{"timestamp": 1767571999.366871, "method": "POST", "url": "http://10.10.38.83:8080/api/file/2/files/list_folder", "headers": {"x-access-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGxlbi5wb3J0ZXJAZ21haWwuY29tIiwiZXF1aXBtZW50X25vIjoiU04wNzhDMTAwMDE1NTAiLCJpYXQiOjE3Njc1NzE2OTIsImV4cCI6MTc2NzY1ODA5Mn0.NuAbWx30VcRst-RCeZoGVMP_F7crtQTvuiw1aaaoZwA", "channel": "", "Content-Type": "application/json; charset=UTF-8", "Content-Length": "60", "Host": "10.10.38.83:8080", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/5.1.0"}, "body": "{\"path\":\"/\",\"recursive\":true,\"equipmentNo\":\"SN078C10001550\"}"}
{"timestamp": 1767571999.6066759, "method": "POST", "url": "http://10.10.38.83:8080/api/file/3/files/query/by/path_v3", "headers": {"x-access-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGxlbi5wb3J0ZXJAZ21haWwuY29tIiwiZXF1aXBtZW50X25vIjoiU04wNzhDMTAwMDE1NTAiLCJpYXQiOjE3Njc1NzE2OTIsImV4cCI6MTc2NzY1ODA5Mn0.NuAbWx30VcRst-RCeZoGVMP_F7crtQTvuiw1aaaoZwA", "channel": "", "Content-Type": "application/json; charset=UTF-8", "Content-Length": "68", "Host": "10.10.38.83:8080", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/5.1.0"}, "body": "{\"path\":\"/DOCUMENT/Document/Archive\",\"equipmentNo\":\"SN078C10001550\"}"}
{"timestamp": 1767571999.6327832, "method": "POST", "url": "http://10.10.38.83:8080/api/file/2/files/synchronous/end", "headers": {"x-access-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGxlbi5wb3J0ZXJAZ21haWwuY29tIiwiZXF1aXBtZW50X25vIjoiU04wNzhDMTAwMDE1NTAiLCJpYXQiOjE3Njc1NzE2OTIsImV4cCI6MTc2NzY1ODA5Mn0.NuAbWx30VcRst-RCeZoGVMP_F7crtQTvuiw1aaaoZwA", "channel": "", "Content-Type": "application/json; charset=UTF-8", "Content-Length": "43", "Host": "10.10.38.83:8080", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/5.1.0"}, "body": "{\"equipmentNo\":\"SN078C10001550\",\"flag\":\"N\"}"}`
```
