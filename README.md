1.โครงสร้าง Folder ย่อย (directory tree)
C:.
|   README.doc
|   
+---demo
+---doc
|       62tan55.pdf
|       62tan55_abstract_en.txt
|       62tan55_abstract_th.txt
|       
+---exam
|       62tan55_exam.mp4
|       62tan55_exam.png
|       
\---src
    +---client
    |   |   .gitignore
    |   |   package-lock.json
    |   |   package.json
    |   |   README.md
    |   |   
    |   +---public
    |   |       favicon.ico
    |   |       index.html
    |   |       logo.png
    |   |       manifest.json
    |   |       robots.txt
    |   |       
    |   \---src
    |       |   App.js
    |       |   home.js
    |       |   index.js
    |       |   serviceWorker.js
    |       |   setupTests.js
    |       |   styles.css
    |       |   
    |       \---components
    |           +---chart
    |           |       BarChartCount.js
    |           |       chartBox.js
    |           |       ChartOverAll7Days.js
    |           |       LineChartRetweetCount.js
    |           |       LineChartRetweetPerMinute.js
    |           |       LineChartTweetCount.js
    |           |       MixChart.js
    |           |       
    |           +---header
    |           |       NavBar.js
    |           |       
    |           +---search
    |           |       autocompleteSearch.js
    |           |       result.js
    |           |       search.css
    |           |       
    |           +---trends
    |           |   |   cards.js
    |           |   |   HashtagTrends.js
    |           |   |   TrendsBox.js
    |           |   |   TweetTrends.css
    |           |   |   TweetTrends.js
    |           |   |   
    |           |   \---img
    |           |           heart.png
    |           |           retweet.png
    |           |           Thammasat.png
    |           |           
    |           +---tweet
    |           |       TweetBox.js
    |           |       
    |           \---wordCloud
    |                   wordCloud.js
    |                   
    +---crawler
    |   |   .DS_Store
    |   |   BackupData.py
    |   |   checkStateData.py
    |   |   DataAnalysis.py
    |   |   DataCleansing.py
    |   |   DataCleansing.pyc
    |   |   DataVisualization.py
    |   |   filterAPI.json
    |   |   GetAutoComplete.py
    |   |   GetCard.py
    |   |   GetGraph.py
    |   |   GetTopTweet.py
    |   |   GetWordclouds.py
    |   |   keywordFilter.json
    |   |   keywordSearch.json
    |   |   main.py
    |   |   README.md
    |   |   retweetPerMinCollection.py
    |   |   searchAPI.json
    |   |   TwitterFilter.py
    |   |   TwitterSearch.py
    |   |   
    |   +---.vscode
    |   |       settings.json
    |   |       
    |   \---__pycache__
    |           DataCleaning.cpython-37.pyc
    |           DataCleansing.cpython-36.pyc
    |           DataCleansing.cpython-37.pyc
    |           GetWordclouds.cpython-36.pyc
    |           GetWordclouds.cpython-37.pyc
    |           TwitterSearch.cpython-37.pyc
    |           
    \---server
        |   package-lock.json
        |   package.json
        |   server.js
        |   
        +---config
        |       database.js
        |       
        +---controllers
        |       .controller.js.swp
        |       controller.js
        |       
        +---helper
        +---models
        |       graphModel.js
        |       
        \---routes
                route.js
 
2.วิธีการติดตั้งโปรแกรม
2.1) ติดตั้ง Environment สำหรับการทำงานของระบบ

	2.1 วิธีติดตั้ง Python และ Library ที่เกี่ยวข้องสำหรับงานวิจัย
2.1.1 การติดตั้ง Python
ในงานวิจัยได้ใช้ภาษา Python Version 3.6.6 โดยจะมีขั้นตอนการติดตั้งดังนี้
1.	ดาวน์โหลดภาษา Python โดยไปที่หน้าดาวน์โหลดของภาษา Python ได้ที่ลิงค์ https://www.python.org/downloads/ เพื่อดาวน์โหลดโปรแกรมลงคอมพิวเตอร์
 
2.	ในหน้าดาวน์โหลด จะปรากฏ package ของภาษา Python ให้ดาวน์โหลด Version 3.6 	
 
3.	หลังจากนั้นเข้ามาในหน้าของVersion 3.6.6 ให้เลื่อนลงมาในส่วนของ Files จะเห็นรายการของ Python package ที่รองรับ ให้เลือกแพลตฟอร์มที่ต้องการ หลังจากนั้นให้รอจนกว่าการดาวน์โหลดจะเสร็จสมบูรณ์
 
4.	ต่อไปเป็นขั้นตอนการติดตั้งภาษา Python ให้ไปที่สถานที่ที่ดาวน์โหลดภาษา Python ไว้และคลิกที่ไฟล์ "python-3.6.6.exe" และคลิกที่ "Run"
5.	หลังจากนั้นหน้าต่างของการติดตั้งจะปรากฏขึ้นมา คลิกเลือกที่ "Add Python 3.6 to PATH" เพื่อให้ระบบทำการกำหนด PATH เพื่อให้ภาษา Python สามารถทำงานได้กับ Command line อัตโนมัติในทุกที่ คลิกที่ "Install now " เพื่อเริ่มการติดตั้งภาษา Python อาจจะเปลี่ยนแปลงตัวเลือกสำหรับการติดตั้งด้วยตัวเองโดยเลือกที่ "Customize install" เช่น เปลี่ยนสถานที่ที่ต้องการติดตั้ง เป็นต้น
6.	รอจนกว่าการติดตั้งจะเสร็จ หลังจากที่การติดตั้งเสร็จสิ้นแล้ว คลิก "Close" เพื่อเสร็จสิ้นการติดตั้งภาษา Python
2.1.2 การติดตั้ง Library ที่เกี่ยวข้องกับงานวิจัย
1. pymongo >> pip install pymongo
2. TwitterAPI >> pip install TwitterAPI
3. smtplib >> pip install smtplib
4. matplotlib >> pip install matplotlib
2.2 วิธีติดตั้ง Node.js
	Node.js เป็น Platform ที่เขียนด้วย Javascript เพื่อใช้เป็น Web Server โดยมีขั้นตอนการติดตั้งดังนี้
1.	ดาวน์โหลด Node.js ได้ที่ https://nodejs.org/en/download/ แล้วเลือก package ที่ต้องการสำหรับแพล็ตฟอร์มของตนเอง
 
2.	เลือกตำแหน่งที่ต้องการแล้วกด Save จากนั้น Install เพื่อทำการติดตั้ง
 
3.	ทำการติดตั้งตามขั้นตอน เมื่อติดตั้งเสร็จแล้ว สามารถตรวจสอบ Version ที่ได้ติดตั้งได้ที่  Command line และพิมพ์คำว่า “node -v” จะแสดง Version ที่ได้ติดตั้ง เป็นอันเสร็จสิ้นขั้นตอน
 

2.3 วิธีติดตั้ง Express.js
Express.js เป็น Web application Framework บน Node.js โดยก่อนจะติดตั้ง Express.js ต้องติดตั้ง Node.js ให้เรียบร้อยก่อน สำหรับการติดตั้ง Express.js จะมีขั้นตอนดังนี้
1.	เปิด Command line สร้างโฟลเดอร์สำหรับเป็นที่อยู่ของโปรแกรม
 
2.	พิมพ์คำสั่ง npm init เพื่อสร้าง package.json สำหรับเก็บรายละเอียดของโปรแกรม
 
3.	ติดตั้ง express ลงใน Directory (save จะเก็บข้อมูลว่าได้ลง express Version นี้ลงใน package.json)
 

2.4 วิธีติดตั้ง React.js
	React.js เป็น Javascript Library โดยก่อนจะติดตั้ง React.js ต้องติดตั้ง Node.js ให้เรียบร้อยก่อน สำหรับการติดตั้ง React.js จะมีขั้นตอนดังนี้
1.	เปิด Command line สร้างโฟลเดอร์สำหรับเป็นที่อยู่ของโปรแกรม
 
2.	พิมพ์คำสั่ง npm init เพื่อสร้าง package.json สำหรับเก็บรายละเอียดของโปรแกรม
3.	พิมพ์คำสั่ง npm install --save react react-dom เพื่อติดตั้ง package
 
4.	พิมพ์คำสั่ง npm install -g create-react-app เพื่อสร้างไฟล์โปรเจ็ค
 
5.	พิมพ์คำสั่ง create-react-app <<ชื่อโฟลเดอร์>> เพื่อสร้างโฟลเดอร์สำหรับโปรเจ็ค
 
6.	ทดลองรันโดยใช้คำสั่ง npm start (เข้าไปที่โฟลเดอร์ของโปรเจ็คก่อน) เมื่อรันสำเร็จจะสามารถเปิดแอปพลิเคชันได้ที่ http://localhost:3000/ ดังภาพ
 


2.5 วิธีติดตั้ง MongoDB Service การทำ Authentication และตั้งค่า Replica
2.5.1 การติดตั้ง MongoDB Service ในงานวิจัยจะเป็นการติดตั้งบนระบบปฏิบัติการ Ubuntu 18.04 x64 ซึ่งจะมีขั้นตอนดังนี้
1. เปิด Terminal แล้วพิมพ์คำสั่งดังต่อไปนี้เพื่อเป็นการ Set Environment
>> sudo apt-get install gnupg
>> wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add-
>> echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
>> sudo apt-get update
2. พิมพ์คำสั่งต่อไปนี้ สำหรับการดาวน์โหลด MongoDB Service
>> sudo apt-get install -y mongodb-org
>> echo "mongodb-org hold" | sudo dpkg --set-selections
>> echo "mongodb-org-server hold" | sudo dpkg --set-selections
>> echo "mongodb-org-shell hold" | sudo dpkg --set-selections
>> echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
>> echo "mongodb-org-tools hold" | sudo dpkg --set-selections
3. หลังจากติดตั้งเสร็จร้อย ต่อไปจะเป็นคำสั่งการรัน Mongo Service เบื้องต้น
>> mongod // การเริ่มต้นเปิดเซิร์ฟเวอร์ MongoDB บนเครื่องของเรา (นิยมใช้แบบ Local)
>> mongo // การเริ่มต้นใช้งาน Mongo เพื่อจัดการกับ database
>> sudo service mongod start // การเริ่มต้นเปิดเซิร์ฟเวอร์ MongoDB แบบ service (นิยมใช้เพื่อรับ Request จากภายนอก)
>> sudo service mongod status // การเช็คสถานะของเซิร์ฟเวอร์ MongoDB Service
>> sudo service mongod restart // การรีสตาร์ทเซิร์ฟเวอร์ กรณีที่มีการ Config Server Mongo หรือเกิด Error 
>> sudo service mongod stop // การยุติการเปิดเซิร์ฟเวอร์ MongoDB แบบ Service 
2.5.2 การทำ Authentication ให้กับ MongoDB Service เพื่อให้เซิร์ฟเวอร์ MongoDB มีความปลอดภัยของข้อมูลมากยิ่งขึ้น (ป้องกันการถูก Hack ข้อมูลจากภายนอก) โดยมีขั้นตอนดังนี้
1. เปิด Terminal และรัน Service ของ MongoDB 
>> sudo service mongod start 
2. พิมพ์คำสั่ง Mongo
>> Mongo 
3. เข้า db admin เพื่อสร้าง super admin
>> use admin
4. สร้าง super admin
>> db.createUser({
User: “useradmin”,
Pwd: “password”,
roles: [{role: “root”, db: “admin”}]})

5. เข้าไป enabled Auth ในไฟล์ Mongod.conf ผ่าน Terminal
>> sudo vi /etc/mongod.conf
6. แก้ไขไฟล์ mongod.conf โดยเพิ่มให้ Mongo สามารถ Authorization และแก้ไขเลข IP ให้สามารถเชื่อมต่อจากภายนอกได้
 
7. จากนั้น restart mongo service
>> sudo service mongod restart
2.5.3 การตั้งค่า Replica เพื่อให้ MongoDB สลับกันเป็น Primary ได้ ในกรณีที่ตัวเก็บข้อมูลที่ Primary มีปัญหา ก็สามารถสลับไปใช้ Secondary ได้ โดยมีขั้นตอนการตั้งค่าดังนี้
1. เปิด Terminal และรัน Service ของ MongoDB
>> sudo service mongod start 
2. รัน Mongo ด้วย user superadmin ที่ได้สร้างไปในหัวข้อที่แล้ว
>> mongo –username <<ไอดีที่ได้สร้างไป>> --password <<พาสเวิร์ดที่ได้สร้างไป>> --authenticationDatabase admin
3. สร้าง Replica Secondary
>> rs.initiate()
4. สร้าง Replica Primary
>> rs.initiate()
5. เข้าไปใส่ชื่อ Replica ที่ได้สร้างไปในไฟล์ mongod.conf โดยชื่อ Replica จะเป็นชื่อ “rs0” (สามารถกำหนดชื่อได้เองตอนสร้าง replica)
>> sudo vi /etc/mongod.conf
6. แก้ไขไฟล์ mongod.conf โดยเพิ่มในส่วนของ Replication ดังภาพ
 
7. จากนั้น restart mongo service
>> sudo service mongod restart
เมื่อ Config ข้อมูลในไฟล์ mongod.conf เสร็จจะได้ดังภาพด้านล่าง
 
2.6 วิธีติดตั้ง Mongo Compass
	Mongo Compass คือโปรแกรม user interface สำหรับ MongoDB สำหรับการดูข้อมูลภายในฐานข้อมูล มีวิธีการติดตั้งดังนี้
1.	ดาวน์โหลดไฟล์ จากเว็ปไซต์ https://www.mongodb.com/download-center/compass เลือก Version และ แพล็ตฟอร์มที่ต้องการ
 
2.	ติดตั้งเสร็จเรียบร้อย ขั้นตอนต่อไปคือการกรอกเพื่อเข้าดูข้อมูลภายในฐานข้อมูล โดยมีตัวอย่างดังภาพข้างล่างนี้
 




     2.2) การรันโปรแกรม
      การรันโปรแกรมนั้นจะแบ่งออกเป็น 3 ส่วน ตาม Folder /src ที่ได้จัดเก็บ source code เริ่มจาก
1.	โฟลเดอร์ crawler เป็น Folder สำหรับเก็บข้อมูลจากทวิตเตอร์ โดยจะรันไฟล์ทั้งหมด 3 ไฟล์ต่อไปนี้
a.	ไฟล์ TwitterFilter.py 
>> cd src/crawler (ชี้ไปที่ตำแหน่งที่อยู่ของไฟล์)
>> python3 TwitterFilter.py
b.	ไฟล์ TwitterSearch.py
>> cd src/crawler (ชี้ไปที่ตำแหน่งที่อยู่ของไฟล์)
>> python3 TwitterSearch.py
c.	ไฟล์ main.py
>> cd src/crawler (ชี้ไปที่ตำแหน่งที่อยู่ของไฟล์)
>> python3 TwitterSearch.py
หากพบ error จากการรัน python3 ควรเช็ค environment ว่าได้มีการติดตั้งครบเรียบร้อยหรือยัง
ตัวอย่าง error ที่อาจเกิดขึ้น เช่น 
ยังไม่ได้ลง package ที่จำเป็นของ python3
ยังไม่ได้ทำการ Authentication หรือตั้งค่า replica ให้กับ mongodb

2.	โฟลเดอร์ client เป็น Folder สำหรับแสดงผลหน้าเว็ปแอปพลิเคชัน โดยมีวิธีการรันดังนี้
>> cd src/client (ชี้ไปที่ตำแหน่งที่อยู่ของไฟล์)
>> npm start
หากพบ error จากการรัน ควรเช็ค environment ว่าได้มีการติดตั้งครบเรียบร้อยหรือยัง
ตัวอย่าง error ที่อาจเกิดขึ้น เช่น 
ยังไม่ได้ลง module ที่จำเป็นของทางฝั่ง client โดยสามารถเช็ค module ที่จำเป็นได้จากไฟล์ package.json ที่ dependencies

3.	โฟลเดอร์ server เป็น Folder สำหรับรับส่งข้อมูลระหว่างผู้ใช้กับฐานข้อมูล โดยมีวิธีการรันดังนี้
>> cd src/server (ชี้ไปที่ตำแหน่งที่อยู่ของไฟล์)
>> node server.js
หากพบ error จากการรัน ควรเช็ค environment ว่าได้มีการติดตั้งครบเรียบร้อยหรือยัง
ตัวอย่าง error ที่อาจเกิดขึ้น เช่น 
ยังไม่ได้ลง module ที่จำเป็นของทางฝั่ง server โดยสามารถเช็ค module ที่จำเป็นได้จากไฟล์ package.json ที่ dependencies

