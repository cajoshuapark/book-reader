# book-reader

## **Purpose:**
Mobile Reactjs app for adding new tray to database, loading tray to high density, and unloading tray from high density.

## **Setup:** 
1. log into ROOT remote server
2. clone frontend
```
cd /opt
git clone git@github.com:intravisiongroup/rfid-reader.git
```
3. install dependencies
```
npm install
```
4. create systemd file
```
nano /lib/systemd/system/react.service
```
copy the following in the react.service file
```
[Unit]
Description=start frontend
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/rfid-reader/clientjs
Environment=CI=true
StandardOutput=inherit
StandardError=inherit
Restart=always
ExecStart=npm run start

[Install]
WantedBy=multi-user.target
```
5. go back to root
6. repeat the same process to set up the graphql server
```
nano /lib/systemd/system/graphql.service
```
copy the following in the graphql.service file
```
[Unit]
Description=Start graphql
After=network.target

[Service]
User=root
WorkingDirectory=/opt/rfid-reader/
ExecStart=openapi-to-graphql --port=3001 swagger.json
Restart=always

[Install]
WantedBy=multi-user.target
```
7. Enable and start the services
```
systemctl start react
systemctl enable react
systemctl start graphql
systemctl enable graphql
```

## **Pages:** 
- **Home Page**
  - Link to Tray Page
  - Link to Loading/Unloading Page
  - <img src="https://user-images.githubusercontent.com/114508632/203146483-ec5dcf7c-ccff-4e2f-bac0-34162100053a.jpg" width="30%" height="30%">

- **Tray Page**
  - Purpose: add new tray to database by scanning and writing on the front and rear rfid tags
  - RFID Scan
  - RFID Write
  - <img src="https://user-images.githubusercontent.com/114508632/203146621-b52e5981-adcf-43ab-a0a5-5651a7942fc4.jpg" width="30%" height="30%">

- **Loading/Unloading Page**
  - Purpose: load and unload tray from rack
  - RFID Scan
  - RFID Write
  - QR Code Scanner
  - <img src="https://user-images.githubusercontent.com/114508632/203146715-cdc6b9eb-8b06-4936-8f0f-b1c9bacdd56a.jpg" width="30%" height="30%">
  - <img src="https://user-images.githubusercontent.com/114508632/203148200-801d5652-752c-464e-bd4b-b73ddc1a0ab5.jpg" width="30%" height="30%">
  - <img src="https://user-images.githubusercontent.com/114508632/203148091-7bd198ca-ff72-457f-958e-196d1d3f09da.jpg" width="30%" height="30%">

## **Workflow:** 
- **Tray Page**
  - Click on scan button and hold FRONT RFID tag on the back of your phone
  - Repeat with REAR RFID tag
  - Once both sides of the tray have been scanned, page will automatically reset to scan the next tray
  - Once you start the scanning process, you can delete the tray by pressing the restart button 
  - Expected: Scan and write with one click
  - Actual: Sometimes it will only scan and not write. Write button has been created for this situation
  - https://user-images.githubusercontent.com/114508632/203147635-4668cceb-fb69-42e6-9eb3-03cc1e101b5e.mp4


  
- **Loading/Unloading Page**
  - Scan front or back of tray
  - Write on RFID tag once batch Id has been fetched
  - Scan QR Code to check if tray went to the right location
  - https://user-images.githubusercontent.com/114508632/203147868-84352887-e581-44d6-8c38-a71dd48d26b4.mp4

## **Technical Features:** 
- **RFID Scanner**
  - Can record tray condition
  - Can show number fetched
  - Can record datetime
  - Can show past loading history
  - Web api used: https://developer.mozilla.org/en-US/docs/Web/API/NDEFReader/NDEFReader
  
- **RFID Writer**
  - Writes on rfid tag which contains Tray ID, Rfid Position, and the Unit BatchId
  - Web api used: https://developer.mozilla.org/en-US/docs/Web/API/NDEFReader/NDEFReader
  
- **QR code scanner**
  - Scans QR which fetches the location and checks if tray went to the right location
  - A post request to MQTT server is made once fetched (in the works)
  - package used: https://www.npmjs.com/package/react-qr-reader

## **Device Requirement:**
- ONLY works on Android Chrome 

## **Live Server link:** 
- https://rfid.ivgn1.com:3000

